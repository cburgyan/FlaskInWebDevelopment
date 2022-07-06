from flask import Flask


# print(__name__)#prints "__main__"
print(f'  {__name__} ')
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/good_morning')
def say_good_morning():
    return 'Good Morning!😊'


if __name__ == "__main__":
    app.run()
