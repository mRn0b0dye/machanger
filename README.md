# ***machanger***
## About
Change Your Network Identity with Ease
## Installation
To install ```machanger```, follow these steps:
```
git clone https://github.com/mRn0b0dye/machanger
cd machanger
pip install -r requirements.txt
chmod +x machanger.py 
```
## Features
### Easy to use with clear instructions
```
python machanger.py -h
```
![Screenshot_2024-06-25_23_58_30](https://github.com/mRn0b0dye/machanger/assets/114957011/6991a428-ad79-4193-929c-8c922e32ce66)


### Change your MAC address with a single command
```
sudo python machanger.py -r eth0
```
### Generate random addresses for anonymity
```
sudo python machanger.py -a eth0
```
### Specify custom MAC addresses for specific needs
```
sudo python machanger.py -i eth0 -m 00:22:29:c3:f9:68
```
