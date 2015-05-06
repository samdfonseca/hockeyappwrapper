# hockeyappwrapper
A mostly useless wrapper around the mostly useless HockeyApp API.

### Example
```python
from hockeyapp import api as hockeyapi
from hockeyapp import utils as hockeyutils

# List auth tokens
all_tokens = hockeyapi.auth_tokens('someuser@somewhere.com', 'someuserspassword')
token = tokens['tokens'][0]['token']

# List apps
apps = hockeyapi.apps(token)

# Download an apk
app = hockeyutils.get_app_by('bundle_identifier', 'com.example.myapp')
version = hockeyutils.get_version(app, '1.0')
hockeyapi.download_apk('myapp-1.0.apk', version)
```

# dlhockapk
A command-line script with some basic functionality.

### Example
```
# Set variable
export HOCKEYAPP_API_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Single app
$ dlhockapk app -p com.example.myapp
$ dlhockapk app -a title MyApp

# Multiple apps
$ dlhockapk apps -p com.example
$ dlhockapk apps -a company "Example Company"

# Latest version
$ dlhockapk version -p com.example.myapp

# Specific version
$ dlhockapk version -p com.example.myapp -v 0.9.1

# All versions
$ dlhockapk versions -p com.example.myapp

# Download specific apk
$ dlhockapk download -p com.example.myapp -v 0.9.1 -d apks

# Download all apks
$ dlhockapk download -p com.example.myapp -d apks

# Install latest apk on a device via adb
$ dlhockapk install -s <specific device> --reinstall -p com.example.myapp
```
