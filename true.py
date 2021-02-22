@ approute('/getFirmware<gatewaySerial><firmwareversion><message><ipvalue><chunksize>')
def getFirmawareUpdate():    
    #data = connection.recv(16)
    server_address = ('192.168.1.6', 3000)
    gatewaySerial  = 'at-at23213123'
    firmwareversion = 3.14
    latest_firmware = 5.4
    # iF OLD firmware send the latest firmware 
    f = open('binfileName','rb')
    print >>sys.stderr, 'received "%s"' % data
    if (current_firmware<latest_firmware):
        print >>sys.stderr, 'sending data back to the client'
        data = f.read(8000)
        print >>sys.stderr, 'Sending this data', data
        connection.sendall(data)
        #connection.sendall(data)
    else:
        print >>sys.stderr, 'no more data from', client_address
        break