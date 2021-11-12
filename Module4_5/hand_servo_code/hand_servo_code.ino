#include <ESP32Servo.h>
 
Servo one;  // create servo object to control a servo
Servo two;
Servo three;
Servo four;
Servo five;
// 16 servo objects can be created on the ESP32
 
int pos = 0;    // variable to store the servo position
// Recommended PWM GPIO pins on the ESP32 include 2,4,12-19,21-23,25-27,32-33 
int servoPin = 26;
int randone;
int randtwo;
int randthree;
int randfour;
int randfive;
 
void setup() {
  // Allow allocation of all timers
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  one.setPeriodHertz(50);    // standard 50 hz servo
  one.attach(26, 500, 2400); // attaches the servo on pin 18 to the servo object
  // using default min/max of 1000us and 2000us
  // different servos may require different min/max settings
  // for an accurate 0 to 180 sweep
  two.setPeriodHertz(50);    // standard 50 hz servo
  two.attach(27, 500, 2400);
  three.setPeriodHertz(50);    // standard 50 hz servo
  three.attach(14, 500, 2400);
  four.setPeriodHertz(50);    // standard 50 hz servo
  four.attach(12, 500, 2400);
  five.setPeriodHertz(50);    // standard 50 hz servo
  five.attach(13, 500, 2400);

  randomSeed(analogRead(0));
}
 
void loop() {
 
  for (pos = 10; pos <= 40; pos += 1) { // goes from 0 degrees to 180 degrees
    randone = random(10, 40);
    randtwo = random(0, 30);
    randthree = random(10, 40);
    randfour = random(10, 40);
    randfive = random(10, 40);
    // in steps of 1 degree
    //myservo.write(pos);    // tell servo to go to position in variable 'pos'
    one.write(randone);
    two.write(randtwo); //0 is home state
    three.write(randthree);
    four.write(randfour);
    five.write(randfive);
    delay(100);             // waits 15ms for the servo to reach the position
  }
}
