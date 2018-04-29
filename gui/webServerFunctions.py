from subprocess import Popen
import os

'''
Utility functions to start web server and build ngrok tunnel to connect the pi to the open web
'''

def startUpWebServer(WEB_APP_PATH, NGROK_PATH):
    os.chdir(WEB_APP_PATH)
    global pid
    pid = Popen(['xterm', '-e', 'python app.py'])
    createNgrokTunnel(NGROK_PATH)
    return pid

def killWebServer():
    pid.kill()

def createNgrokTunnel(NGROK_PATH):
    os.chdir(NGROK_PATH)
    os.system("./ngrok http 5000")
