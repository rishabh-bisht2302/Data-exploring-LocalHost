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
        d['id'] = row[0]
        d['published'] = row[1]
        d['author'] = row[2]
        d['title'] = row[3]
        d['first_sentence'] = row[4]
        l.append(d)
    return l