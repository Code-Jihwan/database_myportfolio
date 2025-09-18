from flask import Flask, render_template
import mysql.connector

app = Flask(__name__) # Flask 앱 생성

# MySQL 연결 - DB 접속 정보
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='a9503!@#',  # 네가 설정한 비밀번호
    database='mylibrary'
)

'''라우트 설정'''

# 홈 페이지 (도서 목록 읽기)
@app.route('/', methods=['GET']) # 기본 홈화면
def index():
    cursor = db.cursor(dictionary=True) # 커서 생성
    
    cursor.execute("SELECT * FROM Books limit 10;") # SQL 쿼리 실행문
    books = cursor.fetchall() # 모든 결과 가져오기
    
    cursor.close()  # 커서 닫기
    return render_template('index.html', books=books) # 기본 홈화면 템플릿 렌더링


@app.route('/analysis') # 데이터 분석 페이지
def data_analysis():
    return render_template('analysis.html')

@app.route('/create') # 도서 추가 페이지
def create():
    return render_template('create.html')

@app.route('/read') # 도서 조회 페이지
def read():
    return render_template('read.html')

@app.route('/update') # 도서 수정 페이지
def update():
    return render_template('update.html')

@app.route('/delete') # 도서 삭제 페이지
def delete():
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)

