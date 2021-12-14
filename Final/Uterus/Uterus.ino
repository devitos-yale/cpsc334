const byte red1 = 15;
const byte red2 = 2;
const byte red3 = 4;
const byte red4 = 5;
const byte red5 = 32;
const byte red6 = 33;
const byte red7 = 25;
const byte red8 = 26;
const byte red9 = 27;
const byte red10 = 14;
const byte red11 = 12;
const byte white1 = 16;
const byte white2 = 17;
const byte white3 = 18;
const byte white4 = 19;
const byte white5 = 21;
const byte ovary = 22;
int stage = 0;
int power = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(red1, OUTPUT);
  pinMode(red2, OUTPUT);
  pinMode(red3, OUTPUT);
  pinMode(red4, OUTPUT);
  pinMode(red5, OUTPUT);
  pinMode(red6, OUTPUT);
  pinMode(red7, OUTPUT);
  pinMode(red8, OUTPUT);
  pinMode(red9, OUTPUT);
  pinMode(red10, OUTPUT);
  pinMode(red11, OUTPUT);
  pinMode(white1, OUTPUT);
  pinMode(white2, OUTPUT);
  pinMode(white3, OUTPUT);
  pinMode(white4, OUTPUT);
  pinMode(white5, OUTPUT);
  pinMode(ovary, OUTPUT);

  Serial.begin(115200);
}

// the loop function runs over and over again forever
void loop() {
  int powerb = digitalRead(9); //power button
  int playb = digitalRead(10); //play button=

  if (powerb == 0) {
    if (power == 0) { //power on
      power = 1;
    }
    else { //power off
      power = 0;
    }
    
    delay(1000);
  }

  if (playb == 0) {
    stage = stage+1;
    if (stage == 4) {
      stage = 0;
    }
    Serial.println(stage);
    delay(1000);
  }

  if (stage == 0) { //follicals growing in ovary
    digitalWrite(ovary, HIGH);
    delay(300);
    digitalWrite(ovary, LOW);
    delay(300);
  }

  if (stage == 1) { //Ovulation + travel through fallopean tube
    digitalWrite(white1, LOW);
    digitalWrite(white5, HIGH);
    delay(300);
    digitalWrite(white5, LOW);
    digitalWrite(white4, HIGH);
    delay(300);
    digitalWrite(white4, LOW);
    digitalWrite(white3, HIGH);
    delay(300);
    digitalWrite(white3, LOW);
    digitalWrite(white2, HIGH);
    delay(300);
    digitalWrite(white2, LOW);
    digitalWrite(white1, HIGH);
    delay(300);
  }

  if (stage == 2) { //ovum embedds + endometrium grows
    digitalWrite(white1, HIGH);
    for (int i=50; i>=0; i--) {
      digitalWrite(red1, HIGH);
      digitalWrite(red2, HIGH);
      digitalWrite(red3, HIGH);
      digitalWrite(red4, HIGH);
      digitalWrite(red5, HIGH);
      digitalWrite(red6, HIGH);
      digitalWrite(red7, HIGH);
      digitalWrite(red8, HIGH);
      digitalWrite(red9, HIGH);
      digitalWrite(red10, HIGH);
      digitalWrite(red11, HIGH);
      delay(2);
      digitalWrite( red1, LOW );
      digitalWrite( red2, LOW );
      digitalWrite( red3, LOW );
      digitalWrite( red4, LOW );
      digitalWrite( red5, LOW );
      digitalWrite( red6, LOW );
      digitalWrite( red7, LOW );
      digitalWrite( red8, LOW );
      digitalWrite( red9, LOW );
      digitalWrite( red10, LOW );
      digitalWrite( red11, LOW );
      delay(10);
    }
    for (int i=50; i>=0; i--) {
      digitalWrite(red1, HIGH);
      digitalWrite(red2, HIGH);
      digitalWrite(red3, HIGH);
      digitalWrite(red4, HIGH);
      digitalWrite(red5, HIGH);
      digitalWrite(red6, HIGH);
      digitalWrite(red7, HIGH);
      digitalWrite(red8, HIGH);
      digitalWrite(red9, HIGH);
      digitalWrite(red10, HIGH);
      digitalWrite(red11, HIGH);
      delay(6);
      digitalWrite( red1, LOW );
      digitalWrite( red2, LOW );
      digitalWrite( red3, LOW );
      digitalWrite( red4, LOW );
      digitalWrite( red5, LOW );
      digitalWrite( red6, LOW );
      digitalWrite( red7, LOW );
      digitalWrite( red8, LOW );
      digitalWrite( red9, LOW );
      digitalWrite( red10, LOW );
      digitalWrite( red11, LOW );
      delay(10);
    }
    for (int i=50; i>=0; i--) {
      digitalWrite(red1, HIGH);
      digitalWrite(red2, HIGH);
      digitalWrite(red3, HIGH);
      digitalWrite(red4, HIGH);
      digitalWrite(red5, HIGH);
      digitalWrite(red6, HIGH);
      digitalWrite(red7, HIGH);
      digitalWrite(red8, HIGH);
      digitalWrite(red9, HIGH);
      digitalWrite(red10, HIGH);
      digitalWrite(red11, HIGH);
      delay(10);
      digitalWrite( red1, LOW );
      digitalWrite( red2, LOW );
      digitalWrite( red3, LOW );
      digitalWrite( red4, LOW );
      digitalWrite( red5, LOW );
      digitalWrite( red6, LOW );
      digitalWrite( red7, LOW );
      digitalWrite( red8, LOW );
      digitalWrite( red9, LOW );
      digitalWrite( red10, LOW );
      digitalWrite( red11, LOW );
      delay(10);
    }
  }
  
  if (stage == 3) { //Menstruation
    digitalWrite(white1, LOW);
    digitalWrite(red1, HIGH);
    digitalWrite(red2, HIGH);
    digitalWrite(red3, HIGH);
    digitalWrite(red4, HIGH);
    digitalWrite(red5, HIGH);
    digitalWrite(red6, HIGH);
    digitalWrite(red7, HIGH);
    digitalWrite(red8, HIGH);
    digitalWrite(red9, HIGH);
    digitalWrite(red10, HIGH);
    digitalWrite(red11, HIGH);
    delay(300);
    digitalWrite(red1, LOW);
    digitalWrite(red2, LOW);
    digitalWrite(red3, LOW);
    digitalWrite(red4, LOW);
    delay(300);
    digitalWrite(red5, LOW);
    digitalWrite(red11, LOW);
    delay(300);
    digitalWrite(red6, LOW);
    digitalWrite(red10, LOW);
    delay(300);
    digitalWrite(red7, LOW);
    digitalWrite(red9, LOW);
    delay(300);
    digitalWrite(red8, LOW);
  }
}
