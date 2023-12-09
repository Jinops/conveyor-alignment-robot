from fastapi import FastAPI, UploadFile, File
import uvicorn
import shutil
import os
import sys
from datetime import datetime
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..', 'model'))
import yolov5_obb.detect as model
datetime
app = FastAPI()
width = 640
height = 640

@app.get("/")
async def main():
  return "OK"

@app.post("/predict")
async def predict(file: UploadFile=File(..., media_type='image/jpeg')):
  time_now = str(datetime.timestamp(datetime.now()))
  image_dir = os.path.join(current_dir, 'images', time_now)
  os.makedirs(image_dir)
  
  with open(os.path.join(image_dir, file.filename), 'wb') as f:
    file.file.seek(0)
    shutil.copyfileobj(file.file, f)

  weights=os.path.join(current_dir, 'best.pt')
  source=os.path.join(image_dir, file.filename)
  project=os.path.join(image_dir, 'output')

  result = model.run(
  weights=weights,
  source=source,
  conf_thres=0.01,
  imgsz=(height, width),
  device=0,
  agnostic_nms=True,
  return_result=True,
  project=project,
  nosave=False,
  name='.',
  # classes=0
  )
  
  return {
    "boxes": result,
    "width": width,
    "height": height,
    }

if __name__ == '__main__':
 uvicorn.run(app, host="0.0.0.0", port=8000)
