#include <SPI.h>
#include <Ethernet.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_MPU6050.h>

// Ethernet settings
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 178);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);
EthernetServer server(80);

void setup() {
  // Initialize the Ethernet device
  Ethernet.begin(mac, ip, gateway, subnet);
  server.begin();
  
  // Start serial communication for debugging purposes
  Serial.begin(9600);
  Serial.println("Server is at ");
  Serial.println(Ethernet.localIP());
}

void loop() {
  // Listen for incoming clients
  EthernetClient client = server.available();
  if (client) {
    Serial.println("Client connected");

    // Wait until the client sends some data
    while (client.connected() && !client.available()) {
      delay(1);
    }

    // Read the request from the client
    String request = client.readStringUntil('\n');
    Serial.println("Request received: " + request);

    // Simulated sensor data
    float pressure = 10133.25; // hPa
    float temperature = 25.0; // °C
    float accel_x = 0.0;
    float accel_y = 0.0;
    float accel_z = 0.0;
    float gyro_x = 0.0;
    float gyro_y = 0.0;
    float gyro_z = 0.0;

    // Create the response string
    String response = "pressure: " + String(pressure) + " hPa, "
                    + "temperature: " + String(temperature) + " C, "
                    + "acceleration: " + String(accel_x) + "," + String(accel_y) + "," + String(accel_z) + ", "
                    + "gyroscope: " + String(gyro_x) + "," + String(gyro_y) + "," + String(gyro_z);

    // Send the response to the client
    client.println(response);
    Serial.println("Response sent: " + response);

    // Close the connection
    client.stop();
    Serial.println("Client disconnected");
  }
}
