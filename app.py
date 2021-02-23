from flask import Flask
import socket
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    print "hello world"
    return 'Hello World!'

@app.route('/get_firmware_update/<gatewayserial>/<firmwareversion><message>')
def updatefirmware(gatewayserial,firmwareversion,message):
    print "Message type :>>>>>>>>>>>>>>",message
    if message =="firmwareupdate":    
        f = open('binfileName','rb')
        data = f.read()
        print ">>>>>>>>>>>>>>>>>>>", gatewayserial
        print "*******************", firmwareversion
        return data
    else:
        return "No action available for this message type. Available message types are :" + "firmwareupdate"
    

if __name__ == '__main__':
    app.run(port = '3000', host = '0.0.0.0', debug = True)