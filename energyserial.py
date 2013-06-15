#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import serial
import time
redOld    = 0
greenOld  = 0
blueOld   = 0
bubbleOld = 0


def rgb(reg, green, blue):
    print "Red",reg
    print "Green",green
    print "Blue",blue

def bubble(value):
    print "Hallo"

def sendCommand():
    print "Sertest"
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    ser.read()
    ser.write("0,0,0,255\n")

if __name__ == '__main__':
    bubble(2)
    rgb(10,20,30)
    sendCommand()
