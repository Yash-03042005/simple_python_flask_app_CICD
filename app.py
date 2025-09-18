from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world from  devops ki duniya'

if __name__ == '__main__':
    app.run() 
