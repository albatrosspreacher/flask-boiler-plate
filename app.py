from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    json_file = {}
    json_file['query'] = 'hello_world'
    return jsonify(json_file)

if __name__ == '__main__':
    app.run()