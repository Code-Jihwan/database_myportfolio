import mysql.connector

# DB 접속 정보를 딕셔너리(설계도)로 변경합니다.
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'a9503!@#',  # 본인의 비밀번호
    'database': 'mylibrary'
}

# 조회 기능
def get_all_books():
    """모든 책 목록을 데이터베이스에서 가져오는 함수"""
    conn = None  # finally 블록에서 사용하기 위해 미리 변수 선언
    cursor = None
    try:
        # **db_config 로 딕셔너리를 풀어 인자로 전달합니다.
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM Books ORDER BY id DESC"
        cursor.execute(query)
        books = cursor.fetchall()
        
        return books
        
    except mysql.connector.Error as err:
        print(f"데이터베이스 오류: {err}")
        return [] # 오류 발생 시 빈 리스트 반환
    finally:
        # return books 아래에 있던 코드는 실행되지 않으므로,
        # finally 블록으로 옮겨서 항상 실행되도록 합니다.
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


# 조회 기능
def get_book_by_isbn(book_isbn):
    """ISBN으로 책 한 권을 데이터베이스에서 가져오는 함수"""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM Books WHERE isbn = %s"
        cursor.execute(query, (book_isbn,))
        book = cursor.fetchone()
        
        return book

    except mysql.connector.Error as err:
        print(f"데이터베이스 오류: {err}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()
            
            
# 조회 기능
def get_book_by_title(book_title):
    """title으로 책 한 권을 데이터베이스에서 가져오는 함수"""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM Books WHERE title like %s"
        
        search_pattern = f"%{book_title}%"
        
        cursor.execute(query, (search_pattern,))
        book = cursor.fetchall()
        
        return book

    except mysql.connector.Error as err:
        print(f"데이터베이스 오류: {err}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()            


# 추가 기능
def add_book(title, author, publish_date, isbn):
    """새 책을 데이터베이스에 추가하는 함수"""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        query = "INSERT INTO Books (title, author, publish_date, isbn) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (title, author, publish_date, isbn))
        conn.commit()
        
        return cursor.lastrowid  # 추가된 책의 ID 반환

    except mysql.connector.Error as err:
        print(f"데이터베이스 오류: {err}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()  
            
            
# 삭제 기능
def del_book_by_isbn(book_isbn):
    """ISBN으로 책 한 권을 데이터베이스에서 삭제하는 함수"""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        query = "Delete from books where isbn = %s"
        cursor.execute(query, (book_isbn,))
        conn.commit() 

    except mysql.connector.Error as err:
        print(f"데이터베이스 오류: {err}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


# 삭제 기능
def del_book_by_title(book_title):
    """Title로 책 한 권을 데이터베이스에서 삭제하는 함수"""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        query = "Delete from books where title = %s"
        cursor.execute(query, (book_title,))
        conn.commit() 

    except mysql.connector.Error as err:
        print(f"데이터베이스 오류: {err}")
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


