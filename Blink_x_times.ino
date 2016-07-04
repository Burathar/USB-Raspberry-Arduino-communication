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
    if (data == 2){
    Serial.write("87653");
    }
    for (int i=0; i <= data - 1; i++){
      digitalWrite(ledPin, HIGH);
      delay(200);
      digitalWrite(ledPin, LOW);
      delay(300);
   } 
  }
}

