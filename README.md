# API
Python generated API which allows user to view specific cryptocurrency information.

# Prerequisites:

This module assumes that the user already has a database set up with the stock information present.
This can be done by using the code found in https://github.com/Dhuel/PythonFinance

# Getting started

This API is created using Flask and virtualenv. To get started, the user will first have to install virtualenv.
```
$ sudo apt-get install python-virtualenv
```
Then create a directory for your API, virtual environment, get it up and running then install flask in your virtual env.
```
$ mkdir API
$ cd API
$ virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.
$ flask/bin/pip install flask
```
From here you may use the CryptoAPI.py file to set up your API

Run the following to give the module the correct permissions
```
$ chmod a+x CryptoAPI.py
```
Then start the API with 
```
$ ./CryptoAPI.py
```
You may also use the following command to start the virtual env, then run the python module from within it
```
source flask/bin/activate
python CryptoAPI.py
```

The API will now be callable from "serverip:5000/API/Get_last_values"

# Note

The current API only returns the last price value stored but future iterations will allow the user to see any stored record between certain date ranges.
