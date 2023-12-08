import requests
import numpy as np
import cv2
from dotenv import load_dotenv
import os 

host=os.environ.get('host')

def get_model_result(img):
  global host
  img_bytes = np.array(img).tobytes()
  files = {'file': ('predict.jpg', img_bytes, 'image/jpeg')}

  res = requests.post(url=f'{host}/predict', files=files).json()
  print('response: ', res)
  return get_best_result(res['boxes'])

def get_best_result(boxes):
  best_box = None
  for box in boxes:
    # (class, [x1,y1,x2,y2,x3,y3,x4,y4], conf)
    if best_box is None or box[2] > best_box[2]:
      best_box = box
  return best_box

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    ret, img = cam.read()
    img = cv2.imencode('.jpg', img)[1]
    print(get_model_result(img))
