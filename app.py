from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL 연결
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='a9503!@#',  # 네가 설정한 비밀번호
    database='mylibrary'
)

# 홈 페이지 (도서 목록 읽기)
@app.route('/', methods=['GET'])
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    cursor.close()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)