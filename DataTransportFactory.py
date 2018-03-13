import csv
import sqlite3
from TestingConstants import TestingConstants

'''

Object used to transport test data to peripheral databases and drives

'''
class DataTransportFactory(object):
    '''
    Instantiates an identifiable DataTransportFactory instance
    '''
    def __init__(self,val):
        self.val = val
        self.constants = TestingConstants()

    '''
    Transports test data to local mounted USB
    '''
    def transportToUSB(self,ratio=0,cellNumber=0,time=0,temperature=0,humidity=0):
        with open(self.constants.CSV_PATH, 'a') as file:
            solarBytesWriter = csv.writer(file)
            solarBytesWriter.writerow([ratio,self.constants.PIN_TO_CELL_MAP[cellNumber],time,temperature,humidity])
            print("Data written to local USB")

    '''
    Transports test data to hidden csv for backup
    '''
    def transportToBufferFile(self,ratio=0,cellNumber=0,time=0,temperature=0,humidity=0):
        with open(self.constants.BUFFER_PATH, 'a') as backupFile:
            backupFileWriter = csv.writer(backupFile)
            backupFileWriter.writerow([ratio,self.constants.PIN_TO_CELL_MAP[cellNumber],time,temperature,humidity])

    '''
    Transports test data to cloud hosted MySQL instance
    '''
    def transportToDB(self,ratio=0,cellNumber=0,date=0,time=0,temperature=0,humidity=0):
        db = sqlite3.connect(self.constants.SQL_DATABASE)
        sqlCursor = db.cursor()

        test = [(date,time,cellNumber,ratio,temperature,humidity),]
        sqlCursor.executemany('INSERT INTO solarTests VALUES (?,?,?,?,?,?)',test)

        db.commit()
        db.close()
        return
