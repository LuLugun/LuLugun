#include <OneWire.h>
#include <DallasTemperature.h>
OneWire oneWire(A4);
DallasTemperature DS18B20(&oneWire);

void setup(void)
{
  Serial.begin(9600);
  DS18B20.begin();
}

void loop(void)
{
  DS18B20.requestTemperatures();
  Serial.println(DS18B20.getTempCByIndex(0));
  delay(1000);
}
