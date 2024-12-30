from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for books
books = []

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books}), 200

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify({"book": book}), 200
    return jsonify({"error": "Book not found"}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({"error": "Invalid input"}), 400
    book = {
        "id": len(books) + 1,
        "title": data['title'],
        "author": data['author']
    }
    books.append(book)
    return jsonify({"message": "Book created", "book": book}), 201

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    if 'title' in data:
        book['title'] = data['title']
    if 'author' in data:
        book['author'] = data['author']
    return jsonify({"message": "Book updated", "book": book}), 200

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
