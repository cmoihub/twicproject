#!/usr/bin/env python

import fingerpi as fp
# from fingerpi import base

# import struct
import time
# import matplotlib.pyplot as plt
import pickle


def printByteArray(arr):
    return map(hex, list(arr))

f = fp.FingerPi()


print 'Opening connection...'
f.Open(extra_info = True, check_baudrate = True)

print 'Changing baudrate...'
f.ChangeBaudrate(115200)
f.CmosLed(True)

while True:
    print 'Please place your finger and press <Enter>'
    _ = raw_input()
    response = f.CaptureFinger()
    if response[0]['ACK']:
        response = f.Identify()
        print response[0]['Parameter']
    else:
        print'No finger detected'
    break

f.CmosLed(False)

    
    