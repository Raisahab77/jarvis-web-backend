from flask import Flask, request, render_template, jsonify
from query import getResponse
import pyttsx3
from jarvisMain import *
from flask_cors import CORS
import sqlite3
from array import array
# import pymongo
import json
from bson import json_util

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["jarvis-chat"]
# mycol = mydb["chats"]

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=["GET", "POST"])
def sendData():
    if request.method == "POST":
        mimetype = request.mimetype
        print(mimetype)
        if mimetype == 'application/x-www-form-urlencoded':
            print("I am here")
            print(type(request.form.keys()))
            print(request.form.keys())
        elif mimetype == 'multipart/form-data':
            form = dict(request.form)
            print("************************** form *******************", form)
        elif mimetype == 'application/json':
            form = request.json
            print("************************** form *******************", form)
            query = form['query'];
            response = getResponse(query)

        else:
            form = request.data.decode()
            print("************************** form *******************", form)

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

def sendAllMessage():
    conn = sqlite3.connect('message.db')
    cursor = conn.cursor()
    allMessage = cursor.execute('''SELECT * FROM MESSAGE''')
    # conn.commit()
    return allMessage

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
  