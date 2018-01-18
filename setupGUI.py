#!/usr/bin/env python3

import tkinter
import os

from guiSetupConstants import guiSetupConstants

'''
Initial code used to create the window and add title, color and dimensions and create stylistic constants
'''
constants = guiSetupConstants()
constants.TITLE = "LOL"
window = tkinter.Tk()
window.title(constants.TITLE)
window.geometry(constants.DIMENSIONS)
window.configure(background=constants.BACKGROUND_COLOR)

'''
Create all widgets to be packed into window
'''
header = tkinter.Label(window,
                       text='\nSolarBytes WiFi/Server Configuration\n\n',
                       font=constants.HEADER_FONT_SETTINGS,
                       bg=constants.BACKGROUND_COLOR)
wifi_entry_description = tkinter.Label(window,
                                       text='Obtain wpa_supplicant network credentials \nfrom your network administrator and \nenter in the below field:',
                                       anchor="w",
                                       justify="left",
                                       font=constants.BODY_FONT_SETTINGS,
                                       bg=constants.BACKGROUND_COLOR)
                                       
supplicant_entry = tkinter.Text(window,
                                height=11)
save_supplicant_button = tkinter.Button(window,
                                        text="Save WiFi Network and Reboot",
                                        command=lambda: saveWifiRebootPi())

'''
Pack all widgets into window and build window
'''
header.pack()
wifi_entry_description.pack()
supplicant_entry.pack()
save_supplicant_button.pack()


'''
Callback function definitions
'''
def saveWifiRebootPi():
    new_wifi_network = supplicant_entry.get("1.0", "end-1c")
    supplicant_file = open(constants.SUPPLICANT_PATH,'a')
    supplicant_file.write('\n' + new_wifi_network)
    supplicant_file.close()
    os.system('sudo reboot')

window.mainloop()
