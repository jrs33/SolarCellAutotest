import csv

'''

Object used to transport test data to peripheral databases and drives

'''
class DataTransportFactory(object):
    '''
    Instantiates an identifiable DataTransportFactory instance
    '''
    def __init__(self,val):
        self.val = val

    '''
    Transports test data to local mounted USB
    '''
    def transportToUSB(self,ratio=0,cellNumber=0,time=0,temperature=0,humidity=0):


    '''
    Transports test data to cloud hosted MySQL instance
    '''
    def transportToCloud(self,ratio=0,cellNumber=0,time=0,temperature=0,humidity=0):
        
