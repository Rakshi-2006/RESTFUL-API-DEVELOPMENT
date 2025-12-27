from flask import Flask, jsonify, request

app = Flask(__name__)

books = []
book_id = 1

@app.route('/')
def home():
    return "Library API is running"

@app.route('/books', methods=['POST'])
def add_book():
    global book_id
    data = request.json
    book = {
        "id": book_id,
        "title": data['title'],
        "author": data['author'],
        "year": data['year']
    }
    books.append(book)
    book_id += 1
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    for book in books:
        if book['id'] == id:
            book['title'] = data['title']
            book['author'] = data['author']
            book['year'] = data['year']
            return jsonify({"message": "Book updated successfully"})
    return jsonify({"message": "Book not found"}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({"message": "Book deleted successfully"})
    return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=False)
