//LingShun Lab

#define Moisture A1 //定義AO 引腳 為 IO-A0
#define DO 13        //定義DO 引腳 為 IO-7

void setup() {
  pinMode(Moisture, INPUT);//定義A0為輸入模式
  pinMode(DO, INPUT);
  Serial.begin(9600);
}

void loop() {
  //串列埠返回測量資料
  Serial.print("Moisture=");
  Serial.print(analogRead(Moisture));//讀取AO的數值
  Serial.print("|DO=");
  Serial.println(digitalRead(DO));//讀取DO的數值
  delay(1000);
}
