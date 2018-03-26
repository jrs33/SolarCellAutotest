# SolarCellAutotest
Solar cells are currently cleaned using water, which is incredibly wasteful and requires on site personel. To alleviate this issue, the Boston University ElectroDynamics lab
has built a technology called an ElectroDynamic screen, which uses electrical polarity to remove dust. In order to fully assure this system is functional, a team of Engineers
at BU collaborated to create SolarBytes, a fully automated testing system that uses proprietary hardware and software that integrates with the EDS and an array of solar cells to 
measure the effectiveness of performance restoration with EDS cleaning methods. The software in this repository includes things like:

- Scripts called by chron to auto-run tests, auto-connect to wifi and auto-renew ngrok tunnels
- An interactive GUI for on-site users to manage the system
- A web interface written in Flask to allow the user to initiate tests and query data
- Backend test logic that connects to an onboard sqlite database for EDS testing data

This software is portable on any Pi, and provides a needed solution to the ElectroDynamics lab and colleagues to run these tests.

## Getting started
1. Clone the repository on your Raspberry Pi
2. Download ngrok which is used to connect the website hosted on the Pi to the open internet:  https://ngrok.com/download
3. cd into the /bash directory and enter your wifi network object (obtain from administrator) into the network_template.txt file
4. Type in 'sh solarbytes_setup.sh'. This will download dependencies, change some file permissions on the pi and reboot the pi
5. Once the pi has rebooted, type ./webserver.sh to start the webserver, ./tunnelRenew.sh to connect the site to the open internet and check the url on a different device to be sure it networked

Thats it! You should now be all set to run tests to assure EDS cleaning effectiveness. 
