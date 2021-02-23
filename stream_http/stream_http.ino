#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>

ESP8266WiFiMulti WiFiMulti;
//String host_port_name = "http://192.168.1.5:3000";
String host_port_name = "http://192.168.1.5:8080/devices";
//Endpoint Format
//String endpoint = "/get_firmware_update/<gatewayserialnumber>/<firmwareversion>/<message>";

String endpoint = "/get_firmware_update/at-at212/1.2/firmwareupdate"; //All pass
//String endpoint = "/get_firmware_update/unavailable/1.5/firmwareupdate"; //device is unavailable
//String endpoint = "/get_firmware_update/at-at212/1.5/firmwareupdate"; //device available firmware up to date
//String endpoint = "/get_firmware_update/at-at212/1.5/sample"; //Message type not found

void setup() {
  Serial.begin(115200);
  for (uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP("ASHOK 2.4G", "7639856885");
}

void loop() {
  if ((WiFiMulti.run() == WL_CONNECTED)) {
    WiFiClient client;
    HTTPClient http; 

    Serial.print( host_port_name + endpoint);
    http.begin(client, host_port_name + endpoint);
    int httpCode = http.GET();
    if (httpCode > 0) {
      Serial.printf("[HTTP] GET... code: %d\n", httpCode);
      if (httpCode == HTTP_CODE_OK) {
        int len = http.getSize();
        Serial.println("Size of the Binary File: ");
        Serial.println(len);
        uint8_t buff[16] = { 0 }; //Change the buffer size for device : buffer of 16 bytes now.

//Comment/Uncomment this line for HTTP streaming
//        Serial.println("HTTP Streaming");
//        Serial.println(http.getString());

//Comment/Uncomment this line for TCP streaming
       Serial.println("TCP Streaming");
      WiFiClient * stream = &client;
      while (http.connected() && (len > 0 || len == -1)) {
       int c = stream->readBytes(buff, std::min((size_t)len, sizeof(buff)));
    Serial.printf("readBytes: %d\n", c); //This messsage 
        if (!c) {
         Serial.println("read timeout");
      }
        Serial.write(buff, c); //Printing the data and the byte size: 
        if (len > 0) {
           len -= c;
        }
       }
        Serial.println();
        Serial.print("[HTTP] connection closed or file end.\n");
      }
    } else {
      Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
      
    }
    http.end();
  }
  else {
    Serial.println("Awaiting WIFI connection");
    delay(500);
  }
  delay(10000);
}
