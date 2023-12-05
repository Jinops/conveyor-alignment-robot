import serial
import cv2
import time
import math
import algo
import os
from request import get_model_result
interval_sec = 1

try:
  arduino = serial.Serial(
    port='/dev/tty.usbmodem11401',
    baudrate=9600,
    timeout=.1
    )
except:
  print('!arduino serial connection failed!')
  print(os.system('ls /dev/tty.*'))

def get_image():
  cam = cv2.VideoCapture(1)
  ret, img = cam.read()
  img = cv2.imencode('.jpg', img)[1]
  return img

def get_image_t(file_name): # for test
  img = cv2.imread('roboflow/train/images/'+file_name)
  return img

def get_distance(xy_list):
  distance = algo.get_distance(640, 640, xy_list)
  # num = 480
  return int(distance)

def get_distance_t(file_name): # for test
  file_name=file_name[:-4]+'.txt'
  with open('roboflow/train/labelTxt/'+file_name,'r') as data_file:
    for line in data_file:
        data = line.split()
  xy_list = []
  for i in range(8):
    xy_list.append(float(data[i]))
    print('get_distance', 640, 640, list(map(int, xy_list)))
  distance = algo.get_distance(640, 640, xy_list)
  # num = 480
  return int(distance)

def get_distance_100(distance, img_height):
  # TODO: over 100
  print('distance: ', distance)
  print('distance(100): ', str(math.floor((distance/img_height*100))))
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

def main():
  mode = input('Select mode - (Enter) Automative (0) Manual : ')
  while mode==0:
    mode_manual()
  mode_main()

def mode_manual():
  data = input("Input Serial Data (q to close): ")
  if data=='q':
    pass
  result = serial_write(data)
  print(result)

def mode_validate_algo():
  file_idx = int(input('Input image idx: ')) # For test
  file_name = os.listdir('roboflow/train/images/')[file_idx]
  print(file_name)
  img = get_image_t(file_name)
  distance = get_distance_t(file_name)
  display(img, distance)
  distance_100 = get_distance_100(distance, img.shape[0])

def mode_main():
  img = get_image()
  model_result = get_model_result(img)
  if model_result is None:
    return 
  distance = get_distance(model_result[1])
  display(img, distance)
  distance_100 = get_distance_100(distance, img.shape[0])
  result = serial_write(distance_100)
  print(result)
  time.sleep(interval_sec)

# while True:
#   # mode_manual()
#   mode_main()
#   # mode_validate_algo()

mode_main()