/*
 * IRremote: IRsendDemo - demonstrates sending IR codes with IRsend
 * An IR LED must be connected to Arduino PWM pin 3.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 */

#include <NewPing.h>
 
#define TRIGGER_PIN  12
#define ECHO_PIN     11
#define MAX_DISTANCE 200
 
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
#include <IRremote.h>

IRsend irsend;

void setup()
{
  Serial.begin(115200);
}

void loop() {
  delay(50);
  Serial.print("Ping: ");
  Serial.print(sonar.ping_cm());
  Serial.println("cm"); 
  if (sonar.ping_cm() <= 50) {
	  for (int i = 0; i < 2; i++) {
		  irsend.sendSony(0xa90, 12);
		  delay(50);
	}
  }
 delay(500);
}
