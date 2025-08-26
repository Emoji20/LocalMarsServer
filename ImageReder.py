import requests 
import os 
def GetImage():
    response =  requests.get("https://android-kotlin-fun-mars-server.appspot.com/photos").json()

    counter = 0 

    folder = "photos"

    os.makedirs(folder, exist_ok=True)


    for i in response : 
        
        filepath = os.path.join(folder, f"Image{counter+1}.jpg")
        
        image = requests.get(response[counter]["img_src"])
        
        with open(filepath, "wb") as file:
            file.write(image.content)
            
        print(f"StateCode : {image.status_code}")
        counter += 1 
    

