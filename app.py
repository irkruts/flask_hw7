from flask import Flask

app = Flask('My site')

@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run()
