#include <Servo.h>   
Servo myservo;  

void setup() 
{
  Serial.begin(9600);
  myservo.attach(9);  
}
void loop() 
{
  char a=Serial.read();  
  if(a=='9')
  { 
    myservo.write(0);  
    delay(1000);
    myservo.write(90); 
    delay(1000);
    myservo.write(0); 
    delay(1000);
    myservo.write(90); 
    delay(1000);
    myservo.write(0);
  }
}
