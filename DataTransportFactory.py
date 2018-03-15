import csv
import sqlite3 as sql
from TestingConstants import TestingConstants

'''

Object used to transport test data to peripheral databases and drives

'''
class DataTransportFactory(object):
    '''
    Instantiates an identifiable DataTransportFactory instance
    '''
    def __init__(self,
                 val):
        self.val = val
        self.constants = TestingConstants()
        self.operations = ['IS','IS_NOT','GREATER','LESS']
        self.rows = {'ratio':float,'cellNumber':int,'date':str,'time':float,'temperature':float,'humidity':float}

    '''
    Transports test data to local mounted USB
    '''
    def transportToUSB(self,
                       ratio=0,
                       cellNumber=0,
                       time=0,
                       temperature=0,
                       humidity=0):
        with open(self.constants.CSV_PATH, 'a') as file:
            solarBytesWriter = csv.writer(file)
            solarBytesWriter.writerow([ratio,self.constants.PIN_TO_CELL_MAP[cellNumber],time,temperature,humidity])

    '''
    Transports test data to hidden csv for backup
    '''
    def transportToBufferFile(self,
                              ratio=0,
                              cellNumber=0,
                              time=0,
                              temperature=0,
                              humidity=0):
        with open(self.constants.BUFFER_PATH, 'a') as backupFile:
            backupFileWriter = csv.writer(backupFile)
            backupFileWriter.writerow([ratio,self.constants.PIN_TO_CELL_MAP[cellNumber],time,temperature,humidity])

    '''
    Transports test data to sql database
    '''
    # TODO: ADD IN TYPE CHECKS AFTER FRONT END FINALIZED
    def transportToDB(self,
                      ratio=0,
                      cellNumber=0,
                      date=0,
                      time=0,
                      temperature=0,
                      humidity=0):
        try:
            db = self.getDatabase()
            sqlCursor = self.getDatabaseTunnel()
            
            test = [(date,time,cellNumber,ratio,temperature,humidity),]
            sqlCursor.executemany('INSERT INTO solarTests VALUES (?,?,?,?,?,?)',test)

            db.commit()
            db.close()
            return
        except Exception as error:
            raise error

    def transportFromDB(self,
                        limit):
        try:
            db = self.getDatabase()
            sqlCursor = self.getDatabaseTunnel()

            queryString = 'SELECT * FROM solarTests LIMIT ' + str(limit) + ';'
            print(queryString)
            results = list()
            for row in sqlCursor.execute(queryString):
                results.append(row)

            db.close()
            return results
        except Exception as error:
            raise error

    def transportFromDBFiltered(self,
                                column,
                                operation,
                                value,
                                limit):
        try:
            db = self.getDatabase()
            sqlCursor = self.getDatabaseTunnel()

            queryString = 'SELECT * FROM solarTests WHERE ' + str(column) + ' ' + str(operation) + ' ' + str(value) + ' LIMIT ' + str(limit) + ';'
            print(queryString)
            results = list()
            for row in sqlCursor.execute(queryString):
                results.append(row)

            db.close()
            return results
        except Exception as error:
            raise error

    def transportFromDBAggregated(self,
                                  column,
                                  operation):
        try:
            db = self.getDatabase()
            sqlCursor = self.getDatabaseTunnel()

            queryString = 'SELECT ' + str(operation) + '(' + str(column) + ') FROM solarTests'
            print(queryString)
            results = list()
            for row in sqlCursor.execute(queryString):
                results.append(row)

            db.close()
            return results
        except Exception as error:
            raise error

    def getDatabaseTunnel(self):
        try:
            db = self.getDatabase()
            sqlCursor = db.cursor()
            return sqlCursor
        except Exception as error:
            raise error

    def getDatabase(self):
        try:
            db = sql.connect(self.constants.SQL_DATABASE)
            return db
        except Exception as error:
            raise error
                        
                        
                        
