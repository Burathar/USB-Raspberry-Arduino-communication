# USB-Raspberry-Arduino-communication
A base application for primarily Raspberry > Arduino communication via USB, programmed with the intention of using multiple arduino's

*I want to thank oscarliang.com for posting [this](https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/) article, for that article helped me out a lot at the start of coding this.*

## What do you need?
- Arduino (I use an aftermarket Arduino Uno)
- Raspberry Pi (I use the Raspberry Pi model 3b)
- USB A - USB B cable (to connect the Arduino to the raspberry)

## How do you use this project?
You can use this project as a base for any Raspberry & Arduino project, so you can (after some minor tweaking) start coding the interesting part of your project right away.

### The Arduino setup
I found it the easiest to load the Arduino sketch to the Arduino on my windows desktop, just because the Linux version of the Arduino IDE doesn't work as well. I think beyond that the uploading of the sketch speaks for itself.

### The Raspberry setup
I think copying the Python script over to the raspberry is easy enough, however, I'd like to make some notes regarding the contents of the script.

I found out that, depending on which Arduino board you use, the Raspberry Pi recognises the Arduino as either a USB device, or a ACM device (read up the difference over [here](https://www.rfc1149.net/blog/2013/03/05/what-is-the-difference-between-devttyusbx-and-devttyacmx). Because I have two Arduinos, one of both category, I made my code compatable with both. However, if (all of your) your arduino(s) show up as for example USB devices, you can remove the latter category, to speed up your code.

For new people in the Raspberry world: you can find this out by unplugging your Arduino, and typing the following in your terminal.
```
ls /dev/tty*
```
Now plug in your Arduino, and run the command again. The new device that popped up should be your Arduino.

You might notice that, when you plug your arduino in and out, it sometimes pops up as ttyUSB0, and sometimes ttyUSB1. As far as I know this is pretty random, and a script will give an error and stop if you use the wrong one. That, as a matter of fact, is mainly why I wrote this code to begin with. One of the advantages of this project is that it deals with this problem, so you shoudn't worry.

#### The Handshake
This project uses a crude kind of handshake to check if the Raspberry is talking to the right Arduino. therefore it's important that you change the values for this handshake if you are planning on using multiple Arduinos (To be clear: The python scipt isn't designed to handle multiple Arduinos at once, the idea is that you can run multiple scripts besides each other, each communicating to one Arduino.).

The vallue for the handshake can be found in the python script in line 81, and in the arduino sketch in line 15. **These vallues must be the same**

This script will, when it is running, continuously check if there is an arduino available. If there is one, it will try to make the handshake. If it receices the handshake, it will send the contents of number.txt over the usb bus that it has selected. This way you can write data to the file from an other program, and this script will forward it to the arduino. If the script doesn't recieve the handshake, it will blacklist that (digital) usb port, and check the other ones. To be clear, this function is mainly implemented for when you use multiple arduino's. If the script had tried all of the usb ports, it un-blacklists every port, and tries again.

The script also makes it possible to disconnect the arduino at any moment and reconnect later, without the script having to restart. However, it does send the initiation data (for the handshake) every time, so you might want to exclude that result on the arduino side with an if statement.
