#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)

redOld    = 0
greenOld  = 0
blueOld   = 0
bubbleOld = 0


def rgb(red, green, blue):
    redOld = red
    greenOld = green
    blueOld = blue
    sendCommand()

def bubble(bubble):
    bubbleOld = bubble
    sendCommand()

def sendCommand():
    print "Sertest"
    ser.write("%d,%d,%d,%d\n" % (redOld,greenOld,blueOld,bubbleOld))

if __name__ == '__main__':
    print "Opening Port"
    ser.read()
    print "Port Open"
    bubble(100)
    rgb(100,200,250)
