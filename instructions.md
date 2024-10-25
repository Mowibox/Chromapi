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

Once connected to the Raspberry Pi, I launch the updates:

```
sudo apt update && sudo apt upgrade
```

As Ubuntu does not have raspi-config natively, we have to install it manually:

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

To run my python codes I installed pip ang git:
```
sudo apt-get install git python3-pip
```
Clone the repository:
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

I made simple tests inside on 'Chromapi/tests' folder to see that everything is working.

Legs and LEDs test: 
```
python3 test_1.py
```
Ultrasonic sensor and LEDs test: 
```
python3 test_2.py
```

## For computer vision

There's a folder dedicated to camera operation and computer vision in 'Chromapi/computer_vision'

A camera test is available by running the following script:
```
python3 cam_stream.py
```
More details are specified in the computer vision folder.

## For some optimization

```
systemctl list-unit-files --type=service
```

```
sudo systemctl disable service_name
```

```
sudo apt install zram-tools
```

```
zramctl
```

nano /boot/firmware/config.txt 

Don't forget to save the updates and reboot the pi.


## Troubleshooting 

```
sudo rm /usr/lib/python3.*/EXTERNALLY-MANAGED
```

``` 
sudo nano /etc/udev/rules.d/gpio.rules
```

```
sudo udevadm control --reload-rules
```

```
sudo udevadm trigger
```
