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
id = -1
def run():
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
            id = response[0]['Parameter']
            #print response[0]['Parameter']
            f.CmosLed(False)
            return id
        else:
            print'No finger detected'
            f.CmosLed(False)
            return id
        break
        
    
