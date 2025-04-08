from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db_connection():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to the Community Library Management System"})

@app.get("/books", response_class=JSONResponse)
async def list_books():
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM Books").fetchall()
    conn.close()
    return {"books": [dict(row) for row in books]}

@app.get("/joined_data", response_class=JSONResponse)
async def joined_data():
    conn = get_db_connection()
    query = """
        SELECT b.Title, b.ISBN, a.Name as AuthorName
        FROM Books b
        JOIN Authors a ON b.Author_ID = a.Author_ID;
    """
    results = conn.execute(query).fetchall()
    conn.close()
    return {"joined_data": [dict(row) for row in results]}

@app.post("/add_book")
async def add_book(title: str = Form(...), isbn: str = Form(...), author_id: int = Form(...), publisher: str = Form(...)):
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO Books (Title, ISBN, Author_ID, Publisher) VALUES (?, ?, ?, ?)",
            (title, isbn, author_id, publisher)
        )
        conn.commit()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.post("/update_book/{book_id}")
async def update_book(book_id: int, title: str = Form(...), isbn: str = Form(...), author_id: int = Form(...), publisher: str = Form(...)):
    conn = get_db_connection()
    try:
        conn.execute(
            "UPDATE Books SET Title = ?, ISBN = ?, Author_ID = ?, Publisher = ? WHERE Book_ID = ?",
            (title, isbn, author_id, publisher, book_id)
        )
        conn.commit()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete_book/{book_id}")
async def delete_book(book_id: int):
    conn = get_db_connection()
    try:
        conn.execute("DELETE FROM Books WHERE Book_ID = ?", (book_id,))
        conn.commit()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    conn.close()
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
