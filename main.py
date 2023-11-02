import serial
import time

arduino = serial.Serial(
  port='/dev/tty.usbmodem1401',
  baudrate=9600,
  timeout=.1
  )

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.1)
    data = arduino.readline()
    return data

while True:
    num = input("Enter a number: ")
    value = write_read(num)
    print(value)

