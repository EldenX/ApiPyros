from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os
import base64
# from car_make_model_classifier_yolo3 import process_image

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pyros.site"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Pyros API is running"}

@app.get("/test")
def test_endpoint():
    return {"message": "Test endpoint working"}

@app.post("/procesar-imagen/")
def procesar_imagen(file: UploadFile = File(...)):
    return {"message": "Endpoint working, but processing disabled for debug"}
    # input_path = os.path.join(UPLOAD_DIR, file.filename)
    # output_path = os.path.join(OUTPUT_DIR, f"processed_{file.filename}")
    # with open(input_path, "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)
    # try:
    #     result = process_image(input_path, output_path)
    #     # Leer la imagen procesada y convertirla a base64
    #     with open(result['output_image_path'], "rb") as img_file:
    #         img_bytes = img_file.read()
    #         img_b64 = base64.b64encode(img_bytes).decode('utf-8')
    #     return JSONResponse({
    #         "image_b64": img_b64,
    #         "car_info": result['car_info']
    #     })
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e)) 
=======
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os
import base64
from car_make_model_classifier_yolo3 import process_image

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pyros.site"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Pyros API is running"}

@app.post("/procesar-imagen/")
def procesar_imagen(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_DIR, file.filename)
    output_path = os.path.join(OUTPUT_DIR, f"processed_{file.filename}")
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        result = process_image(input_path, output_path)
        # Leer la imagen procesada y convertirla a base64
        with open(result['output_image_path'], "rb") as img_file:
            img_bytes = img_file.read()
            img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        return JSONResponse({
            "image_b64": img_b64,
            "car_info": result['car_info']
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
>>>>>>> fb0ea5fde6937f66d5b654a46c946eea92c611d4
