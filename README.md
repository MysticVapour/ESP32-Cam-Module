# ESP32 Camera Module for Color Detection

## Items Required for Setup

1. ESP32 Camera Module
2. FTDI Transmitter
3. Connecting Wires
4. USB Cable - A-Male to Mini-B

## Steps for Hardware Setup

1. Connect the ESP32 Camera with the FTDI Transmitter in the following way
![image](https://github.com/MysticVapour/ESP32-Cam-Module/assets/59056465/3ccd65ee-1c98-4af2-8772-e717c8b56c94)

2. Use the USB Cable to connect the Transmitter with your PC

## Steps for Software Setup

1.	Open Arduino IDE and open the ColorDetectionTest file.
2.	Replace SSID and Password with your network ID.
3.	Make sure Board is (ESP32 Wrover Kit) and a desirable COM port is selected (The one to which your module is connected)
4.	Hold the reset button on the ESP32 and click Upload. Keep holding the reset button.
5.	When you see Connecting… on the console, release the reset button.
6.	Wait for the console to say Hard Resetting Pin
7.	Now remove the IO0 pin from ESP32 and press Reset button again
8.	Wait for Serial Monitor to say Camera Ok and note down the Local IP (192.168.1.XX)
9.	Open CV2 File, replace IP address with Local IP and run program (F5).

## Rough Sketch of Final Prototype
![image](https://github.com/MysticVapour/ESP32-Cam-Module/assets/59056465/9fe3bff8-6f29-4061-9eb6-c69ec2cbf318)

