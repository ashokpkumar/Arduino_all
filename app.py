from flask import Flask
import socket
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    print "hello world"
    return 'Hello World!'

@app.route('/get_firmware_update/<gatewayserial>/<firmwareversion>/<message>')
def updatefirmware(gatewayserial,firmwareversion,message):
    print "Message type :>>>>>>>>>>>>>>",message
    print "gatewayserial :>>>>>>>", gatewayserial
    print "firmwareversion :********", firmwareversion

    latest_firmware_version = 1.5
    gateway_serial_op = "at-at212"
   
    if message =="firmwareupdate":  
        if gatewayserial ==gateway_serial_op:     
            if float(firmwareversion) < latest_firmware_version:
                print ">>>>>>>>>>>>>>>>>>Firmware found to be outdated. updating the firmware"    
                f = open('binfileName','rb')
                data = f.read()
                return data
            else:
                print ">>>>>>>>>>>>>>>>Firmware found to be Up to date. No action needed."
                return "Firmware found to be Up to date. No action needed.", 409
        else:
            print ">>>>>>>>>>>>>>>>>>Device not found in the list"
            return "Device not found ", 404
    else:
        print "Incorrect message type, no action available for this message type"
        return "No action available for this message type. Available message types are :" + "firmwareupdate", 404
    

if __name__ == '__main__':
    app.run(port = '3000', host = '0.0.0.0', debug = True)