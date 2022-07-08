from flask import Flask


# print(__name__)#prints "__main__"
print(f'  {__name__} ')
app = Flask(__name__)


def make_bold(funkal):
    def wrapper():
        return f'<b>{funkal()}</b>'
    return wrapper


def make_italic(funkal):
    def wrapper():
        return f'<em>{funkal()}</em>'
    return wrapper


def make_underlined(funkal):
    def wrapper():
        return f'<u>{funkal()}</u>'
    return wrapper


@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def say_bye():
    return 'Bye!'


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/good_morning')
def say_good_morning():
    return 'Good Morning!😊'


@app.route('/good_morning/<name>/<int:number>/yay')
def say_personal_good_morning(name, number):
    return f'<h3 style="text-align: center;">Good Morning, there, {name}, you are {number} years old!</h3><h4 '\
           'style="text-align: center;">😊</h4><img width=200 src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.4LgTUpaikGz1bfQjuLMuTgHaEK%26pid%3DApi&f=1">' \
           '<br><br><img src="https://media2.giphy.com/media/vVcxJmqG7eoP6/200w.webp?cid=ecf05e472g9dvx0m2qd4sctfvpctyk97991r10dzs1pag4g9&rid=200w.webp&ct=g">'



if __name__ == "__main__":
    app.run(debug=True)
