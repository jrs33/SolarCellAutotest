
# SolarBytes
Solar cells are currently cleaned using water, which is incredibly wasteful and requires on site personnel. To alleviate this issue, the Boston University ElectroDynamics lab
has built a technology called an ElectroDynamic screen, which uses electrical polarity to remove dust. In order to fully assure this system is functional, a team of Engineers
at BU collaborated to create SolarBytes, a fully automated testing system that uses proprietary hardware and software that integrates with the EDS and an array of solar cells to 
measure the effectiveness of performance restoration with EDS cleaning methods. The software in this repository includes things like:

- Scripts called by chron to auto-run tests, auto-connect to wifi and auto-renew open web tunnels
- An interactive GUI for on-site users to manage the system
- A web interface written in Flask to allow the user to initiate tests, save and query data
- Backend test logic that connects to an onboard database to gather performance improvement of solar cell when cleaned by an EDS

This software is portable on any Pi, and provides a needed solution for the ElectroDynamics lab to run these tests live on solar farms.

## Introduction
To get started, we have outlined steps below to show you how to get your Pi up and running to integrate with your EDS testing hardware. The installation process has been condensed into various bash scripts to allow you to easily setup your SolarBytes system. 

### Installing Dependencies:
1) Obtain a raspberry pi with an installed OS and connect to a SolarBytes hardware system 
2) `git clone https://github.com/jrs33/SolarCellAutotest.git` to get the repo on the Pi
3) `cd <repo_location>/SolarCellAutotest/bash`
4) Run `sh permissions.sh` to make all shells executable
5) Obtain a wifi network from your system administrator and enter the proper fields into the `<repo_location>/SolarCellAutotest/bash/network_template.txt` template file. This is SUPER IMPORTANT and will allow the Pi to auto-connect to your areas wifi network. Check out  [this link](https://w1.fi/cgit/hostap/plain/wpa_supplicant/wpa_supplicant.conf) to learn about various network objects used to auto-connect to see what works for you
6) Run `./solarbytes_setup`. This will download all dependencies, setup your database, prepare buffers and configure your wifi. **This will also reboot your Pi**. 

With these steps done, the installation process should be complete.

### Manual Configuration
With the initial setup done, it is important to add some settings to other scripts to personalize your system and also manually start up other scripts that always need to be running

1) We need to be able to sync EDS test data to an onboard USB. Since each USB has a unique UUID we must dynamically recognize this USB. Run `./displayMounts` to see the UUID of your USB, which will be of the form **XXXX-XXXX**. 
2) With this UUID, open up the `syncCsvToUSB.sh` bash script, and notice the second line, which has a variable `USB_UUID_FROM_DISPLAY_MOUNTS=""`. Add the UUID you found from step 1 to this variable, and save the shell script with this new variable.
3) Start up the Flask web server by typing in `./webserver.sh`

Thats it! Data should now be able to be synced on the USB with that UUID connected to your Pi.

### Configuring Cron Jobs
At this point, all dependencies should be configured on your Pi, your USB should be configured, and the web server should be running on the Pi. We now have a few tasks we need to run at regular intervals using [cron](https://en.wikipedia.org/wiki/Cron). 

1) `cd <repo_location>/SolarCellAutotest/resources/`
2) Here you should see a `cron.txt` file. This is a static file that shows three scripts that are run on regular intervals
	* `tunnelRenew.sh` which sets up an [ngrok](https://ngrok.com/) tunnel to forward open web traffic to our on board web server port via a reverse proxy tunnel. This happens every day at 10am.
	* `syncCsvToUSB.sh` which we set up in the previous step, and syncs our data to a file on the onboard USB everyday at midnight
	* `runTest.sh` which runs an EDS cleaning test each day at noon
3) Copy this text file into your clipboard, and type `crontab -e` to edit the crontab file. Paste this text into the crontab file and save.

You are all done setting up your system! Thank you for taking the time to install SolarBytes and we hope you find it useful in proving EDS technology effectiveness to make green technology greener.

