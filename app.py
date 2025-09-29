from flask import Flask, render_template, request, redirect, url_for
from database import get_all_books, get_book_by_isbn, get_book_by_title, add_book

app = Flask(__name__) # Flask 앱 생성

'''라우트 설정'''

# 홈 페이지 (도서 목록 읽기)
@app.route('/', methods=['GET']) # 기본 홈화면
def index():
    return render_template('index.html') # 기본 홈화면 템플릿 렌더링


@app.route('/analysis') # 데이터 분석 페이지
def data_analysis():
    return render_template('analysis.html')


@app.route('/create', methods = ['GET', 'POST']) # 도서 추가 페이지
def create():
    if request.method == 'POST':
        # 폼에서 입력한 도서 정보를 가져옵니다.
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        publish_date = request.form['publish_date']
        
        # 2. database.py의 add_book 함수를 호출해서 DB에 저장합니다.
        add_book(title, author, publish_date, isbn)

        # 3. 책 추가 후, 전체 목록 페이지로 이동(redirect)시킵니다.
        return redirect(url_for('read'))
    
    return render_template('create.html')



@app.route('/read') # 도서 조회 페이지
def read(): 
    # 1. URL에서 'isbn' 검색어를 가져옵니다. 없으면 None이 됩니다.
    search_isbn = request.args.get('isbn')  # 쿼리 파라미터에서 isbn 값 가져오기
    search_title = request.args.get('title') 
    books_to_display = []
    
    if search_isbn:
        # 1. ISBN 검색어가 있으면 ISBN으로만 검색합니다.
        book = get_book_by_isbn(search_isbn)
        if book:
            books_to_display = [book] # 템플릿 for문을 위해 리스트에 담아줍니다.
            
    elif search_title:
        # 2. ISBN 검색어가 없고, 제목 검색어만 있으면 제목으로 검색합니다.
        books_to_display = get_book_by_title(search_title)
        
    else:
        # 3. 아무 검색어도 없으면 모든 책을 보여줍니다.
        books_to_display = get_all_books()
    
    return render_template('read.html', books=books_to_display)  # 도서 목록을 템플릿에 전달


@app.route('/update') # 도서 수정 페이지
def update():
    return render_template('update.html')


@app.route('/delete') # 도서 삭제 페이지
def delete():
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)

