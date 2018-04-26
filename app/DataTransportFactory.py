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

    '''
    DEPRECATED

    Transports test data to local mounted USB
    '''
    def transportToUSB(self,
                       ratio=0,
                       cellNumber=0,
                       date=0,
                       time=0,
                       temperature=0,
                       humidity=0):
        try:
            with open(self.constants.CSV_PATH, 'a') as file:
                solarBytesWriter = csv.writer(file)
                solarBytesWriter.writerow([ratio,self.constants.PIN_TO_CELL_MAP[cellNumber],time,temperature,humidity])
        except:
            print('Unable to write to usb')

    '''
    Transports test data to hidden csv for backup
    '''
    def transportToBufferFile(self,
                              ratio=0,
                              cellNumber=0,
                              date=0,
                              time=0,
                              temperature=0,
                              humidity=0):
        try:
            with open(self.constants.BUFFER_PATH, 'a') as backupFile:
                backupFileWriter = csv.writer(backupFile)
                backupFileWriter.writerow([ratio,self.constants.PIN_TO_CELL_MAP[cellNumber],time,temperature,humidity])
        except:
            print('Unable to write to buffer file')

    '''
    Transports test data to sql database
    '''
    def transportToDB(self,
                      ratio=0,
                      cellNumber=0,
                      date="0",
                      time="0",
                      temperature=0,
                      humidity=0):
        try:
            db = sql.connect(self.constants.SQL_DATABASE)
            sqlCursor = db.cursor()
            insertString = "INSERT INTO solarTests VALUES('{}','{}',{},{},{},{})"
            formatted = insertString.format(date,time,cellNumber,ratio,temperature,humidity)
            sqlCursor.execute(formatted)
            db.commit()
            db.close()
        except Exception as error:
            raise(error)

    def transportFromDB(self,
                        limit):
        try:
            db = self.getDatabase()
            sqlCursor = self.getDatabaseTunnel()

            if(limit >= 0):
                queryString = 'SELECT * FROM solarTests LIMIT ' + str(limit) + ';'
            else:
                queryString = 'SELECT * FROM solarTests;'

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
            colArray = ["testDate", "testTime", "cell", "ratio", "temp", "humidity"]
            sqlCursor = self.getDatabaseTunnel()

            queryString = 'SELECT * FROM solarTests'
            results = list()
            for row in sqlCursor.execute(queryString):
                results.append(row)

            if(operation == "AVG"):
                result = self.getAverage(results, colArray.index(column))

            if(operation == "MIN"):
                result = self.getMinimum(results, colArray.index(column))

            if(operation == "MAX"):
                result = self.getMaximum(results, colArray.index(column))

            if(operation == "SUM"):
                result = self.getSum(results, colArray.index(column))

            print(result)
            db.close()
            return str(result)
        except Exception as error:
            raise error

    def transportFromDBFilterThenAggregate(self,
                                           filtCol,
                                           filtOp,
                                           filtVal,
                                           filtLimit,
                                           aggCol,
                                           aggOp):
        try:
            colArray = ["TestDate", "TestTime", "Cell", "Ratio", "Temp", "Humidity"]
            filteredResults = self.transportFromDBFiltered(filtCol,filtOp,filtVal,filtLimit)
            if(aggOp == "AVG"):
                result = self.getAverage(filteredResults, colArray.index(aggCol))
            if(aggOp == "MIN"):
                result = self.getMinimum(filteredResults, colArray.index(aggCol))
            if(aggOp == "MAX"):
                result = self.getMaximum(filteredResults, colArray.index(aggCol))
            if(aggOp == "SUM"):
                result = self.getSum(filteredResults, colArray.index(aggCol))

            print(result)
            return str(result)
        except Exception as error:
            raise error

    def getTotalTestCount(self):
        try:
            sqlCursor = self.getDatabaseTunnel()
            rowCount = 0
            for row in sqlCursor.execute("SELECT * FROM solarTests"):
                rowCount = rowCount + 1
            return rowCount
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

    def getAverage(self, listRows, index):
        if(len(listRows) == 0):
            return 0

        sum = 0
        for row in listRows:
            sum = sum + row[index]

        average = sum/len(listRows)
        return average

    def getMinimum(self, listRows, index):
        numArray = list()
        for row in listRows:
            numArray.append(row[index])

        minimum = min(numArray)
        return minimum

    def getMaximum(self, listRows, index):
        numArray = list()
        for row in listRows:
            numArray.append(row[index])

        maximum = max(numArray)
        return maximum

    def getSum(self, listRows, index):
        sum = 0
        for row in listRows:
            sum = sum + row[index]

        return sum
