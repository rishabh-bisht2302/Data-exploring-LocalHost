from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "WELCOME TO BOOKS EXPLORING WORLD"

