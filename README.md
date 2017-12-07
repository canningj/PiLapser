{\rtf1\ansi\ansicpg1252\cocoartf1404
{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fnil\fcharset0 AndaleMono;\f2\fnil\fcharset0 Monaco;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red38\green38\blue38;\red255\green255\blue255;
\red49\green49\blue49;\red242\green242\blue242;}
\margl1440\margr1440\vieww17760\viewh14500\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # piLapser\
\
piLapser is a project that turns a Raspberry Pi into a powerful time-lapse photography device.  It allows a user to create a new time-lapse that incorporates lateral motion of the camera in the midst of filming.\
\
## Getting Started\
\
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.\
\
### Prerequisites\
\
What things you need to install the software and how to install them\
\
```\
Python 3.6.0\
Django 1.8\
gphoto2\
\
```\
\
### Installing\
\
How to get the environment running\
\
Install pip\
```\
\pard\pardeftab720\sl280\partightenfactor0

\f1 \cf3 \cb4 \strokec3 python\cf5 \strokec5  \cf3 \strokec3 get\cf5 \strokec5 -\cf3 \strokec3 pip\cf5 \strokec5 .\cf3 \strokec3 py\cf5 \strokec5 \
\pard\pardeftab720\sl280\partightenfactor0

\f0 \cf0 \cb1 \outl0\strokewidth0 ```\
Activate the virtual environment\
\pard\pardeftab720\sl280\partightenfactor0
\cf0 ```\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs36 \cf6 \cb0 \kerning1\expnd0\expndtw0 \CocoaLigature0 source piENV/bin/activate\
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf0 \cb1 \expnd0\expndtw0\kerning0
\CocoaLigature1 ```\
Followed by installing django\
```\cf2 \outl0\strokewidth0 \strokec2 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 sudo pip install Django==1.8\
```\
Download the gphoto2 library\
\pard\pardeftab720\sl280\partightenfactor0
\cf0 \outl0\strokewidth0 ```\cf2 \outl0\strokewidth0 \strokec2 \
\pard\pardeftab720\sl280\partightenfactor0
{\field{\*\fldinst{HYPERLINK "https://sourceforge.net/projects/gphoto/files/"}}{\fldrslt \cf2 https://sourceforge.net/projects/gphoto/files/}}\
\pard\pardeftab720\sl280\partightenfactor0
\cf0 \outl0\strokewidth0 ```\
\cf2 \outl0\strokewidth0 \strokec2 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 Run the server\
\pard\pardeftab720\sl280\partightenfactor0
\cf0 \outl0\strokewidth0 ```\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs36 \cf6 \cb0 \kerning1\expnd0\expndtw0 \CocoaLigature0 python3 manage.py runserver 0.0.0.0:8000\

\f0\fs24 \cf0 \cb1 \expnd0\expndtw0\kerning0
\CocoaLigature1 \
\pard\pardeftab720\sl280\partightenfactor0
\cf0 ```\
\
##Using the application\
In order to access the application, connect the Pi to your local network and run ifconfig on the Pi in order to find the IP address of the machine.  Assuming the IP address of the Pi is 1.2.3.4, connect via the following address.\
\
```\
http://1.2.3.4:8000/piLapse/\
```\cf2 \outl0\strokewidth0 \strokec2 \
\pard\pardeftab720\sl280\partightenfactor0
\cf2 \
\
## Built With\
\
* [Django]({\field{\*\fldinst{HYPERLINK "https://www.djangoproject.com/"}}{\fldrslt https://www.djangoproject.com/}}) - The server framework used\
* [gphoto2]({\field{\*\fldinst{HYPERLINK "http://www.gphoto.org/"}}{\fldrslt http://www.gphoto.org/}}) - Camera control library\
* [Bootstrap]({\field{\*\fldinst{HYPERLINK "https://getbootstrap.com/"}}{\fldrslt https://getbootstrap.com/}}) - Front end styling\
\
\
## Authors\
\
* **Jon Canning** - *Creator* - [canningj](https://github.com/canningj)\
\
\
}