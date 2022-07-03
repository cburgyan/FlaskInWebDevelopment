from flask import Flask


# print(__name__)#prints "__main__"
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'