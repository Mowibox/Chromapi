# Instructions for the Raspberry Pi Zero 2 WH configuration

## Installing the OS

For installing the OS, I used the Raspberry Pi Imager with an 16GB SD card. I then took the Ubuntu Server 24.04.1 (64-bit) OS. I don't forget to enable ssh options while editing the configuration. 

https://www.raspberrypi.com/software/

## OS basic configuration

Since I used the Raspberry Pi without screen (headless), I connect to the pi using ssh via the following command:

```
ssh user@192.168.xxx.xxx
```

Where 'user' is the username specified in the Raspberry Pi Imager configuration, and '@192.168.xxx.xxx' is the IP adress of the pi.

More infos: https://pimylifeup.com/raspberry-pi-ip-address/

Once connected to the Raspberry Pi, I upgraded the packages:

```
sudo apt update && sudo apt upgrade
```
As Ubuntu does not have raspi-config natively, I have to install it manually:

```
sudo apt-get install raspi-config
```
This allows me access to the Raspberry's configurations:
```
sudo raspi-config
```
Here are the parameters I modified/enabled:
* Interface options > Legacy camera
* Interface options > SPI
* Interface options > I2C
* Interface options > Serial Port
* Interface options > Remote GPIO
* Performance options > GPU Memory > 128 MB

Don't forget to reboot the pi after editing:

```
sudo reboot
```

## For programming

To run my python codes I installed pip:
```
sudo apt-get install python3-pip
```

I then installed zram-tools for reducing swap: 
```
sudo apt install zram-tools
```
You can check that zram-tools is well installed with this command:
```
zramctl
```

Clone the repository with git:
```
git clone https://github.com/Mowibox/Chromapi.git
```

Enter the folder:
```
cd Chromapi
```
And install the required python packages:
```
pip install -r requirements.txt
```

I wrote simple tests inside on 'Chromapi/tests' folder to see that everything is working.

Legs and LEDs test: 
```
python3 test_1.py
```
Ultrasonic sensor test: 
```
python3 test_2.py
```

## For computer vision

There's a folder dedicated to camera operation and computer vision in 'Chromapi/software/computer_vision'

A camera test is available by running the following script:
```
python3 cam_stream.py
```
More details are specified in the computer vision folder.

## Troubleshooting 

### Issue with pip
If you have this output when you are using pip:
```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

```
You can use the following command to bypass the error:
```
sudo rm /usr/lib/python3.*/EXTERNALLY-MANAGED
```

### Issues with GPIO permissions

By launching the tests scripts, you may have the following permission error:
```
RuntimeError: No access to /dev/mem.  Try running as root!
```
To fix this issue, you can create a 'gpio.rules' file:
``` 
sudo nano /etc/udev/rules.d/gpio.rules
```
Write this line inside the file:
```
KERNEL=="gpiomem", GROUP="gpio", MODE="0660"
```
Save the file and exit, then reload the udev rules:
```
sudo udevadm control --reload-rules
sudo udevadm trigger
```
