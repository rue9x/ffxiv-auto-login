import pyautogui
import base64
import json
import time
import os
def load_config():    
    with open ("config.json",'r') as fin:
        config = json.load(fin)
    myid=config["username"]
    mypass=config["passBase64"]
    mypass = mypass.encode("ascii")
    mypass = base64.b64decode(mypass)
    mypass = mypass.decode("ascii")
    pathToGame = config["pathToGame"]
    if os.path.exists(pathToGame) == False:
        raise Exception (f"Couldn't locate FFXIV at {pathToGame}")
    return myid, mypass, pathToGame

def login(myid,mypass,pathToGame):
    
    window = None
    failcount = 0
    while window == None:
        try:
            window = pyautogui.getWindowsWithTitle('FFXIVLauncher')[0]
        except:
            window = None
            failcount = failcount+1
        time.sleep(1)
        if failcount == 5:
            os.system('start "" "' + pathToGame+ '"')
        if failcount > 100:
            raise Exception("Couldn't find FFXIVLauncher!")
    window.activate()

    idfield = None
    failcount = 0
    while idfield == None:
        time.sleep(1)
        try:
            idfield = pyautogui.locateOnScreen('id.png',confidence=0.9)
        except:
            idfield = None
            failcount = failcount+1
        if failcount == 10:
            raise Exception("Couldn't find FFXIV login ID box.")
            
    passfield = pyautogui.locateOnScreen('pass.png',confidence=0.9)
    loginbutton = pyautogui.locateOnScreen('login.png',confidence=0.9)
    if loginbutton == None:
        loginbutton = pyautogui.locateOnScreen('login2.png',confidence=0.9)
    idfield = pyautogui.center(idfield)
    passfield = pyautogui.center(passfield)
    loginbutton = pyautogui.center(loginbutton)
    pyautogui.leftClick(idfield.x,idfield.y)
    pyautogui.write(myid)
    pyautogui.leftClick(passfield.x,passfield.y)
    pyautogui.write(mypass)
    pyautogui.leftClick(loginbutton.x,loginbutton.y)
    playButton = None
    while (playButton == None):
        time.sleep(1)
        playButton = pyautogui.locateOnScreen('play.png',confidence=0.9)
    pyautogui.leftClick(playButton)

myid, mypass, pathToGame= load_config()
login(myid,mypass,pathToGame)