#include "DHT.h"
DHT dht(3, DHT11);

void setup()
{
  Serial.begin(9600);
  dht.begin(); 
  
} // setup()

void loop()
{
  delay(1000);
  float h = dht.readHumidity();   //取得濕度
  float t = dht.readTemperature();  //取得溫度C

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(" *C ");
 
}
