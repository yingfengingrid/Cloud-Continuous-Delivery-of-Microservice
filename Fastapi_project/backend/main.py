import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import pandas as pd
import statsmodels
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import pickle


app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}

@app.post("/model/")
async def process_data(file: UploadFile = File(...)):
    # 
    data=pd.read_csv(file.file)
    with open("temp.txt",'wb') as f:
        pickle.dump(data,f)
   
    
    return {"name":"temp.txt"}


if __name__ == "__main__":
    uvicorn.run(app="main:app")