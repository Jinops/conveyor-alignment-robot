from fastapi import FastAPI, UploadFile
import uvicorn
import shutil

app = FastAPI()
## test

@app.get("/")
async def main():
  return "OK"

@app.post("/predict")
async def add_staff(file: UploadFile):
  open(file.filename, 'wb')
      
  return {"message": f"Successfully uploaded {file.filename}"}
uvicorn.run(app, host="0.0.0.0", port=8000)
