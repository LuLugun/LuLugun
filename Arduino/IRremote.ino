#include <IRremote.h> //引用 IRremote 函式庫
const int irReceiverPin = 2; //紅外線接收器訊號接在針腳 2
IRrecv irrecv(irReceiverPin); // 定義 IRrecv 物件來接收紅外線訊號
decode_results results; // 解碼結果將放在 decode_results 結構的 result 變數裏;
/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/
/*
   BYJ48 Stepper motor code
   Connect :
   IN1 >> D8
   IN2 >> D9
   IN3 >> D10
   IN4 >> D11
   VCC ... 5V Prefer to use external 5V Source
   Gnd
   written By :Mohannad Rawashdeh
  https://www.instructables.com/member/Mohannad+Rawashdeh/
     28/9/2013
  */

#include <Servo.h>
#define IN1 8
#define IN2 9
#define IN3 10
#define IN4 11
Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 7;    // variable to store the servo position
int Steps = 0;
boolean Direction = true;
unsigned long last_time;
unsigned long currentMillis;
int steps_left=4095;
long time;
void setup() {
  myservo.attach(9);
  Serial.begin(9600); //開啟 Serial port, 通訊速率為 9600 bps
  irrecv.enableIRIn(); // 啟動紅外線解碼
}
void loop() {
if (irrecv.decode(&results)) { // 解碼成功，收到一組紅外線訊號
if(results.value == 0xFF30CF)
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, HIGH);
  for (pos = 0; pos <= 20; pos += 1) {
    myservo.write(pos);
    delay(15); 
  }
  delay(1000);
  for (pos = 20; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}
if(results.value == 0xFF18E7)
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  for (pos = 0; pos <= 40; pos += 1) {
    myservo.write(pos);
    delay(15); 
  }
  delay(1000);
  for (pos = 40; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}
if(results.value == 0xFF7A85)
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  for (pos = 0; pos <= 60; pos += 1) {
    myservo.write(pos);
    delay(15); 
  }
  delay(1000);
  for (pos = 60; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}
if(results.value == 0xFF10EF)
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  for (pos = 0; pos <= 80; pos += 1) {
    myservo.write(pos);
    delay(15); 
  }
  delay(1000);
  for (pos = 80; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}
if(results.value == 0xFF38C7)
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  for (pos = 0; pos <= 100; pos += 1) {
    myservo.write(pos);
    delay(15); 
  }
  delay(1000);
  for (pos = 100; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}
irrecv.resume(); // 繼續收下一組紅外線訊號
}
}
