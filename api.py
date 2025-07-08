from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os
import base64
from car_make_model_classifier_yolo3 import process_image
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



@app.get("/")
def health_check():
    return {"status": "ok", "message": "Pyros API is running"} 
    
@app.get("/debug-files")
def debug_files():
    import os
    files = []
    for root, dirs, filenames in os.walk("."):
        for filename in filenames:
            path = os.path.join(root, filename)
            files.append({"file": path, "size": os.path.getsize(path)})
    return files
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://pyros.site"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/procesar-imagen/")
def procesar_imagen(file: UploadFile = File(...)):
    input_path = os.path.join(UPLOAD_DIR, file.filename)
    output_path = os.path.join(OUTPUT_DIR, f"processed_{file.filename}")
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        result = process_image(input_path, output_path)
        with open(result['output_image_path'], "rb") as img_file:
            img_bytes = img_file.read()
            img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        return JSONResponse({
            "image_b64": img_b64,
            "car_info": result['car_info']
        })
    except Exception as e:
        import traceback
        traceback.print_exc()  # <--- Esto imprime el error real en los logs
        raise HTTPException(status_code=500, detail=str(e))

