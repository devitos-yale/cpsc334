// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  //int sensorValue = digitalRead(10);
  int joystickY = analogRead(34);
  int joystickX = analogRead(35);
  int joystickSW = digitalRead(10);
  int button = digitalRead(9);
  int flipswitch = digitalRead(11);
  //int key = 5000;
  // print out the value you read:
  Serial.println(5000); //start key
  Serial.println(joystickY);
  Serial.println(joystickX);
  Serial.println(joystickSW);
  //Serial.println("BUTTONS:");
  Serial.println(button);
  Serial.println(flipswitch);
  delay(10);        // delay in between reads for stability
}
