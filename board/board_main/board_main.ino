#include <MyCobotBasic.h>
#include <ParameterList.h> // serial port is defined here depend on board. (for me, MyCobot_Mega)

MyCobotBasic myCobot;
int serialInput;

Coords coords_0 = {32.50,-60.40,93.60,93.68,11.88,-81.59};
Coords coords_100 = {133.00,-48.40,93.50,91.59,-20.93,-82.74};
Coords coordsToMove;
Coords coordsToIdle;

int speed = 30; // movement speed
int msToStay = 3000; // time for moving+staying
int IdleAddZ = 25; // adding Y of Coord after stay

void initAngles(){
  Angles angles = {0, 0, 0, 0, 0, 0};
  myCobot.writeAngles(angles, 20);
}

void setColorIfMoving(){ // TODO: Check Performance
  if(myCobot.checkRunning()){
    myCobot.setLEDRGB(byte(255), 0, 0);
  }
  else {
    myCobot.setLEDRGB(0, 0, byte(255));
  }
}

void printCoords(){
  Serial.print(" (Coords) {");
  for (int i=0; i<=5; i++){
    Serial.print(myCobot.getCoords()[i]);
    (i < 5) ? Serial.print(",") : NULL;
  }
  Serial.print('}');
}

void setCoords(Coords* coords){
  if(myCobot.isPoweredOn()){
    myCobot.setLEDRGB(0, 30, 0);
    myCobot.powerOff();
  } else {
    myCobot.powerOn();
    *coords = myCobot.getCoords();
    printCoords();
  }
}

void move(int length){
  for (int i = 0; i < Axes; i++){
    coordsToMove[i] = coords_0[i] + (coords_100[i] - coords_0[i]) * length / 100;
  }
  myCobot.writeCoords(coordsToMove, speed);
  printCoords();
  delay(msToStay);
  coordsToIdle = coordsToMove;
  coordsToIdle[Z] += IdleAddZ;
  myCobot.writeCoords(coordsToIdle, speed);
  printCoords();
}

void setup() {
  myCobot.setup();
  myCobot.powerOn();
  initAngles();

  Serial.begin(9600); // USB Serial. FYI, Cobot uses Serial1 on Mega board.
}

void loop() {
  setColorIfMoving();
  if (Serial.available()) {
    serialInput = Serial.parseInt();
    Serial.print("(Serial) " + String(serialInput) + " / ");

    if(serialInput==-1){
      setCoords(&coords_0);
    }
    else if(serialInput==-2){
      setCoords(&coords_100);
      coords_100['Y'] = coords_0['Y'];
    }
    else if (0 <= serialInput && serialInput <=100){
      move(serialInput);
    }
    else{
      Serial.print("out of range");
    }
    Serial.println();
  }
}
