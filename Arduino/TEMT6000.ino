void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT); 

}

void loop() {
  int light_value = analogRead(A0);
  float volts = analogRead(A0) * 5.0 / 1024.0;   
  float amps = volts / 10000.0;     
  float microamps = amps * 1000000;  
  float lux = microamps * 2.0;       
  Serial.print ("Raw ADC data:");
  Serial.println (light_value);
  Serial.print ("Volts:");
  Serial.println (volts);
  Serial.print ("Lux:");
  Serial.println (lux);  
  delay(1000);
  
}
