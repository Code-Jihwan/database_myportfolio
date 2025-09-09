CREATE DATABASE mylibrary;
USE mylibrary;

CREATE TABLE Books (
	id INT auto_increment primary key,
    title varchar(255) NOT NULL,
    author varchar(50),
    publish_date DATE,
    isbn varchar(13) unique NOT NULL
);

CREATE TABLE Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    join_date DATE NOT NULL DEFAULT (CURDATE()), -- 가입일을 오늘 날짜로 자동 설정
    gender ENUM('M', 'F')
);

CREATE TABLE Loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE NOT NULL DEFAULT (CURDATE()), -- 대출일 지정 없으면 오늘 날짜로 자동 설정
    return_date DATE,
    -- Books 데이터가 삭제되면, 관련 대출 기록의 book_id를 NULL로 설정
    FOREIGN KEY (book_id) REFERENCES Books(id) ON DELETE SET NULL,
    -- Members 데이터가 삭제되면 관련 대출 기록도 함께 삭제
    FOREIGN KEY (member_id) REFERENCES Members(id) ON DELETE CASCADE
);


SET FOREIGN_KEY_CHECKS = 0; -- 외래 키 제약 조건 비활성화
TRUNCATE TABLE Books;
TRUNCATE TABLE Members;
TRUNCATE TABLE Loans;
SET FOREIGN_KEY_CHECKS = 1; -- 외래 키 제약 조건 다시 활성화


-- 대출을 하는 사람은 5명 수동 추가
INSERT INTO Members (name, email, gender) VALUES
('김철수', 'chulsoo.kim@example.com', 'M'),
('이영희', 'younghee.lee@example.com', 'F'),
('박지성', 'jisung.park@example.com', 'M'),
('김연아', 'yuna.kim@example.com', 'F'),
('손흥민', 'heungmin.son@example.com', 'M');
