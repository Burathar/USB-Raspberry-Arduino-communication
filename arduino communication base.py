import serial, time, sys

connection = 0
port = 0
blacklist = set()
timer = 0
data = ''

while True:
    while connection == 0:      #try to find the arduino at one of the usb ports
        try:
            if not '1' in blacklist:
                ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)
                #print 'Connection with USB0 established'
                connection = 1
                port = 1
        except IOError:
            try:
                if not '2' in blacklist:
                    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=.1)
                    #print 'Connection with USB1 established' 
                    connection = 1
                    port = 2
            except IOError:
                try:
                    if not '3' in blacklist:
                        ser = serial.Serial('/dev/ttyUSB2', 9600, timeout=.1)
                        #print 'Connection with USB2 established'
                        connection = 1
                        port = 3
                except IOError:
                    try:
                        if not '4' in blacklist:
                            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
                            #print 'Connection with ACM0 established'
                            connection = 1
                            port = 4
                    except IOError:
                        try:
                            if not '5' in blacklist:
                                ser = serial.Serial('/dev/ttyACM1', 9600, timeout=.1)
                                #print 'Connection with ACM1 established'
                                connection = 1
                                port = 5
                        except IOError:
                            try:
                                if not '6' in blacklist:
                                    ser = serial.Serial('/dev/ttyACM2', 9600, timeout=.1)
                                    #print 'Connection with ACM2 established'
                                    connection = 1
                                    port = 6
                            except IOError:
                                try:
                                    if not '7' in blacklist: #This one can be changed for an other arduino brand
                                        ser = serial.Serial('/dev/ttyACM3', 9600, timeout=.1)
                                        #print 'Connection with ACM3 established'
                                        connection = 1
                                        port = 7
                                except IOError:
                                    while blacklist:
                                        blacklist.pop()
                                    connection = 0
                                    print 'Connection can\'t be established'
                                    time.sleep(2)
                                except:
                                    print 'Unexpected error 1'
                                    time.sleep(2)
        
                                    
    else:
        data = ''
        try:
            time.sleep(1.55)  #Wait for the connection to stabalize
            ser.write('2')    #This vallue calls for the handshake
            while connection < 2: #Check whether we have the right arduino
                newChar = ser.read()
                if newChar:
                    timer = time.time()
                    data = data + newChar
                if time.time() - timer >= 0.02:
                    if data == '8765':  #This vallue is the handshake returncode for this arduino
                        connection = 2
                        #print 'Connection established'
                    else:
                        print 'This is not the right arduino'
                        connection = 0
                        blacklist.add(port)
                        #print blacklist
                time.sleep(1)
        except IOError:
            print 'Arduino doesn\'t respond'
            connection = 0
        except Exception as error:
            print 'Unexpected error:' , type(error)
            connection = 0

    while connection == 2:
        number = ''
        try:
            with open('number.txt', 'rw+') as f:
                f.seek(0)
                if not f.read(1):
                    #file is empty, wait for input
                    pass
                else:
                    #You can insert any other data you want to send here. (This will be sent every loop)
                    f.seek(0)
                    ser.write (f.read()) 
                    f.seek(0)
                    f.truncate()
                    time.sleep(1)
            ser.write('/n')
        except IOError:
            print 'File can\'t be accessed'
            connection = 0
        except:
            print 'Unexpected error'
            connection = 0
        time.sleep(1)  #this delay effects the update speed when the commection is working, lower when updatespeed is more important than cpu usage
    time.sleep(1)
