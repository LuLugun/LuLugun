#define TdsSensorPin A0
#define VREF 5.0      // analog reference voltage(Volt) of the ADC
int analogBuffer;    // store the analog value in the array, read from ADC
int analogBufferTemp;
int analogBufferIndex = 0,copyIndex = 0;
float averageVoltage = 0,tdsValue = 0,temperature = 25;
 
void setup()
{
    Serial.begin(9600);
    pinMode(TdsSensorPin,INPUT);
}
 
void loop()
{
     
      analogBuffer= analogRead(TdsSensorPin);    //read the analog value and store into the buffer
      analogBufferTemp= analogBuffer;
      averageVoltage = analogBufferTemp * (float)VREF / 1024.0; // read the analog value more stable by the median filtering algorithm, and convert to voltage value
      float compensationCoefficient=1.0+0.02*(temperature-25.0);    //temperature compensation formula: fFinalResult(25^C) = fFinalResult(current)/(1.0+0.02*(fTP-25.0));
      float compensationVolatge=averageVoltage/compensationCoefficient;  //temperature compensation
      tdsValue=(133.42*compensationVolatge*compensationVolatge*compensationVolatge - 255.86*compensationVolatge*compensationVolatge + 857.39*compensationVolatge)*0.5; //convert voltage value to tds value
      Serial.print("TDS Value:");
      Serial.print(tdsValue,0);
      Serial.println("ppm");
   
}
