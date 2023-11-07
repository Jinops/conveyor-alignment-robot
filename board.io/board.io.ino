#include <MyCobotBasic.h>
#include <ParameterList.h> // Define rx/tx port here!

MyCobotBasic myCobot;
String SerialData;
int num;

void initAngles(){
  myCobot.setLEDRGB(byte(255), 0, 0);
  Angles angles = {0, 0, 0, 0, 0, 0};
  myCobot.writeAngles(angles, 20);
  delay(200);
  myCobot.setLEDRGB(0, 0, byte(255));
}

void test(){
  myCobot.writeAngles({0.08,98.43,-117.33,-56.07,0.26,0.52}, 20);
}

void blink(int count, int delay_ms=100){
  for (int i=0; i<count; i++){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(delay_ms);
    digitalWrite(LED_BUILTIN, LOW);
    delay(delay_ms);
  }
}

void printAngles(){
  Serial.print(" (Angles) {");
  for (int i=0; i<=5; i++){
    Serial.print(myCobot.getAngles()[i]);
    (i < 5) ? Serial.print(",") : NULL;
  }
  Serial.print('}');
}

void printCoords(){
  Serial.print(" (Coords) {");
  for (int i=0; i<=5; i++){
    Serial.print(myCobot.getCoords()[i]);
    (i < 5) ? Serial.print(",") : NULL;
  }
  Serial.print('}');
}

void setup() {;
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  myCobot.setup();
  myCobot.powerOn();
  initAngles();

  Serial.begin(9600); // USB Serial / Cobot uses Serial1
}

void loop() {
  if (Serial.available()) {
    SerialData = Serial.readString();
    Serial.print("(Serial) " + SerialData);
    num = SerialData.substring(0, 1).toInt();

    if(num==0){
      printAngles();
      printCoords();
    }
    else if (1 <= num && num <= 6){
      int angle = SerialData.substring(1).toInt();
      myCobot.writeAngle(num, angle, 20);
    } 
    else if(num==7){
      initAngles();
    }
    else if (num==8){
      test();
    }
    else if(num==9){ // moter ON / OFF
      Serial.print(myCobot.isPoweredOn());
      if(myCobot.isPoweredOn()){
        myCobot.setLEDRGB(0, byte(50), 0);
        myCobot.powerOff();
      } else {
        myCobot.powerOn();
        myCobot.setLEDRGB(0, 0, byte(255));
        printAngles();
        printCoords();
      }
    }
  }
}
