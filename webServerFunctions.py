from subprocess import Popen
import os

def startUpWebServer(WEB_APP_PATH):
    os.chdir(WEB_APP_PATH)
    Popen(['xterm', '-e', 'python app.py'])
    return
