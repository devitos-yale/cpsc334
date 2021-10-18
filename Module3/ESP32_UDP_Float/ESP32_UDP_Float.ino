/*
 *  This sketch sends random data over UDP on a ESP32 device
 *
 */
#include "WiFi.h"
#include "WiFiUdp.h"

// WiFi network name and password:
const char * networkName = "yale wireless";
const char * networkPswd = "";

//IP address to send UDP data to:
// either use the ip address of the server or 
// a network broadcast address
const char * udpAddress = "172.29.17.214";
const int udpPort = 8092;

//Are we currently connected?
boolean connected = false;

//The udp library class
WiFiUDP udp;

byte command[27] = {0x20, 0x00, 0x00, 0x00, 0x16, 0x02, 0x62, 0x3A, 0xD5, 0xED, 0xA3, 0x01, 0xAE, 0x08, 0x2D, 0x46, 0x61, 0x41, 0xA7, 0xF6, 0xDC, 0xAF, 0xD3, 0xE6, 0x00, 0x00, 0x1E};

void setup(){
  // Initilize hardware serial:
  Serial.begin(115200);

  //Connect to the WiFi network
  connectToWiFi(networkName, networkPswd);
}

void loop(){
  //int values = random(0, 100); // GENERATE TEST FLOAT or
  //int values = hallRead();
  
  int piezoValue = analogRead(34); //Piezo sensor
  String msg1 = String(piezoValue); // CONVERT FLOAT TO STRING

  int buttonValue = digitalRead(9); //button
  String msg2 = String(buttonValue); // CONVERT FLOAT TO STRING
  
  //only send data when connected
  if(connected){
    //Send a packet
    udp.beginPacket(udpAddress,udpPort);
    udp.print(msg1);  // USES .print INSTEAD OF .write
    udp.endPacket();

    udp.beginPacket(udpAddress,udpPort);
    udp.print(msg2);  // USES .print INSTEAD OF .write
    udp.endPacket();
  }
  //Wait for 1 second
  delay(10);
}

void connectToWiFi(const char * ssid, const char * pwd){
  Serial.println("Connecting to WiFi network: " + String(ssid));

  // delete old config
  WiFi.disconnect(true);
  //register event handler
  WiFi.onEvent(WiFiEvent);

  //Initiate connection
  WiFi.begin(ssid, pwd);

  Serial.println("Waiting for WIFI connection...");
}

//wifi event handler
void WiFiEvent(WiFiEvent_t event){
    switch(event) {
      case SYSTEM_EVENT_STA_GOT_IP:
          //When connected set 
          Serial.print("WiFi connected! IP address: ");
          Serial.println(WiFi.localIP());  
          //initializes the UDP state
          //This initializes the transfer buffer
          udp.begin(WiFi.localIP(),udpPort);
          connected = true;
          break;
      case SYSTEM_EVENT_STA_DISCONNECTED:
          Serial.println("WiFi lost connection");
          connected = false;
          break;
    }
}
