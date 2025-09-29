### 도서관 관리 시스템 _ 데이터베이스 프로젝트
#### - 책, 회원, 대출 관리 시스템
#### - 도서 정보 관리를 위한 기본적인 C(생성) / R(조회) / U(수정) / D(삭제) 기능 구현 완료
#### - MySQL로 데이터 모델링 및 쿼리 구현

***

### ER 다이어그램 작성
<img width="1465" height="502" alt="도서관리 ER 다이어그램 작성" src="https://github.com/user-attachments/assets/e43cf181-fa07-4721-8e56-20257ea446e3" />


schema.sql -> 데이터베이스 구축 완료

https://github.com/Code-Jihwan/database_myportfolio/blob/769b9b831b83a7ccf2793c5be0fe498778581fed/sql/schema.sql

***
### 도서 정보 관리 : C(생성) / R(조회) / U(수정) / D(삭제) 기능의 웹 사이트 구현

Main (Home 화면)
<img width="1512" height="982" alt="스크린샷 2025-09-29 오후 1 19 08" src="https://github.com/user-attachments/assets/989fcaea-929e-41c9-92c0-b76f73af71d4" />
***

Create (도서 추가)
<img width="1512" height="982" alt="스크린샷 2025-09-29 오후 1 19 43" src="https://github.com/user-attachments/assets/18dd09d9-72a0-4f95-a034-e40b168970a0" />
***

Read(도서 조회)
<img width="1512" height="982" alt="스크린샷 2025-09-29 오후 1 19 50" src="https://github.com/user-attachments/assets/88f9bbd9-38a9-400c-85e6-b8a0faa3e951" />

<img width="1512" height="982" alt="스크린샷 2025-09-29 오후 1 20 06" src="https://github.com/user-attachments/assets/36facfd4-8b60-43c5-aeab-2f59072a0013" />

***
Update(도서 수정)
<img width="1512" height="982" alt="스크린샷 2025-09-29 오후 1 20 34" src="https://github.com/user-attachments/assets/01ac35df-e859-4f94-80f4-312ceacb7e5d" />
<img width="1512" height="982" alt="스크린샷 2025-09-29 오후 1 20 41" src="https://github.com/user-attachments/assets/db2ff28c-e608-4153-a10f-904a9f2137c1" />

***

Delete(도서 삭제)
<img width="1512" height="982" alt="스크린샷 2025-09-29 오후 1 20 56" src="https://github.com/user-attachments/assets/6ddb6df3-9ce3-4f57-b328-379ddc5b1d89" />
<img width="1512" height="982" alt="스크린샷 2025-09-29 오후 2 33 23" src="https://github.com/user-attachments/assets/01ac9968-e60d-452f-8ee1-8178d05dfba5" />

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

#### 추가) 파이썬 패키지 및 프로젝트 관리 -> UV 사용

블로그 포스팅 정리 (직접 작성) : https://velog.io/@nuguri/Python-UV-패키지-관리

***


***



