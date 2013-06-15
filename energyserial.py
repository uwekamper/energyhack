#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time


redOld    = 0
greenOld  = 0
blueOld   = 0
bubbleOld = 0

class Yoda(object):
    """
    A class to encapsulate the
    """
    def __init__(self, serial_port='/dev/ttyACM0'):
        self.red = 0
        self.green = 0
        self.blue = 0
        self.bubble = 0

        self.ser = serial.Serial(serial_port, 9600, timeout=1)
        print "opening %s" % self.ser.portstr
        self.ser.read()

    def __del__(self):
        self.ser.close()

    def set_rgb(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self._sendCommand()

    def set_bubble(self, bubble):
        self.bubble = bubble
        self._sendCommand()

    def _sendCommand(self):
        values = (255 - self.red, 255 - self.green, 255 - self.blue, self.bubble)
        command = "%d,%d,%d,%d\n" % values
        print 'sending', command
        self.ser.write(command)
        time.sleep(1)

if __name__ == '__main__':
    yoda = Yoda(serial_port='/dev/tty.usbmodem621')
    yoda.set_bubble(100)
    yoda.set_rgb(100,200,250)
