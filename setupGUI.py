import tkinter

'''
Initial code used to create the window and add title, color and dimensions and create stylistic constants
'''
window = tkinter.Tk()
window.title("Solar Bytes Setup")
window.geometry("1300x1300")
BACKGROUND_COLOR = '#fdb603'
FONT_SETTINGS_HEADER = ('Helvetica', '16', 'bold')
FONT_SETTINGS_BODY = ('Helvetica', '12')
window.configure(background=BACKGROUND_COLOR)

'''
Create all widgets to be packed into window
'''
header = tkinter.Label(window,
                       text='\nSolarBytes WiFi/Server Configuration\n\n',
                       font=FONT_SETTINGS_HEADER,
                       bg=BACKGROUND_COLOR)
wifi_entry_description = tkinter.Label(window,
                                       text='Obtain wpa_supplicant network credentials \nfrom your network administrator and \nenter in the below field:',
                                       anchor="w",
                                       justify="left",
                                       font=FONT_SETTINGS_BODY,
                                       bg=BACKGROUND_COLOR)
                                       
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
    supplicant_file = open('/etc/wpa_supplicant/wpa_supplicant.conf','a')
    supplicant_file.write(new_wifi_network)
    supplicant_file.close()
    
    

window.mainloop()
