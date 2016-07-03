# USB-Raspberry-Arduino-communication
A base application for primarily Raspberry > Arduino communication via USB, programmed with the intention of using multiple arduino's
## What do you need?

- Arduino (I use an aftermarket Arduino Uno)
- Raspberry pi (I use the Raspberry pi model 3b)
- USB A - USB B cable (to connect the Arduino to the raspberry)



You can use this porject as a base for any raspberry & arduino project, so you don't have to figure this out on your own.
There are some points though, you might have to change before it works in your case. One of them is the codeblock in the python file right at the start: The block that tries to open a serial connection over the usb ports. I found out that depending on which arduino board you use, the raspberry pi (3b in my case) recognises the arduino as either a USB device, or a ACM device (read up the difference over [here](https://www.rfc1149.net/blog/2013/03/05/what-is-the-difference-between-devttyusbx-and-devttyacmx). Because I have two arduinos, one of both category, I made my code compatable with both. However, if (all of your) your arduino(s) show up as for example USB devices, you can remove the latter category, to speed up your code.

For new people in the Raspberry world: you can find this out by unplugging your Arduino, and typing the following in your terminal.
```
ls /dev/tty*
```
Now plug in your Arduino, and run the command again. The new device that popped up should be your Arduino.
