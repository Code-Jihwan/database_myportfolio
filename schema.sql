CREATE DATABASE mylibrary;
USE mylibrary;

CREATE TABLE Books (
	id INT auto_increment primary key,
    title varchar(100) NOT NULL,
    author varchar(50),
    publish_year INT,
    isbn varchar(13) unique NOT NULL
);

CREATE TABLE Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    join_date DATE NOT NULL,
    gender ENUM('M', 'F')
);

CREATE TABLE Loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(id),
    FOREIGN KEY (member_id) REFERENCES Members(id),
    status ENUM('대출중', '반납') DEFAULT '대출중'
);

select * from mylibrary.Books;
select * from mylibrary.Members;
select * from mylibrary.Loans;

INSERT INTO Books (title, author, publish_year, isbn) VALUES
('해리포터와 마법사의 돌', 'J.K. 롤링', 1997, '1234567890123'),
('1984', '조지 오웰', 1949, '9876543210987');

INSERT INTO Members (name, email, join_date, gender) VALUES
('홍길동', 'hong@example.com', '2025-01-01', 'M'),
('김영희', 'younghee@example.com', '2025-02-15', 'F');

INSERT INTO Loans (book_id, member_id, loan_date, return_date, status) VALUES
(1, 1, '2025-09-01', NULL, '대출중'),
(2, 2, '2025-09-05', '2025-09-10', '반납');