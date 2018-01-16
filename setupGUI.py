import tkinter

'''
Initial code used to create the window and add title, color and dimensions
'''
window = tkinter.Tk()
window.title("Solar Bytes Setup")
window.geometry("1300x1300")
background_color = '#fdb603'
window.configure(background=background_color)

'''
Create all widgets to be packed into window
'''
header = tkinter.Label(window,
                       text='SolarBytes WiFi/Server Configuration',
                       bg=background_color)
wifi_entry_description = tkinter.Label(window,
                                       text='Obtain wpa_supplicant network credentials from your network administrator and enter in the below field',
                                       bg=background_color)
                                       
supplicant_entry = tkinter.Text(window,
                                height=11)
save_supplicant_button = tkinter.Button(window,
                                        text="Save WiFi Network and Reboot",
                                        command=saveWifiRebootPi)

'''
Pack all widgets into window and build window
'''
header.pack()
wifi_entry_description.pack()
supplicant_entry.pack()
save_supplicant_button.pack()

window.mainloop()
