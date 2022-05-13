#include "DHT.h"
DHT dht(3, DHT11);                           //DHT11

void setup() 
{
  dht.begin();
  Serial.begin(9600);
  pinMode(5, OUTPUT);     //atomizer
}

void loop()
{
  char a=Serial.read();
  
  
  if (a=='w')                    //atomizer
  {
      digitalWrite(5, HIGH);
      delay(10000);              
      digitalWrite(5, LOW);   
  }

  if(a=='4')                        //temperature 
  {
    float t = dht.readTemperature();
    if (isnan(t))
    {
      Serial.println("無法從DHT傳感器讀取！");
      return;
    }
    Serial.print(t);
  }

  if(a=='h')                      //humiduty
  {
    float h = dht.readHumidity();
    if (isnan(h))
    {
      Serial.println("無法從DHT傳感器讀取！");
      return;
    }
    Serial.print(h);  
  }


}
