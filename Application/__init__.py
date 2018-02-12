from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Attempt'

if __name__ == '__main__':
        app.run()
