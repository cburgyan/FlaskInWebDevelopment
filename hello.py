from flask import Flask


# print(__name__)#prints "__main__"
print(f'  {__name__} ')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()