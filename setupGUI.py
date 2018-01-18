#!/usr/bin/env python3

import tkinter

import wifiFunctions as wf
from GuiSetupConstants import GuiSetupConstants

'''
Initial code used to create the window and add title, color and dimensions and create stylistic constants
'''
constants = GuiSetupConstants()
window = tkinter.Tk()
window.title(constants.TITLE)
window.geometry(constants.DIMENSIONS)
window.configure(background=constants.BACKGROUND_COLOR)

'''
Create all widgets and pack into window
'''
header = tkinter.Label(window,
                       text='\nSolarBytes WiFi/Server Configuration\n\n',
                       font=constants.HEADER_FONT_SETTINGS,
                       bg=constants.BACKGROUND_COLOR)
header.pack()

wifi_entry_description = tkinter.Label(window,
                                       text='Obtain wpa_supplicant network credentials \nfrom your network administrator and \nenter in the below field:',
                                       anchor="w",
                                       justify="left",
                                       font=constants.BODY_FONT_SETTINGS,
                                       bg=constants.BACKGROUND_COLOR)
wifi_entry_description.pack()
                                       
supplicant_entry = tkinter.Text(window,
                                height=11)
supplicant_entry.pack()

save_supplicant_button = tkinter.Button(window,
                                        text="Save WiFi Network and Reboot",
                                        command=lambda: wf.saveWifiRebootPi(constants.SUPPLICANT_PATH, supplicant_entry.get("1.0","end-1c")))
save_supplicant_button.pack()

clear_supplicant_button = tkinter.Button(window,
                                         text="Clear Supplicant File",
                                         command=lambda: wf.clearSupplicantFile(constants.SUPPLICANT_PATH))
clear_supplicant_button.pack()
                                         

'''
Build window
'''
window.mainloop()
