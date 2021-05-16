from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_static():
    return render_template('index.html') #add your file here

if __name__ == '__main__':
    app.run()