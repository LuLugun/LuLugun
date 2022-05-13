void setup(){
  Serial.begin(9600);
  pinMode(A2, INPUT);;
}
 
void loop(){
  int smokeValue = analogRead(A2); 
  Serial.println(smokeValue);
  delay(1000);
  
}
