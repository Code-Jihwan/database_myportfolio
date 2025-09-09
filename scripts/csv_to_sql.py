import csv
from datetime import datetime

def csv_to_sql(csv_file_path, sql_path, table_name):
    """
    데이터가 들어있는 csv 파일을 읽어서 sql insert 문으로 변환하는 함수

    Args:
        csv_file_path (str): 가져와서 읽을 CSV 파일 경로
        sql_path (str): 저장할 SQL 파일 경로
        table_name (str): INSERT 할 테이블 이름
    """
    
    with open(csv_file_path, mode='r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        with open(sql_path, mode='w', encoding='utf-8') as sqlfile:
            
            # DB 테이블의 컬럼 이름을 정의
            db_columns = ["title", "author", "publish_date", "isbn"]
            # 정의한 컬럼 이름으로 INSERT INTO 부분 작성
            columns_sql = ', '.join(db_columns)
            
            print("SQL 변환 시작...")
            count = 0
            
            for row in reader:
                try:
                    isbn = row.get('isbn13')
                    if not isbn:
                        continue
                    
                    title = row.get('title', 'No Title').replace("'", "''")
                    author = row.get('authors', 'No author').replace("'", "''")
                    
                    # publication_date에서 날짜 추출 로직 수정
                    pub_date_str = row.get('publication_date', '')
                    publish_date = 'NULL' # 기본값은 NULL
                    if pub_date_str:
                        try:
                            date_obj = datetime.strptime(pub_date_str, '%m/%d/%Y')
                            # datetime 객체를 SQL에 맞는 'YYYY-MM-DD' 문자열로 변환
                            publish_date = f"'{date_obj.strftime('%Y-%m-%d')}'"
                        except ValueError:
                            publish_date = 'NULL'
                
                    # 추출한 값들을 순서에 맞게 VALUES 부분으로 작성
                    values_sql = f"'{title}', '{author}', {publish_date}, '{isbn}'"
                    # 최종 SQL 명령어 작성
                    sql_command = f"INSERT IGNORE INTO {table_name} ({columns_sql}) VALUES ({values_sql});\n"
                    sqlfile.write(sql_command)
                    count += 1
                except Exception as e:
                    print(f"처리 중 오류 발생 -> skip: {row} -> {e}")
                    continue
                    
    print(f"총 {count}개의 레코드가 SQL 파일로 변환되어 저장되었습니다: {sql_path}")

csv_to_sql('books.csv', 'book_inserts.sql', 'Books')