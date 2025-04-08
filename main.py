from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db_connection():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/books", response_class=HTMLResponse)
async def list_books(request: Request):
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM Books").fetchall()
    conn.close()
    books_list = [dict(book) for book in books]
    return templates.TemplateResponse("books.html", {"request": request, "books": books_list})

@app.get("/update_book/{isbn}", response_class=HTMLResponse)
async def get_update_book(isbn: str, request: Request):
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM Books WHERE ISBN = ?", (isbn,)).fetchone()
    conn.close()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book_data = dict(book)
    return templates.TemplateResponse("update_book.html", {"request": request, "book": book_data})

@app.post("/update_book/{isbn}")
async def update_book(isbn: str,
                      title: str = Form(...),
                      new_isbn: str = Form(None),
                      author_id: int = Form(...),
                      publisher: str = Form(...),
                      year_published: int = Form(...)):
    # If new_isbn is not provided, default to the original ISBN.
    if not new_isbn:
        new_isbn = isbn
    conn = get_db_connection()
    try:
        conn.execute(
            "UPDATE Books SET Title = ?, ISBN = ?, AuthorID = ?, Publisher = ?, YearPublished = ? WHERE ISBN = ?",
            (title, new_isbn, author_id, publisher, year_published, isbn)
        )
        conn.commit()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    conn.close()
    return RedirectResponse(url="/books", status_code=303)

@app.get("/joined_data", response_class=HTMLResponse)
async def joined_data(request: Request):
    conn = get_db_connection()
    query = """
        SELECT b.Title, b.ISBN, a.FirstName || ' ' || a.LastName as AuthorName
        FROM Books b
        JOIN Authors a ON b.AuthorID = a.AuthorID;
    """
    results = conn.execute(query).fetchall()
    conn.close()
    joined_list = [dict(row) for row in results]
    return templates.TemplateResponse("joined_data.html", {"request": request, "joined_data": joined_list})

@app.post("/add_book")
async def add_book(title: str = Form(...), 
                   isbn: str = Form(...), 
                   author_id: int = Form(...), 
                   publisher: str = Form(...),
                   year_published: int = Form(...)):
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO Books (Title, ISBN, AuthorID, Publisher, YearPublished) VALUES (?, ?, ?, ?, ?)",
            (title, isbn, author_id, publisher, year_published)
        )
        conn.commit()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete_book/{isbn}")
async def delete_book(isbn: str):
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM Books WHERE ISBN = ?", (isbn,))
        conn.commit()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    conn.close()
    return RedirectResponse(url="/books", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
