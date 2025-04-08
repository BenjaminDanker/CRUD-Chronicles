
# Community Library Management System

This project is a CRUD application that manages a community library using FastAPI and SQLite. The web application provides a simple interface for performing create, read, update, and delete operations on books, as well as displaying joined data from related tables (Books and Authors).

## Features

- **CRUD Operations:**  
  Create, update, and delete books in the database.

- **Dynamic Update Forms:**  
  Each book row in the list includes an “Edit” button that navigates to a dedicated update page with pre-populated information.

- **AJAX-Based Deletion:**  
  The delete button removes a book row from the UI instantly without a full page reload.

- **Template Inheritance:**  
  All pages extend a common base template for a consistent look and feel.

- **Joined Data Display:**  
  The application shows join results combining book titles with author names.

## Technologies Used

- **Backend:** FastAPI, SQLite
- **Frontend:** Jinja2 templates, HTML, JavaScript (AJAX)
- **Server:** Uvicorn

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/BenjaminDanker/CRUD-Chronicles.git
   ```
2. **Navigate into the Repository:**
   ```bash
   cd CRUD-Chronicles
   ```
3. **Install the Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Prepare the Database:**
   Ensure your SQLite database (`data.db`) has been created using the provided SQL scripts (`create.sql`, `insert.sql`, and `crud.sql`).

### Running the Application

1. **Start the FastAPI Server:**
   ```bash
   uvicorn main:app --reload
   ```
2. **Open in Browser:**  
   Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the application.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Special thanks to Professor Lu for guidance in this course.
- Appreciation to all online resources and communities that provided support for FastAPI and AJAX implementations.
