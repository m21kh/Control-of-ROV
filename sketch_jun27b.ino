#include <SPI.h>
#include <Ethernet.h>
#include <Servo.h>
int Speed = 0;
const int arraySize = 21; // Define the size of the array to include speeds from 0 to 20
String storedTexts[arraySize] = {"speed 0", "speed 1", "speed 2", "speed 3", "speed 4", 
                                 "speed 5", "speed 6", "speed 7", "speed 8", "speed 9",
                                 "speed 10", "speed 11", "speed 12", "speed 13", "speed 14",
                                 "speed 15", "speed 16", "speed 17", "speed 18", "speed 19",
                                 "speed 20"};
char previousState[20] = "";
char currentState[20] = "hello";

// Pin for motor move forward
#define MOTOR_FORWARD_1 6
#define MOTOR_FORWARD_2 7
#define MOTOR_FORWARD_3 8
#define MOTOR_FORWARD_4 9


// Pin for motor move backward

#define MOTOR_BACKWARD_1 2
#define MOTOR_BACKWARD_2 3
#define MOTOR_BACKWARD_3 4
#define MOTOR_BACKWARD_4 5



// Pin for motor rig

#define LIGHT_RELAY 49
#define CAMERA_RELAY 47
#define ARM1_RELAY 43
#define ARM2_RELAY 45
#define MOTION_REVERSE_RELAY 41




// pin for reverse motor


#define MOTOR_UP 11
#define MOTOR_DOWN 12

// class for motor forward

Servo MotorForward1,MotorForward2,MotorForward3,MotorForward4; 
//class for motor backword
Servo MotorBackward1,MotorBackward2,MotorBackward3,MotorBackward4; 
//class for motor up and down
Servo MotorUp,MotorDown;


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// MAC address and IP address of the Arduino
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 177);
IPAddress subnet(255, 255, 255, 0);

EthernetServer server(12345);

const int maxDataLength = 100; // Adjust the size based on your needs
char receivedData[maxDataLength];
int dataLength = 0;
String Light_Value_ON = "direction forward";
String Light_Value_OFF = "Light OFF";
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








// Function to activate LIGHT_RELAY
void activateLightRelay() {
  digitalWrite(LIGHT_RELAY, LOW);
}

// Function to deactivate LIGHT_RELAY
void deactivateLightRelay() {
  digitalWrite(LIGHT_RELAY, HIGH);
}

// Function to activate CAMERA_RELAY
void activateCameraRelay() {
  digitalWrite(CAMERA_RELAY, LOW);
}

// Function to deactivate CAMERA_RELAY
void deactivateCameraRelay() {
  digitalWrite(CAMERA_RELAY, HIGH);
}

// Function to activate ARM1_RELAY
void activateArm1Relay() {
  digitalWrite(ARM1_RELAY, LOW);
}

// Function to deactivate ARM1_RELAY
void deactivateArm1Relay() {
  digitalWrite(ARM1_RELAY, HIGH);
}

// Function to activate ARM2_RELAY
void activateArm2Relay() {
  digitalWrite(ARM2_RELAY, LOW);
}

// Function to deactivate ARM2_RELAY
void deactivateArm2Relay() {
  digitalWrite(ARM2_RELAY, HIGH);
}

// Function to activate MOTION_REVERSE_RELAY
void activateMotionReverseRelay() {
  digitalWrite(MOTION_REVERSE_RELAY, LOW);
}

// Function to deactivate MOTION_REVERSE_RELAY
void deactivateMotionReverseRelay() {
  digitalWrite(MOTION_REVERSE_RELAY, HIGH);
}




// for move forward
void moveMotorsForward(int speed) {
  int pulseWidth = map(speed, 0, 20, 1000, 2000); // Map speed to pulse width range (1000 to 2000)

  // Set the position of each motor
  MotorForward1.writeMicroseconds(pulseWidth);
  MotorForward2.writeMicroseconds(pulseWidth);
  MotorForward3.writeMicroseconds(pulseWidth);
  MotorForward4.writeMicroseconds(pulseWidth);
}




// for backword


void moveMotorsBackward(int speed) {
  int pulseWidth = map(speed, 0, 20, 1000, 2000); // Map speed to pulse width range (1000 to 2000)

  // Set the position of each backward motor
  MotorBackward1.writeMicroseconds(pulseWidth);
  MotorBackward2.writeMicroseconds(pulseWidth);
  MotorBackward3.writeMicroseconds(pulseWidth);
  MotorBackward4.writeMicroseconds(pulseWidth);
}


// for move up
void moveMotorsUp(int speed) {

   deactivateMotionReverseRelay();
   delay(100);
  int pulseWidth = map(speed, 0, 20, 1000, 2000); // Map speed to pulse width range (1000 to 2000)
  // Set the position of each up motor
  MotorUp.writeMicroseconds(pulseWidth);
  MotorDown.writeMicroseconds(pulseWidth);

 
}


void moveMotorsDown(int speed) {
  activateMotionReverseRelay();
  delay(100);
  int pulseWidth = map(speed, 0, 20, 1000, 2000); // Map speed to pulse width range (1000 to 2000)
  // Set the position of each up motor
  MotorUp.writeMicroseconds(pulseWidth);
  MotorDown.writeMicroseconds(pulseWidth);

 
}


void moveMotorsLeft(int speed) {
  int pulseWidth = map(speed, 0, 20, 1000, 2000); // Map speed to pulse width range (1000 to 2000)

  // Set the position of each backward motor
  MotorBackward1.writeMicroseconds(pulseWidth);
  MotorBackward2.writeMicroseconds(pulseWidth);
  MotorForward3.writeMicroseconds(pulseWidth);
  MotorForward4.writeMicroseconds(pulseWidth);
}



void moveMotorsRight(int speed) {
  int pulseWidth = map(speed, 0, 20, 1000, 2000); // Map speed to pulse width range (1000 to 2000)

  // Set the position of each backward motor
  MotorBackward3.writeMicroseconds(pulseWidth);
  MotorBackward4.writeMicroseconds(pulseWidth);
  MotorForward1.writeMicroseconds(pulseWidth);
  MotorForward2.writeMicroseconds(pulseWidth);
}
void BreakMotor()
{
  moveMotorsForward(0);
  delay(100);
  moveMotorsBackward(0);
    delay(100);

  MotorUp.writeMicroseconds(1000);
  delay(100);
  MotorDown.writeMicroseconds(1000);
  delay(100);

}


bool isSpeedFound(String text, String arr[], int size) {
  for (int i = 0; i < size; i++) {
    if (arr[i] == text) {
      Speed = text.substring(6).toInt(); // Extract and store the number after "speed "
      return true;
    }
  }
  return false;
}
////////////////////////////////////////////////////////////////////////////////


void setup() {


  // Relay define  output
  
    pinMode(LIGHT_RELAY,OUTPUT);
    pinMode(CAMERA_RELAY ,OUTPUT);
    pinMode(ARM1_RELAY ,OUTPUT);
    pinMode(ARM2_RELAY,OUTPUT);
    pinMode(MOTION_REVERSE_RELAY,OUTPUT);


    digitalWrite(LIGHT_RELAY,HIGH);
    digitalWrite(CAMERA_RELAY ,HIGH);
    digitalWrite(ARM1_RELAY ,HIGH);
    digitalWrite(ARM2_RELAY,HIGH);
    digitalWrite(MOTION_REVERSE_RELAY,HIGH);

    //Motor inistialize
    MotorForward1.attach(MOTOR_FORWARD_1);
    MotorForward2.attach(MOTOR_FORWARD_2);
    MotorForward3.attach(MOTOR_FORWARD_3);
    MotorForward4.attach(MOTOR_FORWARD_4);
    
    MotorBackward1.attach(MOTOR_BACKWARD_1);
    MotorBackward2.attach(MOTOR_BACKWARD_2);
    MotorBackward3.attach(MOTOR_BACKWARD_3);
    MotorBackward4.attach(MOTOR_BACKWARD_4);
    
    MotorUp.attach(MOTOR_UP);
    MotorDown.attach(MOTOR_DOWN);
    BreakMotor();
  // Initialize the Ethernet shield with a static IP
  Ethernet.begin(mac, ip, subnet);
  Serial.print("Server is at ");
  server.begin();
  Serial.print("Server is at ");
  Serial.println(Ethernet.localIP());

  

  Serial.begin(9600);

}


void loop() {
  int toggle = 0;
    // Check for incoming clients
  EthernetClient client = server.available();
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (dataLength < maxDataLength - 1) { // Ensure we don't overflow the array
          receivedData[dataLength++] = c;
          receivedData[dataLength] = '\0'; // Null-terminate the string
        }
      }
    }
    Serial.print("Receive Data : ");
    Serial.println(receivedData);

 
    if (isSpeedFound(receivedData, storedTexts, arraySize)) {
      Serial.print("Speed = ");
      Serial.println(Speed);
      
    } else {
      
    }
  
  delay(100); // Small delay to avoid overwhelming the serial communication


    // Check if received data matches the compareValue
    if (strcmp(receivedData,"Light ON") == 0)
      {
        
          activateLightRelay();
          
        // Perform actions when data matches
      }
    else  if (strcmp(receivedData,"Light OFF") == 0)
      {
       
           deactivateLightRelay();
         
          // Perform actions when data matches
        }

     else  if (strcmp(receivedData,"Arm1 ON") == 0)
      {
       
          activateArm1Relay();
          // Perform actions when data matches
        }
      else  if (strcmp(receivedData,"Arm1 OFF") == 0)
      {
       
          deactivateArm1Relay();
          // Perform actions when data matches
       }

       
     else  if (strcmp(receivedData,"Arm2 ON") == 0)
        {
         
            activateArm2Relay();
            // Perform actions when data matches
         }
      else  if (strcmp(receivedData,"Arm2 OFF") == 0)
        {
         
            deactivateArm2Relay();
            // Perform actions when data matches
         }

    


       else  if (strcmp(receivedData,"direction UP") == 0)
      {
       
           moveMotorsUp(Speed);
          // Perform actions when data matches
        }
      else  if (strcmp(receivedData,"direction Down") == 0)
      {
       
           moveMotorsDown(Speed);
          // Perform actions when data matches
       }
      else  if (strcmp(receivedData,"Camera ON") == 0)
      {
       
            activateCameraRelay();
            
          // Perform actions when data matches
        }
      else  if (strcmp(receivedData,"Camera OFF") == 0)
      {
       
           deactivateCameraRelay();
          // Perform actions when data matches
       }
       else  if (strcmp(receivedData,"direction forward") == 0)
      {
       
           moveMotorsBackward(Speed);
           Serial.println("In");
          // Perform actions when data matches
       }
       else  if (strcmp(receivedData,"direction reverse") == 0)
      {
       
           moveMotorsForward(Speed);
          // Perform actions when data matches
       }
       else  if (strcmp(receivedData,"direction left") == 0)
      {
       
           moveMotorsLeft(Speed);
          // Perform actions when data matches
       }
       else  if (strcmp(receivedData,"direction right") == 0)
      {
       
           moveMotorsRight(Speed);
          // Perform actions when data matches
       }       
       else  if (strcmp(receivedData,"Motor ON") == 0)
      {
       
          // Perform actions when data matches
       }
             else  if (strcmp(receivedData,"Motor OFF") == 0)
      {
       
          // Perform actions when data matches
       }
      

    if (strcmp(previousState, receivedData) != 0) 
    {
    // State has changed
        BreakMotor();
        strcpy(previousState, receivedData);
        
    }
  
    
       
       
       

         

      


    
    // Reset the dataLength to zero for next iteration
    dataLength = 0;

    // Close the connection
    client.stop();
  }
}
