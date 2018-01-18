#!/usr/bin/env python3

import tkinter
import os

import guiSetupConstants as gsc

'''
Initial code used to create the window and add title, color and dimensions and create stylistic constants
'''
window = tkinter.Tk()
window.title(gsc.TITLE)
window.geometry(gsc.DIMENSIONS)
window.configure(background=gsc.BACKGROUND_COLOR)

'''
Create all widgets to be packed into window
'''
header = tkinter.Label(window,
                       text='\nSolarBytes WiFi/Server Configuration\n\n',
                       font=gsc.FONT_SETTINGS_HEADER,
                       bg=gsc.BACKGROUND_COLOR)
wifi_entry_description = tkinter.Label(window,
                                       text='Obtain wpa_supplicant network credentials \nfrom your network administrator and \nenter in the below field:',
                                       anchor="w",
                                       justify="left",
                                       font=gsc.FONT_SETTINGS_BODY,
                                       bg=gsc.BACKGROUND_COLOR)
                                       
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
    supplicant_file = open(gsc.SUPPLICANT_PATH,'a')
    supplicant_file.write('\n' + new_wifi_network)
    supplicant_file.close()
    os.system('sudo reboot')

window.mainloop()
