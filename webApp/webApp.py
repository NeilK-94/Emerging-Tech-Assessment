#    Run with: env FLASK_APP=webApp.py flask run
#    Adapted from: https://palletsprojects.com/p/flask/
 
#   For creating the web application
import flask as fl

#   For decoding images
import base64

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
    return {"message": theImage}

@app.route('/')
def hello():
    return app.send_static_file('DigitRecogniser.html')