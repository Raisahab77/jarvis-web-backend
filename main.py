from flask import Flask, request, render_template, jsonify
from query import getResponse
import pyttsx3
from jarvisMain import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=["GET", "POST"])
def sendData():
    if request.method == "POST":
        print("Getting post request")
        print(request.data)
        message = request.data
        message = message.decode()
        response = getResponse(message)
        print(f"getting response from getresponse {response}")
        return response

    print("After Send Data")
    return "Hello from jarvis"


    #               ___
    #              (. .)
    #             |.   .|
    #             |.   .|
    #             |.   .|
    #             |.   .| 
    #             |.   .|
    #             |.   .|  _____    ____
    #      ____   |.   .|  |.  .|  /  .|
    #     /.   |. |.   .|  |.  .| |.  .|
    #     |.    |.|.   .|  |.  .| |.   /
    #     \.    |.|.   .| /.   .|     ./
    #      \.                        ./
    #       \.                      ./
    #        \.                    ./
    #         \.                  ./
    #          \.                ./

     

if __name__ == '__main__':
    app.run(debug = True)
  