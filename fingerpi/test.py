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

while True:
    print 'Place the finger on the scanner and press <Enter>'
    _ = raw_input()
    f.CmosLed(True)
    # response = f.IsPressFinger()
    response = f.EnrollStart(1)
    if response[0]['ACK']:
        print 'Start enrolling procedure, please present fingeprint'
        response1 = f.Enroll1()
        if response1[0]['ACK']:
            print 'Place your print again'
            response2 = f.Enroll2()
            if response2[0]['ACK']:
                print 'Place your finger a final time'
                response3 = f.Enroll3()
                if response3[0]['ACK']:
                    print'Fingerprint successfully enrolled, welcome user 1'
                
        
f.CmosLed(False)
if response[0]['Parameter'] != 'NACK_FINGER_IS_NOT_PRESSED':
    print 'Unknown Error occured', response[0]['Parameter']
    print 'I love donnuts'

