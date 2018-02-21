from subprocess import Popen
import os

def startUpWebServer(WEB_APP_PATH):
    os.chdir(WEB_APP_PATH)
    global pid
    pid = Popen(['xterm', '-e', 'python app.py'])
    return pid

def killWebServer():
    pid.kill()

def createNgrokTunnel(NGROK_PATH):
    os.chdir(NGROK_PATH)
    os.system("./ngrok http 5000")
