from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


books = [
    {
        'name': 'Things We Never Got Over',
        'details': [
            {
                'author': 'Lucky Score',
                'price': 15.9
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')


# http://127.0.0.1:5000/book
@app.route('/book', methods=['POST'])
def create_book():
    data = request.get_json()
    print(data)
    book = {
        'name': data['name'],
        'details': []
    }
    books.append(book)
    return jsonify(book)


# http://127.0.0.1:5000/book
@app.route('/book')
def get_books():
    return jsonify({'books': books})


# http://127.0.0.1:5000/book/Things We Never Got Over
@app.route('/book/<string:name>')
def get_book(name):
    for book in books:
        if book['name'] == name:
            return jsonify(book)
    return jsonify({'message': 'book not found!'})
# def get_book(name):
#     book = find_book(name)
#     if not book:
#         return jsonify({'message': 'book not found'})
#     return jsonify(book)


# http://127.0.0.1:5000/book/Things We Never Got Over/detail
@app.route('/book/<string:name>/detail', methods=['POST'])
def create_details_in_book(name):
    request_data = request.get_json()
    # request_data = {'name':'Django'}
    # request_data['name'] is to Django which is book name!
    for book in books:
        if book['name'] == name:
            new_detail = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            book['details'].append(new_detail)
            return jsonify(new_detail)
    return jsonify({'message': 'book not found!'})
# def create_book_detail(name):
#     book = find_book(name)
#     if not book:
#         return jsonify({'message': 'book not found'})
#     data = request.get_json()
#     book['details'].append({'name': data['name'], 'price': data['price']})
#     return jsonify(book)


# http://127.0.0.1:5000/book/Things We Never Got Over/detail
@app.route('/book/<string:name>/detail')
def get_book_details(name):
    for book in books:
        if book['name'] == name:
            return jsonify({'details': book['details']})
            # return jsonify(book['details'])
    return jsonify({'message': 'book not found!'})
# def get_book_details(name):
#     book = find_book(name)
#     if not book:
#         return jsonify({'message': 'book not found'})
#     return jsonify(book['details'])


# def find_book(name):
#     for book in books:
#         if book['name'] == name:
#             return book
#     return None


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
