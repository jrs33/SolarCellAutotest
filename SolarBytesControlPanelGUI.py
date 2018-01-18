import tkinter as tk
import wifiFunctions as wf

class SolarBytesControlPanelApp:
    def __init__(self, window, constants):
        self.window = window
        self.constants = constants

        self.window.title(self.constants.TITLE)
        self.window.geometry(self.constants.DIMENSIONS)
        self.window.configure(background=self.constants.BACKGROUND_COLOR)

        '''
        Create all widgets and pack into window
        '''
        header = tk.Label(self.window,
                          text='\nSolarBytes WiFi/Server Configuration\n\n',
                          font=self.constants.HEADER_FONT_SETTINGS,
                          bg=self.constants.BACKGROUND_COLOR)
        header.pack()

        wifi_entry_description = tk.Label(self.window,
                                          text='Obtain wpa_supplicant network credentials \nfrom your network administrator and \nenter in the below field:',
                                          anchor="w",
                                          justify="left",
                                          font=self.constants.BODY_FONT_SETTINGS,
                                          bg=self.constants.BACKGROUND_COLOR)
        wifi_entry_description.pack()
                                               
        supplicant_entry = tk.Text(self.window,
                                   height=11)
        supplicant_entry.pack()

        save_supplicant_button = tk.Button(self.window,
                                           text="Save WiFi Network and Reboot",
                                           command=lambda: wf.saveWifiRebootPi(self.constants.SUPPLICANT_PATH, supplicant_entry.get("1.0","end-1c")))
        save_supplicant_button.pack()

        clear_supplicant_button = tk.Button(self.window,
                                            text="Clear Supplicant File",
                                            command=lambda: wf.clearSupplicantFile(self.constants.SUPPLICANT_PATH))
        clear_supplicant_button.pack()
