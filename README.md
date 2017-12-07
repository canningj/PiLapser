# piLapser

piLapser is a project that turns a Raspberry Pi into a powerful time-lapse photography device.  It allows a user to create a new time-lapse that incorporates lateral motion of the camera in the midst of filming.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.\

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6.0
Django 1.8
gphoto2
```

### Installing

How to get the environment running

Install pip
```
python get-pip.py
```
Activate the virtual environment
```
source piENV/bin/activate\
```

Followed by installing django

```
sudo pip install Django==1.8\
```
Download the gphoto2 library
```
https://sourceforge.net/projects/gphoto/files/
```
Run the server
```
python3 manage.py runserver 0.0.0.0:8000\
```

### Using the application
In order to access the application, connect the Pi to your local network and run ifconfig on the Pi in order to find the IP address of the machine.  Assuming the IP address of the Pi is 1.2.3.4, connect via the following address.
```
http://1.2.3.4:8000/piLapse/
```

## Built With

* [Django](https://www.djangoproject.com/) - The server framework used
* [gphoto2](http://www.gphoto.org/) - Camera control library
* [Bootstrap](https://getbootstrap.com/) - Front end styling


## Authors

* **Jon Canning** - *Creator* - [canningj](https://github.com/canningj)
