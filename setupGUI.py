#!/usr/bin/env python
from GuiSetupConstants import GuiSetupConstants
import SolarBytesControlPanelGUI as sbgui
import tkinter as tk

'''
Initial code used to create the window and add title, color and dimensions and create stylistic constants
'''
constants = GuiSetupConstants()
window = tk.Tk()
app = sbgui.SolarBytesControlPanelApp(window, constants)

'''
Build window
'''
window.mainloop()
