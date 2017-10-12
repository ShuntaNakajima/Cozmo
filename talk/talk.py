import cozmo
import sys
import urllib
import json
import requests
from io import StringIO
import re
import pyrebase
import time
from cozmo.util import degrees, distance_mm, speed_mmps
config = {
  "apiKey": "AIzaSyDqmJ2l6ojiTpJo5NQr0z7Lsmy2x5ONX4A",
  "authDomain": "cozmo-f3c99.firebaseapp.com",
  "databaseURL": "https://cozmo-f3c99.firebaseio.com",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
say_text = ""
input_text = ""
saved_text = ""
def say_textadd(say_text: str,text: str):
    if text == "あ":
        say_text = say_text + " ah"
    if text == "い":
        say_text = say_text + " ee"
    if text == "う":
        say_text = say_text + " uh"
    if text == "え":	
        say_text = say_text + " eh"
    if text == "お":
        say_text = say_text + " oh"
    if text == "か":
        say_text = say_text + " car"
    if text == "き":
        say_text = say_text + " cki"
    if text == "く":
        say_text = say_text + " cuh"
    if text == "け":
        say_text = say_text + " cae"
    if text == "こ":
        say_text = say_text + " coh"
    if text == "さ":
        say_text = say_text + " sar"
    if text == "し":
        say_text = say_text + " c"
    if text == "す":
        say_text = say_text + " thu"
    if text == "せ":
        say_text = say_text + " saye"
    if text == "そ":
        say_text = say_text + " sho"
    if text == "た":
        say_text = say_text + " tar"
    if text == "ち":
        say_text = say_text + " chee"
    if text == "つ":
        say_text = say_text + " tue"
    if text == "て":
        say_text = say_text + " teh"
    if text == "と":
        say_text = say_text + " toh"
    if text == "な":
        say_text = say_text + " ner"
    if text == "に":
        say_text = say_text + " nae"
    if text == "ぬ":
        say_text = say_text + " nue"
    if text == "ね":
        say_text = say_text + " neh"
    if text == "の":
        say_text = say_text + " noh"
    if text == "は":
        say_text = say_text + " hah"
    if text == "ひ":
        say_text = say_text + " hee"
    if text == "ふ":
        say_text = say_text + " who"
    if text == "へ":
        say_text = say_text + " heh"
    if text == "ほ":
        say_text = say_text + " hoh"
    if text == "ま":
        say_text = say_text + " mot"
    if text == "み":
        say_text = say_text + " me"
    if text == "む":
        say_text = say_text + " moo"
    if text == "め":
        say_text = say_text + " meh"
    if text == "も":
        say_text = say_text + " moh"
    if text == "や":
        say_text = say_text + " yea"
    if text == "ゆ":
        say_text = say_text + " you"
    if text == "よ":
        say_text = say_text + " yoo"
    if text == "ら":
        say_text = say_text + " rar"
    if text == "り":
        say_text = say_text + " ree"
    if text == "る":
        say_text = say_text + " rhu"
    if text == "れ":
        say_text = say_text + " reh"
    if text == "ろ":
        say_text = say_text + " rho"
    if text == "わ":
        say_text = say_text + " woa"
    if text == "を":
        say_text = say_text + " oh"
    if text == "ん":
        say_text = say_text + " m"   
    if text == "が":
        say_text = say_text + " gah"
    if text == "ぎ":
        say_text = say_text + " git"
    if text == "ぐ":
        say_text = say_text + " goh"
    if text == "げ":
        say_text = say_text + " geh"
    if text == "ご":
        say_text = say_text + " gho"
    if text == "ざ":
        say_text = say_text + " zar"
    if text == "じ":
        say_text = say_text + " g"
    if text == "づ":
        say_text = say_text + " zoo"
    if text == "ぜ":
        say_text = say_text + " zeh"
    if text == "ぞ":
        say_text = say_text + " zoh"
    if text == "だ":
        say_text = say_text + " dar"
    if text == "ぢ":
        say_text = say_text + " g"
    if text == "づ":
        say_text = say_text + " zoo"
    if text == "で":
        say_text = say_text + " deh"
    if text == "ど":
        say_text = say_text + " doh"
    if text == "ば":
        say_text = say_text + " bar"
    if text == "び":
        say_text = say_text + " bee"
    if text == "ぶ":
        say_text = say_text + " boh"
    if text == "べ":
        say_text = say_text + " beh"
    if text == "ぼ":
        say_text = say_text + " boh"
    if text == "ぱ":
        say_text = say_text + " par"
    if text == "ぴ":
        say_text = say_text + " pee"
    if text == "ぷ":
        say_text = say_text + " poo"
    if text == "ぺ":
        say_text = say_text + " peh"
    if text == "ぽ":
        say_text = say_text + " poh"
    if text == "、":
        say_text = say_text + " ."
    if text == "。":
        say_text = say_text + " ,"
    else:
        say_text = say_text + " "
    return say_text

def stream_handler(message):
    global saved_text
    global input_text
    if saved_text != message["data"]:
        print("user -->" + message["data"])
        input_text = message["data"]
        saved_text = input_text
def cozmo_program(robot: cozmo.robot.Robot):
    global input_text
    global saved_text
    saved_text = db.child("message").remove()
    time.sleep(1)
    stats = "false"
    while stats == "false":
        global my_stream
        my_stream = db.child("message").stream(stream_handler)
        while input_text == "":
            time.sleep(.5)
        my_stream.close
        if input_text == "終了":
            break
        botparams = {
        "appkey": "",
        "text": input_text,
        }
        botp = urllib.parse.urlencode(botparams)
        boturl = "https://www.cotogoto.ai/webapi/noby.json?" + botp
        with urllib.request.urlopen(boturl) as res:
            html = res.read().decode("utf-8")
            global data
            data = json.loads(html)
        print(data["text"])
        if data["commandId"] == "right":
        	robot.turn_in_place(degrees(-90)).wait_for_completed()
        	input_text = ""
        elif data["commandId"] == "left":
        	robot.turn_in_place(degrees(90)).wait_for_completed()
        	input_text = ""
        elif data["commandId"] == "forward":
        	robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
        	input_text = ""
        else:
            url = 'https://labs.goo.ne.jp/api/hiragana?'
            headers = {'content-type': 'application/json'}
            params = {"app_id":"","sentence":data["text"],"output_type":"hiragana"}
            r = requests.post(url, data=json.dumps(params), headers=headers)
            io = StringIO(r.text)
            json_data = json.load(io)
            say_text = ""
            for i in json_data["converted"]:
               say_text = say_textadd(say_text,i)
            print (json_data["converted"])
            print (say_text)
            robot.say_text(say_text).wait_for_completed()
            input_text = ""

cozmo.run_program(cozmo_program)