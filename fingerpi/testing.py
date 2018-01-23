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

print 'Entering test loop'
count = f.GetEnrollCount()
print 'Total enroll count is :' + str(count[0]['Parameter'])
print count

while True:
    print 'Place the finger on the scanner and press <Enter>'
    _ = raw_input()
    response = f.IsPressFinger()
    if response[0]['Parameter'] == 0:
        print 'There is a finger here'
        print response[0]['ACK']
        break
    else:
        print 'There is no finger here'
        print response[0]['ACK']
        break

while True:
    print 'Place your finger on the scanner for identification and press <Enter>'
    _ = raw_input()
    response = f.Identify()
    print response