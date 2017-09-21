# Google play python3 API [![Build Status](https://travis-ci.org/NoMore201/googleplay-api.svg?branch=master)](https://travis-ci.org/NoMore201/googleplay-api)

This project contains an unofficial API for google play interactions. The code mainly comes from
[GooglePlayAPI project](https://github.com/egirault/googleplay-api/) which was written for python2 and it's not
maintained anymore. The code was ported to python3 with some important changes:

* ac2dm authentication with checkin and device info upload
* updated search and download calls
* using headers of a Nexus 6P. Add you own device under `device.properties` file

# Usage
Check the test.py module for a simple example.

An important note about login function:
```
def login(self, email, password, ac2dmToken=None, gsfId=None)
```
for first time logins, you should only provide email and password.
The module will take care of retrieving an ac2dm token, registering 
"your device" to the google account you supplied, and retrieving 
a Google Service Framework ID (which basically is the android ID of a device).

For the next logins you **should** save the ac2dm master token and the gsfId (androidId), and provide them as parameters to the login function. If you login again with email and password only, this is the equivalent of deleting the google account from you device and re-initalize it every time.

# API reversing

Since I started playing with a more recent version of the GooglePlay API on LineageOS 14.1 (Android 7.1) using [mitmproxy](https://mitmproxy.org/), I gathered some information about new APIs.
Checkout the Documentation folder for more details on single API endpoints.

# Development status
- [ ] Investigate how paid apps download works
- [ ] Investigate if it's possible to dowload apk with obb files
