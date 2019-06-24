from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "WELCOME TO BOOKS EXPLORING WORLD"

@app.route('/v1/resource/all',methods=['GET'])
def all():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    result = cur.execute('SELECT * FROM books;').fetchall()
    res_dict = dict_factory(result)
    return jsonify(res_dict)

def dict_factory(list_of_tuple):
    lst= []
    for book in list_of_tuple:
        d = {}
        d['id'] = book[0]
        d['published'] = book[1]
        d['author'] = book[2]
        d['title'] = book[3]
        d['first_sentence'] = book[4]
        lst.append(d)
    return lst

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
    
@app.route('/v1/resource',methods=['GET'])
def specific_data():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')
    title = query_parameters.get('title')
    query = 'SELECT * FROM books WHERE'
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    filter_by = []
    if 'published' in request.args:
        query += 'published=? AND'
        filter_by.append(published)
    elif 'author' in request.args:
        query += 'author=? AND'
        filter_by.append(author)
    elif 'title' in request.args:
        query += 'title=? AND'
        filter_by.append(title)
    elif 'id' in request.args:
        query += 'id=? AND'
        filter_by.append(id)
    else:
        return 'Error...Result not found'
    query = query[:-4] + ';'
    result = cur.execute(query,filter_by).fetchall()
    res_dict = dict_factory(result)
    return jsonify(res_dict)

app.run(debug=True)
