#include <IRremote.h>

IRsend irsend;
void setup()
{
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
      irsend.sendNEC(0xA90, 32);  //這邊要加上0x !
      Serial.print("1");
      delay(1000);
  }     
}
