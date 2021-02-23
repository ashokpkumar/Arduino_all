from flask import Flask
import socket
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/get_firmware_update/<gatewayserial>/<firmwareversion>')
def updatefirmware(gatewayserial,firmwareversion):
    f = open('binfileName','rb')
    message = "hello moto"
    print "file opened"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.1.4', 3000)
    print "port opened"
    sock.connect(server_address)
    print "Connection happening between the server"
    data = f.read(8000)
    sock.sendall(data)
    print "Message sent"
    sock.close()
    print "Socket closed"
    '''
    sock.bind(server_address)
    print "Socket binded"
    sock.listen(1)
    print "Listening"
    connection, client_address = sock.accept()
    print "Accepted",connection,client_address
    data = connection.recv(16)
    data = f.read(8000)
    connection.sendall(data)
    '''
    return data
    

if __name__ == '__main__':
    app.run(port = '3000', host = '0.0.0.0', debug = True)