from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=2020, host='127.0.0.1', debug=True)
