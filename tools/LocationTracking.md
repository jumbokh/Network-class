## Location Tracking Tools
```
Location Tracking Tools :- Concept behind Seeker is simple, just like we host phishing pages to get credentials why not host a fake page that requests your location like many popular location based websites. Read more on thewhiteh4t's Blog .Seeker Hosts a fake website which asks for Location Permission and if the target allows it, we can get :
Longitude
Latitude
Accuracy
Altitude - Not always available
Direction - Only available if user is moving
Speed - Only available if user is moving
Along with Location Information we also get Device Information without any permissions :
Unique ID using Canvas Fingerprinting
Device Model - Not always available
Operating System
Platform
Number of CPU Cores - Approximate Results
Amount of RAM - Approximate Results
Screen Resolution
GPU information
Browser Name and Version
Public IP Address
Local IP Address
Local Port
Automatic IP Address Reconnaissance is performed after the above information is received.
This tool is a Proof of Concept and is for Educational Purposes Only, Seeker shows what data a malicious website can gather about you and your devices and why you should not click on random links and allow critical permissions such as Location etc.
How is this Different from IP GeoLocation
Other tools and services offer IP Geolocation which is NOT accurate at all and does not give location of the target instead it is the approximate location of the ISP.
Seeker uses HTML API and gets Location Permission and then grabs Longitude and Latitude using GPS Hardware which is present in the device, so Seeker works best with Smartphones, if the GPS Hardware is not present, such as on a Laptop, Seeker fallbacks to IP Geolocation or it will look for Cached Coordinates.
Generally if a user accepts location permsission, Accuracy of the information recieved is accurate to approximately 30 meters
Accuracy depends on multiple factors which you may or may not control such as :
Device - Won't work on laptops or phones which have broken GPS
Browser - Some browsers block javascripts
GPS Calibration - If GPS is not calibrated you may get inaccurate results and this is very common.
```
* https://github.com/thewhiteh4t/seeker.git
```
Installation
Kali Linux / Arch Linux / Ubuntu / Parrot OS / Termux
git clone https://github.com/thewhiteh4t/seeker.git
cd seeker/
chmod +x install.sh
./install.sh
BlackArch Linux
sudo pacman -S seeker
Docker
docker pull thewhiteh4t/seeker
OSX
git clone https://github.com/thewhiteh4t/seeker.git
cd seeker/
python3 seeker.py
In order to run in tunnel mode, install ngrok by running this command in the terminal:
brew install ngrok/ngrok/ngrok
ngrok http 8080
```
