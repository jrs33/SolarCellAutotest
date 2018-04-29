'''
Object used to centralize major immutable testing constants
'''

class TestingConstants(object):
	def __init__(self):
		self.PIN_TO_CELL_MAP = {12 : "1", 16 : "2", 20 : "3", 21 : "4", 6 : "5", 13 : "6", 19 : "7", 26 : "8"}
		self.EDS_TRIGGER_PIN = 22
		self.CSV_PATH = "/media/usb/solarbytes.csv"
		self.BUFFER_PATH = "/home/pi/Desktop/.sbBuffer.csv"
		self.SQL_DATABASE = "solarbytes.db"

	@property
	def PIN_TO_CELL_MAP(self):
		return self.__PIN_TO_CELL_MAP

	@PIN_TO_CELL_MAP.setter
	def PIN_TO_CELL_MAP(self, PIN_TO_CELL_MAP):
		self.__PIN_TO_CELL_MAP = {12 : "1", 16 : "2", 20 : "3", 21 : "4", 6 : "5", 13 : "6", 19 : "7", 26 : "8"}

	@property
	def EDS_TRIGGER_PIN(self):
		return self.__EDS_TRIGGER_PIN

	@EDS_TRIGGER_PIN.setter
	def EDS_TRIGGER_PIN(self, EDS_TRIGGER_PIN):
		self.__EDS_TRIGGER_PIN = 22

	@property 
	def CSV_PATH(self):
		return self.__CSV_PATH

	@CSV_PATH.setter
	def CSV_PATH(self, CSV_PATH):
		self.__CSV_PATH = "/media/usb/solarbytes.csv"

	@property
	def BUFFER_PATH(self):
		return self.__BUFFER_PATH

	@BUFFER_PATH.setter
	def BUFFER_PATH(self, BUFFER_PATH):
		self.__BUFFER_PATH = "/home/pi/Desktop/solarbytes.csv"

	@property
	def SQL_DATABASE(self):
		return "solarbytes.db"

	@SQL_DATABASE.setter
	def SQL_DATABASE(self, SQL_DATABASE):
		self.__SQL_DATABASE = "solarbytes.db"
