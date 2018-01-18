class GuiSetupConstants(object):
    def __init__(self):
        self.TITLE = "SolarBytes Control Panel"
        self.DIMENSIONS = "400x400"
        self.BACKGROUND_COLOR = "#fdb603"
        self.HEADER_FONT_SETTINGS = ('Helvetica', '16', 'bold')
        self.BODY_FONT_SETTINGS = ('Helvetica', '12')
        self.SUPPLICANT_PATH = "/etc/wpa_supplicant/wpa_supplicant.conf"

    @property
    def TITLE(self):
        return self.__TITLE

    @TITLE.setter
    def TITLE(self, TITLE):
        self.__TITLE = "SolarBytes Control Panel"

    @property
    def DIMENSIONS(self):
        return self.__DIMENSIONS

    @DIMENSIONS.setter
    def DIMENSIONS(self, DIMENSIONS):
        self.__DIMENSIONS = "400x400"

    @property
    def BACKGROUND_COLOR(self):
        return self.__BACKGROUND_COLOR

    @BACKGROUND_COLOR.setter
    def BACKGROUND_COLOR(self, BACKGROUND_COLOR):
        self.__BACKGROUND_COLOR = "#fdb603"

    @property
    def HEADER_FONT_SETTINGS(self):
        return self.__HEADER_FONT_SETTINGS

    @HEADER_FONT_SETTINGS.setter
    def HEADER_FONT_SETTINGS(self, HEADER_FONT_SETTINGS):
        self.__HEADER_FONT_SETTINGS = ('Helvetica', '16', 'bold')

    @property
    def BODY_FONT_SETTINGS(self):
        return self.__BODY_FONT_SETTINGS

    @BODY_FONT_SETTINGS.setter
    def BODY_FONT_SETTINGS(self, BODY_FONT_SETTINGS):
        self.__BODY_FONT_SETTINGS = ('Helvetica', '12')

    @property
    def SUPPLICANT_PATH(self):
        return self.__SUPPLICANT_PATH

    @SUPPLICANT_PATH.setter
    def SUPPLICANT_PATH(self, SUPPLICANT_PATH):
        self.__SUPPLICANT_PATH = "/etc/wpa_supplicant/wpa_supplicant.conf"
    
