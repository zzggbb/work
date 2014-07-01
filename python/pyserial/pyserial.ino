int pin = 11;

void setup() {
  // setup pin 13 for output
  pinMode(pin,OUTPUT);
  // init serial port
  Serial.begin(9600); 
}

void loop() {
  String str;
  if (Serial.available() > 0) {
    str = Serial.readStringUntil('\n');
  }
  if(str=="on") digitalWrite(pin,HIGH);

  if(str=="off") digitalWrite(pin,LOW);

  if(str=="pause") delay(500);
  
  delay(500);
}
