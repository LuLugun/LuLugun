#include <LiquidCrystal_PCF8574.h>
#include <OneWire.h>                         //防水型溫度感測器
#include <DallasTemperature.h>               //防水型溫度感測器 
#include "DHT.h"
#include <Servo.h>
LiquidCrystal_PCF8574 lcd(0x27);  // 設定i2c位址，一般情況就是0x27和0x3F兩種
DHT dht(3, DHT11); 
Servo myservo;
OneWire oneWire1(11);                        //NO1 water temperature 
OneWire oneWire3(13);                        //bucket water temperature 
DallasTemperature DS18B20_1(&oneWire1);
DallasTemperature DS18B20_3(&oneWire3);   
#define TdsSensorPin A0
#define TdsSensorPin1 7
#define VREF 5.0      // analog reference voltage(Volt) of the ADC
int analogBuffer;    // store the analog value in the array, read from ADC
int analogBufferTemp;
int analogBufferIndex = 0,copyIndex = 0;
float averageVoltage = 0,tdsValue = 0,temperature = 25;
int c = 0;


void setup()
{  
  Serial.begin(9600);
  lcd.begin(16, 4); // 初始化LCD
  lcd.setBacklight(255);
  lcd.clear();
  lcd.setCursor(0, 0);  //設定游標位置 (字,行)
  dht.begin();
  DS18B20_1.begin();
  DS18B20_3.begin(); 
  myservo.attach(2);   //light
  pinMode(A0, INPUT);     //TDS
  pinMode(7, INPUT);     //TDS
  pinMode(A1, INPUT);     //MQ-135
  pinMode(A2, INPUT);     //MQ-2 
  pinMode(10, OUTPUT);     //NO1.in
  pinMode(8, OUTPUT);     //NO1.out
  pinMode(A3, INPUT);     //TEMT6000
  pinMode(12, OUTPUT);    //NO1.trig
  pinMode(9, INPUT);     //NO1.echo
  pinMode(5, OUTPUT);     //atomizer
  pinMode(4, OUTPUT);     //water.trig 
  pinMode(6, INPUT);      //water.echo
}

void loop()
{
  char a=Serial.read();

  
  
  float h = dht.readHumidity();   //取得濕度
  float t = dht.readTemperature();  //取得溫度
  DS18B20_1.requestTemperatures();
  float wt = DS18B20_1.getTempCByIndex(0);//取得水溫
  analogBuffer= analogRead(TdsSensorPin);    //read the analog value and store into the buffer
  analogBufferTemp= analogBuffer;
  averageVoltage = analogBufferTemp * (float)VREF / 1024.0; // read the analog value more stable by the median filtering algorithm, and convert to voltage value
  float compensationCoefficient=1.0+0.02*(temperature-25.0);    //temperature compensation formula: fFinalResult(25^C) = fFinalResult(current)/(1.0+0.02*(fTP-25.0));
  float compensationVolatge=averageVoltage/compensationCoefficient;  //temperature compensation
  tdsValue=(133.42*compensationVolatge*compensationVolatge*compensationVolatge - 255.86*compensationVolatge*compensationVolatge + 857.39*compensationVolatge)*0.5; //convert voltage value to tds value
  
  lcd.clear();
  lcd.setCursor(0, 0);  //設定游標位置 (字,行)
  lcd.print("RH   :");  //Relative Humidity 相對濕度簡寫
  lcd.setCursor(7, 0);  
  lcd.print(h);
  lcd.setCursor(12, 0);
  lcd.print("%");

  lcd.setCursor(0, 1);  //設定游標位置 (字,行)
  lcd.print("Temp :");
  lcd.setCursor(7, 1);  
  lcd.print(t);
  lcd.setCursor(12, 1);
  lcd.print((char)223); //用特殊字元顯示符號的"度"
  lcd.setCursor(13, 1);
  lcd.print("C");

  lcd.setCursor(4, 2);  //設定游標位置 (字,行)
  lcd.print("Water:");
  lcd.setCursor(11, 2);  
  lcd.print(wt);
  lcd.setCursor(17, 2);
  lcd.print((char)223); //用特殊字元顯示符號的"度"
  lcd.setCursor(18, 2);
  lcd.print("C");

  lcd.setCursor(4, 3);  //設定游標位置 (字,行)
  lcd.print("TDS  :"); 
  lcd.setCursor(11, 3);  
  lcd.print(tdsValue);
  lcd.setCursor(18, 3);
  delay(1000);

  while(a=='a')                        //No1 out         
  {
    digitalWrite(8,HIGH);
    char b=Serial.read();
    if(b=='2')
    {
      digitalWrite(8,LOW);
      break;
    }
  }

  while(a=='b')                       //No1 in  
  {
    digitalWrite(10,HIGH);
    char b=Serial.read();
    if(b=='2')
    {
      digitalWrite(10,LOW);
      break;
    }
  }

  

  if(a=='z')                          //No1 change  
  {
     long cm1,cm2,duration1,duration2;
    digitalWrite(12, LOW);
    delayMicroseconds(5);
    digitalWrite(12, HIGH);     
    delayMicroseconds(10);
    digitalWrite(12, LOW); 
    pinMode(9,INPUT);            
    duration1 = pulseIn(9, HIGH);   
    cm1 = (duration1/2) / 29.1;        
    if(cm1<=5)
    {
       int aa=0;
       while(aa<8)
       {
         digitalWrite(8,HIGH);
         digitalWrite(12, LOW);
         delayMicroseconds(5);
         digitalWrite(12, HIGH);     
         delayMicroseconds(10);
         digitalWrite(12, LOW);
         pinMode(9,INPUT);            
         duration1 = pulseIn(9, HIGH);   
         cm1 = (duration1/2) / 29.1; 
         if(cm1>=10)
         {
          aa+=1;       
         }
         char b=Serial.read();
         if(b=='2')
         {
           break;
         }
         delay(500);
       }
    }
    digitalWrite(8,LOW);
    delay(500);
    digitalWrite(12, LOW);
    delayMicroseconds(5);
    digitalWrite(12, HIGH);     
    delayMicroseconds(10);
    digitalWrite(12, LOW);
    pinMode(9,INPUT);             
    duration1 = pulseIn(9, HIGH);   
    cm1 = (duration1/2) / 29.1;
    delay(5000);
    if(cm1>=6)
    {
      int aa=0;
      while(aa<10)
      {
         digitalWrite(10,HIGH);
         digitalWrite(12, LOW);
         delayMicroseconds(5);
         digitalWrite(12, HIGH);     
         delayMicroseconds(10);
         digitalWrite(12, LOW);   
         pinMode(9,INPUT);          
         duration1 = pulseIn(9, HIGH);   
         cm1 = (duration1/2) / 29.1;
         if(cm1<=4)
         {
          aa+=1;       
         }
         char b=Serial.read();
         if(b=='2')
         {
           break;
         }
         delay(500);
      } 
    }
    digitalWrite(10,LOW);
  }
  

  
  if(a=='6')                        //water temperature1
  {
    DS18B20_1.requestTemperatures();
    Serial.println(DS18B20_1.getTempCByIndex(0));
  }
  if(a=='7')                        //CO2
  {
    int sensorValue = analogRead(A1);
    Serial.println(sensorValue, DEC);
  }
  if(a=='8')                       //smoke
  {
     int smokeValue = analogRead(A2); 
     Serial.println(smokeValue);
  }
  
  if(a=='f')                     //water temperature3
  {
    DS18B20_3.requestTemperatures();
    Serial.println(DS18B20_3.getTempCByIndex(0));
  }

  if(a=='t')                       //TDS
  {
    analogBuffer= analogRead(TdsSensorPin);    //read the analog value and store into the buffer
    analogBufferTemp= analogBuffer;
    averageVoltage = analogBufferTemp * (float)VREF / 1024.0; // read the analog value more stable by the median filtering algorithm, and convert to voltage value
    float compensationCoefficient=1.0+0.02*(temperature-25.0);    //temperature compensation formula: fFinalResult(25^C) = fFinalResult(current)/(1.0+0.02*(fTP-25.0));
    float compensationVolatge=averageVoltage/compensationCoefficient;  //temperature compensation
    tdsValue=(133.42*compensationVolatge*compensationVolatge*compensationVolatge - 255.86*compensationVolatge*compensationVolatge + 857.39*compensationVolatge)*0.5; //convert voltage value to tds value
    Serial.println(tdsValue,0);
    analogBuffer= analogRead(TdsSensorPin1);    //read the analog value and store into the buffer
    analogBufferTemp= analogBuffer;
    averageVoltage = analogBufferTemp * (float)VREF / 1024.0; // read the analog value more stable by the median filtering algorithm, and convert to voltage value
    float compensationCoefficient1=1.0+0.02*(temperature-25.0);    //temperature compensation formula: fFinalResult(25^C) = fFinalResult(current)/(1.0+0.02*(fTP-25.0));
    float compensationVolatge1=averageVoltage/compensationCoefficient1;  //temperature compensation
    tdsValue=(133.42*compensationVolatge1*compensationVolatge1*compensationVolatge1 - 255.86*compensationVolatge1*compensationVolatge1 + 857.39*compensationVolatge1)*0.5; //convert voltage value to tds value
    Serial.println(tdsValue,0);
  }
  if(a=='4')                        //temperature 
  {
    float t = dht.readTemperature();
    if (isnan(t))
    {
      Serial.println("無法從DHT傳感器讀取！");
      return;
    }
    Serial.println(t);

  }

  if(a=='h')                      //humiduty
  {
    float h = dht.readHumidity();
    if (isnan(h))
    {
      Serial.println("無法從DHT傳感器讀取！");
      return;
    }
    Serial.println(h);

  }
  if(a=='5')                        //TEMT6000
  {
    int light_value = analogRead(A3);
    float volts = analogRead(A3) * 5.0 / 1024.0;
    float amps = volts / 10000.0;
    float microamps = amps * 1000000;
    float lux = microamps * 2.0;
    Serial.println (lux);
  }

  if (a=='w')                    //atomizer
  {
      digitalWrite(5, HIGH);
      delay(10000);              
      digitalWrite(5, LOW);   
  }

  if(a=='9')                     //light
  {
    myservo.write(0);  
    delay(1000);
    myservo.write(48); 
    delay(1000);
    myservo.write(0); 
    delay(1000);
    myservo.write(48); 
    delay(1000);
    myservo.write(0);
  }

  if(a=='3')                         //water level
  {
    digitalWrite(12, LOW);
    delayMicroseconds(5);
    digitalWrite(12, HIGH);     
    delayMicroseconds(10);
    digitalWrite(12, LOW);
    pinMode(9, INPUT);             
    long duration1 = pulseIn(9, HIGH);   
    long cm1 = (duration1/2) / 29.1; 
    digitalWrite(4, LOW);
    delayMicroseconds(5);
    digitalWrite(4, HIGH);     
    delayMicroseconds(10);
    digitalWrite(4, LOW);
    pinMode(6, INPUT);             
    long duration3 = pulseIn(6, HIGH);   
    long cm3 = (duration3/2) / 29.1;  
    Serial.print("盆栽水位:");
    Serial.println(cm1);
    Serial.print("水池水位:");
    Serial.println(cm3);
  }
} 
