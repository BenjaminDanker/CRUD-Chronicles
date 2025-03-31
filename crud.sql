-- crud.sql

-- SELECT: Read all books along with their authors
SELECT b.ISBN, b.Title, a.FirstName, a.LastName
FROM Books b
JOIN Authors a ON b.AuthorID = a.AuthorID;

-- INSERT: Create a new member
INSERT INTO Members (MemberID, FirstName, LastName, Email, Phone)
VALUES (102, 'Charlie', 'Brown', 'charlie.brown@example.com', '555-9012');

-- UPDATE: Update a member's email address
UPDATE Members
SET Email = 'alice.newemail@example.com'
WHERE MemberID = 100;

-- DELETE: Remove a loan record
DELETE FROM Loans
WHERE LoanID = 1001;
