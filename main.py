from fastapi import FastAPI 
import requests
import os
import ImageReder
from fastapi.responses import PlainTextResponse, FileResponse

app = FastAPI()


@app.get("/realestate" , response_class=PlainTextResponse)
def realestate() : 

    with open("realestate.txt", "r", encoding="utf-8") as f:
        content = f.read()      
          
    return content




@app.get("/photos" , response_class=PlainTextResponse)
def photos():
    
    with open("realestate.txt", "r", encoding="utf-8") as f:
        content = f.read()  
              
    return content


@app.get("/image")
def image(name : str):
    
    if os.path.exists("photos"):
        return FileResponse(f"photos/{name}" ,  media_type="image/jpg")
    else : 
        ImageReder.GetImage()