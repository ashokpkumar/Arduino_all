from flask import Flask
import socket
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    print "hello world"
    return 'Hello World!'

@app.route('/get_firmware_update/<gatewayserial>/<firmwareversion>')
def updatefirmware(gatewayserial,firmwareversion):
    f = open('binfileName','rb')
    data = f.read(8000)
    print ">>>>>>>>>>>>>>>>>>>", gatewayserial
    print "*******************", firmwareversion
    return data
    

if __name__ == '__main__':
    app.run(port = '3000', host = '0.0.0.0', debug = True)