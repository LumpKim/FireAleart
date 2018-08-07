#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def crc16(data):
    if type(data) is tuple:
        data = list(data)

    crc_polynom = 0x8408
    crc_preset = 0xFFFF
    for i in range(0, len(data)):
        crc_preset ^= data[i]
        data[i] += data[i]
        for j in range(0, 8):
            if (crc_preset & 0x0001) > 0:
                crc_preset = (crc_preset>>1)^crc_polynom
            else:
                crc_preset = (crc_preset>>1)
    return crc_preset

if __name__ == "__main__":
    #hexdata = [0x21,0x00,0x00,0x00,0x00,0x00]
    hexdata = []
    if len(sys.argv) < 2:
        print('''usage: python crc16.py 210000000000 
or python crc16.py 21 00 00 00 00 00''')

    elif len(sys.argv) == 2:
        l = len(sys.argv[1])
        for i in range(l):
            if i%2==0:
                hexdata.append('0x%s' % sys.argv[1][i:i+2])
        hexdata = map(lambda x: int(x,16), hexdata)
        print("CRC: %X" % crc16(hexdata))
    else:
        for i in sys.argv:
            hexdata.append(i)
        del hexdata[0]
        hexdata = map(lambda x: int('0x%s'%x,16), hexdata)
        print("CRC: %X" % crc16(hexdata))