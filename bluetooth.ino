void setup() {
  // initialize serial:
  Serial.begin(9600);
  // initialize the led pin
  pinMode(13, OUTPUT);
}

void loop() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    switch(inChar) {
      case '1':
        digitalWrite(13, HIGH);
      break;
      case '0':
        digitalWrite(13, LOW);
      break;
    }
    
    /*digitalWrite(13, inChar == '1' ? HIGH : LOW);*/
    Serial.println(inChar);
  }
}

