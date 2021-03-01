from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello world</h1>'

if __name__ == '__main__':
    app.run()