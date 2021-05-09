/*
 * IRremote: IRsendDemo - demonstrates sending IR codes with IRsend
 * An IR LED must be connected to Arduino PWM pin 3.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 */


#include <IRremote.h>

IRsend irsend;

const byte pirPin = 12;

void setup()
{
  pinMode(pirPin , INPUT);
  Serial.begin(9600);
}

void loop() {
  boolean val = digitalRead(pirPin);
  if(val == 1){
    for (int i = 0; i < 2; i++) {
    irsend.sendSony(0xa90, 12);
    delay(50);
  }
    Serial.print("on");
}
delay(500);
}
