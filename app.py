from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return "home page" 

if __name__ == '__main__':
    app.run(debug=True)
