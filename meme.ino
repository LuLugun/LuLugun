int buzzer = 8; //設置控制蜂鳴器的數位 IO 腳 
void setup() {
  pinMode(buzzer, OUTPUT); //設置數位 IO 腳模式，OUTPUT 為轀出 
} 
void loop() {
  unsigned char i, j; //定義變數
  while (1) {     for (i = 0; i < 80; i++){ //發出一個頻率的聲音
    digitalWrite(buzzer, HIGH); //發聲音
    delay(1);//延時 1ms
    digitalWrite(buzzer, LOW); //不發聲音
    delay(1);//延時 1ms
    } 
  }
 }
