# Recognition of Hand Written digits
**Neil Kyne**

### About the project
Recognition of the MNIST dataset is considered to be a great introduction to machie learning and is dubbed the 'Hello World' of the field.

This repository contains my submission for the module Emerging Technologies in year 4. The repository contains a jupyter notebook where I go through how to load the MNIST dataset, create a sequential neural network model, compile and train our model and finally test the model, among other things.

It also contains a web application running on a flask server. The server interacts with the model we created in the jupyter notebook and sends/receives data to and from the web appication.

### Environment setup
See the requirements.txt file in order to see the full list of packages and their versions I had installed while develooping the project.

### Technologies used
This project was mainly done in Python as well as some Javascript, HTML and CSS.

Some modules and frameworks used include: 
* Flask
Flask is a web application framework written in Python. It provides you with tools, libraries and technologies that allow you to build a web application.
    * JQuery
        JQuery is a tool which provides a set of AJAX methods to develop web application. Mainly HTTP (request) methods.
    * Keras
        Keras is an open-source neural-network library written in Python. It sits top of TensorFlow. It's designed to enable quick and easy development with deep neural networks.
    * PIL
        (Previously Python Imaging Library) Pillow provides support for opening, manipulating, and saving many different image file formats.



### How to run
Clone or download the project to your machine. to clone the project use the command: "git clone https://github.com/NeilK-94/Emerging-Tech-Assessment.git"

From this directory you must run the below command on the command line to start up the flask server.
```python
$ env FLASK_APP=webApp.py flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
As stated above, the server will run on "http://127.0.0.1:5000/". Once there you will see a very basic webpage with a canvas. Draw a digit between 0 and 9 on this canvas then click the submit button.

This will send the contents of the canvas to the flask server using JQuery. From there, we decode the image from a base64 string to an image. (If you want to see what the base64 image looked like open up the developer's console in your editor!) We then resize the image received from the canvas to the correct size for our model (28x28).

Finally we convert the image to grayscale and then into an array, after this it is ready to be given to our model for a prediction.

The models prediction is sent back to the web application and displayed on the screen as well as the console.

Adapted from: https://palletsprojects.com/p/flask/

