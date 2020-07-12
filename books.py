from flask import Flask, jsonify
from booksdata import books
app= Flask(__name__)



@app.route('/books')
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:isbn>')
def get_books_by_isbn(isbn):
    return_value={}
    for book in books:
        if book["isbn"]==isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)

app.run(port=5000)