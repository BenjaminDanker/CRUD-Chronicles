from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
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
    # Example join between Books and Authors. Modify field names and join conditions as per your schema.
    conn = get_db_connection()
    query = """
        SELECT b.Title, b.ISBN, a.Name as AuthorName
        FROM Books b
        JOIN Authors a ON b.Author_ID = a.Author_ID;
    """
    results = conn.execute(query).fetchall()
    conn.close()
    return {"joined_data": [dict(row) for row in results]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
