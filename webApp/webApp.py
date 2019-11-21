#    Run with: env FLASK_APP=webApp.py flask run

#    Adapted from: https://palletsprojects.com/p/flask/
#    cv2 usage adapted from https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
 
import flask as fl  #   For creating the web application
import base64   #   For decoding images
from cv2 import cv2  #   For resizing image
from keras.models import load_model    #   For loading the model
import numpy as np  #   For performing higher level math functions
from PIL import Image, ImageOps

model = load_model('MyModel.h5')

#   Create the flask web application
app = fl.Flask(__name__)

@app.route('/uploadimage', methods = ['GET', 'POST'])
def uploadimage():
    #   Get the image from the request
    theImage = fl.request.values.get("theImage", "")

    #Decode the string to an image
    decodedimg = base64.b64decode(theImage[22:])

    #   Save the image
    with open ("theImage.png", "wb") as f:
        f.write(decodedimg)
    
    originalImage = cv2.imread("theImage.png")

    #   Percent of original image to scale to. (5% of 400 = 20)
    scale_percent = 5
    width = int(originalImage.shape[1] * scale_percent / 100)
    height = int(originalImage.shape[0] * scale_percent / 100)
    dim = (width, height)

    resizedImage = cv2.resize(originalImage, dim, interpolation = cv2.INTER_AREA)
    #grayImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
    #grayArray = (np.array(grayImage).reshape(1, 28, 28, 1))

    #   Save the resized image
    cv2.imwrite("C:/Users/neilk/Desktop/Emerging-Tech-Assessment/webApp/resizedImage.png", resizedImage)
    

    print(resizedImage.shape)
    
    return {"message": theImage}





@app.route('/')
def hello():
    return app.send_static_file('DigitRecogniser.html')