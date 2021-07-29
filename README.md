*Date creation: 04/04/2021*

# SaveCameraAuto

## Description
This script is intended to automate the backup of a SD card when plugged in a Linux OS.

## First purpose
This project is created for the 4x4 Capsule world trip to ease the backup of camera, Go Pro data.

## Installation
# Find USB Device Vendor ID
Copy Vendor ID by looking for a new device by running 'lsusb' command.
For instance the usb device Vendor ID of 'Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub' is '1d6b'

# Create custom udev
Copy the 10.autobackup.rules in /etc/udev/rules.d/ folder and rename it if needed
Update the content replacing 'ATTRS{idVendor}' with '1d6b' in our example and update the RUN parameter to your script location

## Integration
TODO

## Language of programmation
TODO

## How to contribute
The main and develop branch is protected and only Valentin Rudloff will be able to merge and create a version
One can create a feature/* or fix/* like branche to give new features or fixes to the project 
