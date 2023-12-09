import serial
import cv2
import time
import math
import algo
import os
import request

interval_sec = 1
width=640
height=640

try:
  arduino = serial.Serial(
    port='/dev/tty.usbmodem1301',
    baudrate=9600,
    timeout=.1
    )
except:
  print('!arduino serial connection failed!')
  print(os.system('ls /dev/tty.*'))

def get_image():
  cam = cv2.VideoCapture(0)
  ret, img = cam.read()
  # img = cv2.imread('model/test.jpg')
  crop_image = get_crop_image(img)
  return crop_image

def get_crop_image(img):
  center_y = img.shape[0] // 2
  center_x = img.shape[1] // 2

  start_y = center_y - height // 2
  end_y = center_y + height // 2
  start_x = center_x - width // 2
  end_x = center_x + width // 2

  return img[start_y:end_y, start_x:end_x]

def get_distance(xy_list):
  distance = algo.get_distance(width, height, xy_list)
  print('distance: ', distance)
  return int(distance)

def get_distance_100(distance, img_height):
  distance_100 = math.floor(distance/img_height*100)
  distance_100 = min(100, max(0, distance_100))
  print('distance(100): ', distance_100)
  return str(distance_100)
             
def serial_write(x):
  arduino.write(bytes(x, 'utf-8'))
  time.sleep(1) # Because async
  data = arduino.readline()
  return data

def display(img, distance):
  print("display")
  img = cv2.line(img, (width//2, height), (width//2, height-distance), (0,0,255), 10)
  cv2.imshow('window', img)
  cv2.waitKey(1) & 0xFF == ord('0')

def main():
  mode = input('Select mode - (Enter) Automative (0) Manual : ')
  print(mode)
  while mode=='0':
    mode = mode_manual()
  while True:
    mode_main()
    time.sleep(interval_sec)

def mode_manual():
  data = input("Input Serial Data (q to close): ")
  if data=='q':
    return None
  result = serial_write(data)
  print(result)
  return '0'

def mode_main():
  img = get_image()
  model_result = request.get_model_result(img)[0]
  if model_result is None:
    display(img, 0)
    return 
  distance = get_distance(model_result[1])
  display(img, distance)
  distance_100 = get_distance_100(distance, img.shape[0])
  result = serial_write(distance_100)
  time.sleep(1)
  print(result)

if __name__ == '__main__':
  main()
