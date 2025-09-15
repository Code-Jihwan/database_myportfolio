### 도서관 관리 시스템 _ 데이터베이스 프로젝트
#### - 책, 회원, 대출 관리 시스템
#### - MySQL로 데이터 모델링 및 쿼리 구현

### ER 다이어그램 작성
<img width="1465" height="502" alt="도서관리 ER 다이어그램 작성" src="https://github.com/user-attachments/assets/e43cf181-fa07-4721-8e56-20257ea446e3" />


schema.sql -> 데이터베이스 구축 완료

https://github.com/Code-Jihwan/database_myportfolio/blob/769b9b831b83a7ccf2793c5be0fe498778581fed/sql/schema.sql

***

### 데이터 구하기 Kaggle 데이터셋 활용하기
#### Goodreads-books Dataset
https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks

***

### Python 스크립트로 SQL 구문 생성
도서 정보 데이터가 담긴 CSV 파일을 MySQL에서 곧바로 실행할 수 있는 INSERT 문 묶음으로 변환

https://github.com/Code-Jihwan/database_myportfolio/blob/769b9b831b83a7ccf2793c5be0fe498778581fed/scripts/csv_to_sql.py

books.csv -> book_inserts.sql

***

### mylibary 데이터베이스 (Books, Members, Loans 테이블)
- Books Table : 도서 정보 입력 (book_inserts.sql 사용)
- Members Table : 회원 정보 입력 (5명 회원 수동 입력)
- Loans Table : 대출 정보 입력 (입력 예정)

***

추가) 파이썬 패키지 및 프로젝트 관리 -> UV 사용
블로그 포스팅 정리 (직접 작성) : https://velog.io/@nuguri/Python-UV-패키지-관리

***
