from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hola platzi masters'


if __name__ == '__main__':
    app.run()