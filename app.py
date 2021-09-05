from flask import Flask
from flask import jsonify 
import os

app = Flask(__name__)

@app.route("/")
def hai():
    return jsonify({"Author":{"Name":"Arun Bang","Registration No":"19BBS0006"}})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
