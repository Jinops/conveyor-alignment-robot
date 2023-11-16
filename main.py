import serial
import cv2
import time
import math

interval_sec = 1

arduino = serial.Serial(
  port='/dev/tty.usbmodem1401',
  baudrate=9600,
  timeout=.1
  )

def get_image():
  cam = cv2.VideoCapture(1)
  ret, img = cam.read()
  # img = cv2.imread('./img_sample.jpeg')
  # cv2.imwrite('./test.jpg', img)

  return img

def get_distance():
  # get model's result from img
  num = int(input("Enter a number: ")) # Test
  # num = 480
  return num

def get_distance_100(distance, img_height):
  print(str(math.floor((distance/img_height*100))))
  return str(math.floor((distance/img_height*100)))
             
def serial_write(x):
  arduino.write(bytes(x, 'utf-8'))
  time.sleep(1) # Because async
  data = arduino.readline()
  return data

def display(img, distance):
  height = img.shape[0]
  width = img.shape[1]
  img = cv2.line(img, (width//2, height), (width//2, height-distance), (0,0,255), 10)
  cv2.imshow('window', img)
  cv2.waitKey(1) & 0xFF == ord('0')

####

mode = input('Select mode - (Enter) Automative (0) Manual : ')

while mode==2:
  data = input("Input Serial Data (q to close): ")
  if data=='q':
    break
  serial_write(data)

while True:
  img = get_image()
  distance = get_distance()
  display(img, distance)
  distance_100 = get_distance_100(distance, img.shape[0])
  result = serial_write(distance_100)
  print(result)
  time.sleep(interval_sec)
