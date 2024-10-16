from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Event when a message is received
@socketio.on('message')
def handle_message(msg):
    print('Received message: ' + msg)
    response = 'Stay safe online!'
    send(response)

if __name__ == '__main__':
    socketio.run(app, port=5000)
