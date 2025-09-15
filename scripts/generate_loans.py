import mysql.connector
import random
from datetime import datetime, timedelta

def generate_random_loans(db_config, num_loans=100):
    """Loans 테이블 데이터 입력을 위한 데이터베이스에 무작위 대출 기록을 생성."""
    
    try:
        # 데이터베이스 연결
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor() # cursor는 데이터베이스에 SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
        
        # 모든 책 ID와 회원 ID를 가져오기
        cursor.execute("SELECT id FROM Books")
        book_ids = [item[0] for item in cursor.fetchall()]
        
        cursor.execute("SELECT id FROM Members")
        member_ids = [item[0] for item in cursor.fetchall()]
        
        print(f"{num_loans}개의 무작위 대출 기록 생성 시작...")
        
        for _ in range(num_loans):
            # 무작위로 책 ID와 회원 ID 선택
            random_book_id = random.choice(book_ids)
            random_member_id = random.choice(member_ids)
            
            # 무작위 대출 날짜 생성 (최근 1년 이내)
            days_ago = random.randint(1, 365)
            loan_date = datetime.now() - timedelta(days=days_ago)
            
            # 70% 확률로 반납 처리 (반납일은 대출일로부터 1~14일 사이)
            if random.random() < 0.7:
                return_days = random.randint(1, 14)
                return_date = loan_date + timedelta(days=return_days)
                return_date_sql = f"'{return_date.strftime('%Y-%m-%d')}'"
            else:
                return_date_sql = "NULL" # 미반납
            
            # INSERT 쿼리 실행
            query = f"INSERT INTO Loans (book_id, member_id, loan_date, return_date) VALUES ({random_book_id}, {random_member_id}, '{loan_date.strftime('%Y-%m-%d')}', {return_date_sql})"
            cursor.execute(query)

        db.commit() # 모든 변경사항을 데이터베이스에 최종 저장
        print("대출 기록 생성이 완료되었습니다!")

    except mysql.connector.Error as err:
        print(f"데이터베이스 에러: {err}")
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()
            print("데이터베이스 연결이 종료되었습니다.")


# 실행 스크립트
if __name__ == "__main__":
    db_connection_config = {
        'host': 'localhost',
        'user': 'root', # 이름
        'password': 'a9503!@#',
        'database': 'mylibrary'
    }
    generate_random_loans(db_connection_config, num_loans=100)