import serial
import time
import cv2

interval_sec = 1

arduino = serial.Serial(
  port='/dev/tty.usbmodem1401',
  baudrate=9600,
  timeout=.1
  )

def get_image():
  # cam = cv2.VideoCapture(0)
  # ret, img = cam.read()
  # img = cv2.imread('./img_sample.jpeg')
  # return img
  return None

def get_distance(img):
  # get model's result from img
  num = input("Enter a number: ") # Test
  return num

def serial_write(x):
  arduino.write(bytes(x, 'utf-8'))
  time.sleep(1) # Because async
  data = arduino.readline()
  return data

while True:
  img = get_image()
  distance = get_distance(img)
  result = serial_write(distance)
  print(result)
  time.sleep(interval_sec)

