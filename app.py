from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/app')
def blog():
    return "Hello, from Flask App!"



if __name__ == '__main__':
    app.run(threaded=True,port=8081)
