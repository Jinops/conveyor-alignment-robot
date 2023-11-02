#include <MyCobotBasic.h>
int incomingByte;

void blink(int count, int delay_ms=200){
  for (int i=0; i<count; i++){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(delay_ms);
    digitalWrite(LED_BUILTIN, LOW);
    delay(delay_ms);
  }
}

void setup() {
  // myCobot.setup();
  // myCobot.powerOn();

  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  // if (Serial.available()){
  //   data = Serial.read();
  //   if (data == '1'){
  //     digitalWrite(LED_BUILTIN, HIGH);
  //   }
  // }
    if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.parseInt();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);

    blink(incomingByte);
  }
}

