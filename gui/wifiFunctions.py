import os

'''
Supplicant file interface to save and clear wifi credentials to auto-connect to wifi
'''

def saveWifiRebootPi(SUPPLICANT_PATH, wifi_network):
    supplicant_file = open(SUPPLICANT_PATH,'a')
    supplicant_file.write('\n' + wifi_network)
    supplicant_file.close()
    os.system('sudo reboot')

def clearSupplicantFile(SUPPLICANT_PATH):
    supplicant_file = open(SUPPLICANT_PATH,'w')
    supplicant_file.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev' + '\n' + 'update_config=1' + '\n')
    supplicant_file.close()
