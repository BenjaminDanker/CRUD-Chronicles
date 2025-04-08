-- insert.sql

-- Insert sample data into Authors
INSERT INTO Authors (AuthorID, FirstName, LastName, BirthYear, Nationality)
VALUES
(1, 'George', 'Orwell', 1903, 'British'),
(2, 'Jane', 'Austen', 1775, 'British'),
(3, 'Bob', 'Hone', 1900, 'British'),
(4, 'Billy', 'Steve', 1740, 'British');

-- Insert sample data into Books
INSERT INTO Books (ISBN, Title, AuthorID, Publisher, YearPublished)
VALUES
('9780451524935', '1984', 1, 'Secker & Warburg', 1949),
('9780141439518', 'Pride and Prejudice', 2, 'T. Egerton', 1813),
('9780451524945', '1944', 3, 'Billys Journey', 1901),
('9780141439543', 'The Big Town', 4, 'Pubilisher Co.', 1885);

-- Insert sample data into Members
INSERT INTO Members (MemberID, FirstName, LastName, Email, Phone)
VALUES
(100, 'Alice', 'Smith', 'alice.smith@example.com', '555-1234'),
(101, 'Bob', 'Jones', 'bob.jones@example.com', '555-5678'),
(102, 'Joey', 'Smith', 'joey.smith@example.com', '555-1334'),
(103, 'Chris', 'Jones', 'Chris.jones@example.com', '555-5673');

-- Insert sample data into Loans
INSERT INTO Loans (LoanID, MemberID, ISBN, LoanDate, DueDate)
VALUES
(1000, 100, '9780451524935', '2025-03-01', '2025-03-15'),
(1001, 101, '9780141439555', '2025-03-05', '2025-03-19'),
(1002, 102, '9780451524934', '2025-03-01', '2025-03-15'),
(1003, 103, '9780141439523', '2025-03-05', '2025-03-19');