from flask import Flask
import socket

ip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host=ip, port=8080)