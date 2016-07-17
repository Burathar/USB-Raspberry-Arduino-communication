const int ledPin = 13;

int data = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  Serial.setTimeout(3);
  if (Serial.available() > 0) {
    data = Serial.parseInt();
    if (data == 2){     //The Raspberry Pi sends this vallue to initate the handshake, you can change it to whatever vallue you want as long as it is the same on the Raspberry side.
    Serial.write("87653"); //This is the return vallue the Raspberry Pi waits for
    }
    for (int i=0; i <= data - 1; i++){  //This is just an optional debugging function
      digitalWrite(ledPin, HIGH);
      delay(200);
      digitalWrite(ledPin, LOW);
      delay(300);
   } 
  }
}

