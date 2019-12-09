#   Emerging Tech Assessment (Digit Recogniser)
#   Neil Kyne

#   Run with: env FLASK_APP=webApp.py flask run

#   Adapted from: https://palletsprojects.com/p/flask/
#   cv2 usage adapted from https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
 
import flask as fl  #   For creating the web application
import base64   #   For decoding images
#from cv2 import cv2  #   For resizing image
from keras.models import load_model, Sequential    #   For loading the model
import numpy as np  #   For performing higher level math functions
from PIL import Image, ImageOps

#   Percent of original image to scale to. (5% of 400 = 20)
    # scale_percent = 5
    # width = int(originalImage.shape[1] * scale_percent / 100)
    # height = int(originalImage.shape[0] * scale_percent / 100)

model = load_model('MyModel11.h5')

imageWidth = 28
imageHeight = 28
dim = (imageWidth, imageHeight)

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
    
    #   Open the image from the request as originalImage
    originalImage = Image.open("theImage.png")

    #   Resize it
    resizedImage = ImageOps.fit(originalImage, dim, Image.ANTIALIAS)

    #   Confirm the dimensions of the resized image
    w1, h1 = resizedImage.size
    print(w1, h1)
    
    #   Save it locally
    resizedImage.save("resizedImage.png", quality=100, optimize=True)

    #   Convert to grayscale and then convert that to an array
    grayscaleImage = ImageOps.grayscale(resizedImage)
    grayscaleArray = np.array(grayscaleImage)
    grayscaleArray.shape    #   Gives (28, 28)

    grayscaleArray = grayscaleArray.reshape(1, 28, 28)
    
    #   flattened = grayscaleArray.flatten()
    #   setPrediction = model.predict(flattened)

    setPrediction = model.predict([grayscaleArray])
    print(setPrediction)    #   Always gives back same values
    getPrediction = np.array(setPrediction[0])

    #   argmax basically finds the maximum probability by index
    predictedNumber = str(np.argmax(getPrediction))
    print(predictedNumber)  #   Always same

    #   Consider removing flattened layer from model and just have dense with input_dim=784
 
    return predictedNumber




@app.route('/')
def hello():
    return app.send_static_file('DigitRecogniser.html')