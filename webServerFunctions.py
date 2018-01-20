import os

def startUpWebServer(WEB_APP_PATH):
    os.chdir(WEB_APP_PATH)
    os.system('python app.py')
