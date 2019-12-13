#   Emerging Tech Assessment (Digit Recogniser)
#   Neil Kyne

#   Run with: env FLASK_APP=webApp.py flask run

#   Adapted from: https://palletsprojects.com/p/flask/
#   cv2 usage adapted from https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
 
import flask as fl  #   For creating the web application
import base64   #   For decoding images
from cv2 import cv2  #   For resizing image
from keras.models import load_model, Sequential    #   For loading the model
import numpy as np  #   For performing higher level math functions
from PIL import Image, ImageOps

#   Percent of original image to scale to. (5% of 400 = 20)
    # scale_percent = 5
    # width = int(originalImage.shape[1] * scale_percent / 100)
    # height = int(originalImage.shape[0] * scale_percent / 100)

model = load_model('MyModel3.h5')

imageWidth = 28
imageHeight = 28
dim = (imageWidth, imageHeight)

#   Create the flask web application
app = fl.Flask(__name__)

@app.route('/')
def hello():
    return app.send_static_file('DigitRecogniser.html')



@app.route('/uploadimage', methods = ['GET', 'POST'])
def uploadimage():
    #   Get the image from the request
    encodedImage = fl.request.values.get("theImage", "")

    #Decode the string to an image starting at the 22nd index of the
    decodedImage = base64.b64decode(encodedImage[22:])

    #   Save the image
    with open ("encodedImage.png", "wb") as f:
        f.write(decodedImage)
    
    #   Open the image from the request as originalImage
    originalImage = Image.open("encodedImage.png")

    #   Resize it to dimensions specified above. Apply antialias to 'smooth' out the edges
    resizedImage = ImageOps.fit(originalImage, dim, Image.ANTIALIAS)
    
    #   Save it locally
    resizedImage.save("resizedImage.png", quality=100, optimize=True)

    #   Reopen
    resizedImage = cv2.imread('resizedImage.png')

    # Set the image to gray scale
    grayScaleImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
    # resizedImage = Image.open(BytesIO(decodedImage)).convert('L')

    # pass the grayscale image into an array
    imageArray = np.array(grayScaleImage)

    # Have tried giving it 3 dimeniosnal shape and changing model also. Stll gives back same value.
    imageArray = imageArray.reshape(-1,784)
    # imageArray = imageArray.reshape(1, 28, 28)

    print("Image array shape: ") 
    print(imageArray.shape)

    #print("Image array: ") 
    #print(imageArray[0][0})

    #flattened = imageArray.flatten()
    #print("flattened array: ") 
    #print(flattened.shape)

    #   call model.predict on the image array
    setPrediction = model.predict([imageArray])
    print(setPrediction)    #   Always gives back same values!!!

    #   If its always giving the model the same values is the image being handled properly??

    #   argmax basically finds the maximum probability by index
    getPrediction = np.array(setPrediction[0])
    predictedNumber = str(np.argmax(getPrediction))
    print("Prediction: " + predictedNumber)  #   Always same
 
    return predictedNumber


