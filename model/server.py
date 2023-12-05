from fastapi import FastAPI, UploadFile, File
import uvicorn
import shutil
import os
import yolov5_obb.detect as model

app = FastAPI()
## test

@app.get("/")
async def main():
  return "OK"

@app.post("/predict")
async def add_staff(file: UploadFile=File(..., media_type='image/jpeg')):
  with open(file.filename, 'wb') as f:
    file.file.seek(0)
    shutil.copyfileobj(file.file, f)

  # current_dir=os.path.dirname(os.path.realpath(__file__))
  current_dir = './'

  weights=os.path.join(current_dir, 'best.pt')
  source=os.path.join(current_dir, file.filename)

  result = model.run(
  weights=weights,
  source=source,
  conf_thres=0.01,
  imgsz=(640,640),
  device=0,
  agnostic_nms=True,
  return_result=True,
  # classes=0
  )
  
  return {"boxes": result}

uvicorn.run(app, host="0.0.0.0", port=8000)
