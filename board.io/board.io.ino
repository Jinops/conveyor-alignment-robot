#include <MyCobotBasic.h>
#include <ParameterList.h>

MyCobotBasic myCobot;
int incomingByte;

void init_angles(int speed=20){
  myCobot.setLEDRGB(0XFF, 0, 0);
  myCobot.writeAngle(1, 0, speed);
  delay(1000);
  myCobot.writeAngle(2, 0, speed);
  delay(1000);
  myCobot.writeAngle(3, 0, speed);
  delay(1000);
  myCobot.writeAngle(4, 0, speed);
  delay(1000);
  myCobot.writeAngle(5, 0, speed);
  delay(1000);
  myCobot.writeAngle(6, 0, speed);
  delay(1000);
  myCobot.setLEDRGB(0, 0, 0XFF);
}

void test(){
  myCobot.writeAngle(2, -60, 50);
  delay(1000);
  myCobot.writeAngle(3, -30, 50);
  delay(1000);
}

void blink(int count, int delay_ms=100){
  for (int i=0; i<count; i++){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(delay_ms);
    digitalWrite(LED_BUILTIN, LOW);
    delay(delay_ms);
  }
}

void setup() {
  myCobot.setup();
  myCobot.powerOn();

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  init_angles(50);
  Serial1.begin(9600);   // Cobot uses Serial0 (rx,tx 0)

  test();
}

void loop() {
  // if (Serial1.available()) {
  //   incomingByte = Serial.parseInt();

  //   Serial1.print("I received: ");
  //   Serial1.println(incomingByte, DEC);

  //   blink(incomingByte);

  //   if (incomingByte == 99){
  //     myCobot.setLEDRGB(byte(0), byte(0), byte(0));
  //   } else {
  //     myCobot.setLEDRGB(0, byte(incomingByte), 0);
  //   }
  // }
}

