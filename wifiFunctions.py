import os

def saveWifiRebootPi(SUPPLICANT_PATH, wifi_network):
    supplicant_file = open(SUPPLICANT_PATH,'a')
    supplicant_file.write('\n' + wifi_network)
    supplicant_file.close()
    os.system('sudo reboot')

def clearSupplicantFile(SUPPLICANT_PATH):
    supplicant_file = open(SUPPLICANT_PATH,'w')
    supplicant_file.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev' + '\n' + 'update_config=1' + '\n')
    supplicant_file.close()
