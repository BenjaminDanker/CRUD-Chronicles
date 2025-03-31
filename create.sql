-- create.sql
-- Table: Authors
-- Functional Dependencies:
--   AuthorID -> FirstName, LastName, BirthYear, Nationality
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthYear INT,
    Nationality VARCHAR(50)
);

-- Table: Books
-- Functional Dependencies:
--   ISBN -> Title, AuthorID, Publisher, YearPublished
CREATE TABLE Books (
    ISBN VARCHAR(20) PRIMARY KEY,
    Title VARCHAR(100),
    AuthorID INT,
    Publisher VARCHAR(100),
    YearPublished INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

-- Table: Members
-- Functional Dependencies:
--   MemberID -> FirstName, LastName, Email, Phone
CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20)
);

-- Table: Loans
-- Functional Dependencies:
--   LoanID -> MemberID, ISBN, LoanDate, DueDate
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY,
    MemberID INT,
    ISBN VARCHAR(20),
    LoanDate DATE,
    DueDate DATE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (ISBN) REFERENCES Books(ISBN)
);
