How it Works:
>Works as Python based file as server and ESP8266 as Client
>Run the server.py from terminal
>Flash the wificlientbasic.ino to ESP8266

>Client first connect to the WIFI and then send a hello message to the Server and listens to the data from the same socket
>Server starts a server and listens to any message from Client in the IP and Port '192.168.1.3', 3000
>If message recevied, the Server displays the message from the client and then open a binary file and send it.
>The Client wait for the server to send a data and display the data in the Serial port
>Run the readSerial.py to read the serial data from esp8266
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Changes to be made to the file:
in Server.py:
1. change this to a available IP and Port. set it to max IP like 192.168.1.10 to avoid any conflict.
    server_address = ('192.168.1.3', 3000) 

2. Add more logic to include buffer of 1024 bytes to send data in bursts.
    data = f.read()


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In the Arduino INO:
1. Line 12 & 13-Change the SSID and Password of the wifi Access point.
    #define STASSID "ASHOK 2.4G"
    #define STAPSK  "7639856885"

2. Line 18 & 19 - change this to the IP and port we set in the Server.
    const char* host = "192.168.1.3";
    const uint16_t port = 3000;

3. Line 24 - Set the Baud rate supported by the device.
     Serial.begin(115200);

4. Line 65 - Change this to the endpoint you want to call instead of just sending a message.
    client.println("hello from ESP8266");

5. Line 69 - Change this to the Supported seperation used in the acutual binary file to avoid any truncation.
    String line = client.readStringUntil('\r');

6. Line 73 - Remove this line if you experience any error as unexpected connection closure
    client.stop();

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
References:
https://stackoverflow.com/questions/27241804/sending-a-file-over-tcp-sockets-in-python
https://stackoverflow.com/questions/45974344/save-txt-file-as-binary-in-python
https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
https://www.arduino.cc/en/Reference/ClientConnect
https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266WiFi/examples/WiFiClientBasic/WiFiClientBasic.ino
Connect as client and GET request>> https://arduino-esp8266.readthedocs.io/en/2.5.0/esp8266wifi/client-examples.html

https://circuits4you.com/2018/11/26/esp8266-nodemcu-tcp-socket-server-arduino-example/
https://stackoverflow.com/questions/61483877/flask-socketio-arduino-esp
https://www.instructables.com/ESP8266-WiFi-File-Management/
https://pymotw.com/2/socket/tcp.html


