from flask import Flask, request, render_template, jsonify
from query import getResponse
import pyttsx3
from jarvisMain import *
from flask_cors import CORS
import sqlite3
from array import array
import pymongo
import json
from bson import json_util

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["jarvis-chat"]
mycol = mydb["chats"]

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=["GET", "POST"])
def sendData():
    if request.method == "POST":
        print("Getting post request")  
        message = request.data
        print(message)
        message = message.decode()
        message = message.lower()
        response = getResponse(message)
        # insertMessage(message,'me')
        # insertMessage(response,'bot')
        mydict = { "message": message, "sendby": 'me' }
        x = mycol.insert_one(mydict)
        mydict = { "message": response, "sendby": 'bot' }
        x = mycol.insert_one(mydict)
        print(f"getting response from getresponse {response}")
        return response

    if request.method =="GET":
        x = list(mycol.find({}))
        x = jsonify(json_util.dumps(x))
        print(x)
        print(type(x))
        # x = str(x)
        return x

    # print("After Send Data")
    # return "Hello from Ritu"

# def sendAllMessage():
#     conn = sqlite3.connect('message.db')
#     cursor = conn.cursor()
#     allMessage = cursor.execute('''SELECT * FROM MESSAGE''')
#     # conn.commit()
#     return allMessage

def insertMessage(message,sendby):
    conn = sqlite3.connect('message.db')
    cursor = conn.cursor()
    # cursor.execute("CREATE TABLE MESSAGE(message char(200), sendBy char(3));")
    cursor.execute('''INSERT INTO MESSAGE(message, sendby) VALUES(?,?)''',(message,sendby,))
    conn.commit()

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
  