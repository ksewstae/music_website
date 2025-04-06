from flask import Flask


app = Flask(__name__)


@app.route('/')
def main_screen():
    return 'Сайт с музыкой'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')