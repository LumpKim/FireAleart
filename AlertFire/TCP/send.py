def sendNormal():
    pack = [0x02, 0x03, 0x00, 0x06, 0xc6, 0x60, 0x03]
    data = [3]
    
    #crc = [0x0c, 0x06, 0x06, 0x00]  # crc16(data, len(data))
    #pack[4] = crc[2] << 4 + crc[3]
    #pack[5] = crc[0] << 4 + crc[1]

    return pack

def sendError():
    pack = [0x02, 0x05, 0x00, 0x15, 0x01, 0x00, 0x00, 0x00, 0x03]
    data = pack[3:5]

    crc = [0x0c, 0x06, 0x06, 0x00]  # crc16(data, len(data))
    pack[4] = crc[2] << 4 + crc[3]
    pack[5] = crc[0] << 4 + crc[1]

    return pack