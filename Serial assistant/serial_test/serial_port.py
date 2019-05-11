import serial.tools.list_ports
import binascii
def getport():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        return -1
    else:
        portname_list = []
        for port in port_list:
            portname_list.append(port[0])
        port_list_0 = list(port_list[0])
        port_serial = port_list_0[0]
        ser = serial.Serial(port_serial, 115200, bytesize=8, parity='N', stopbits=1,
                            timeout=None, xonxoff=0, rtscts=0)
        return ser
ser = getport()
# ser.open()
send_str = ''
count = 0
while 1:
    b = ser.read()
    b = binascii.a2b_hex(b.hex())
    if b == 'P':
        send_str = ''
        count = 0
    send_str += bytes.decode(b)
    count += 1
    if count == 191:
        break
    print(b)
print(send_str)
# ser = serial.Serial()
# ser_1 = serial.Serial()
# ser.port = getport()[0]
# ser.baudrate = 19200
# ser.bytesize = 8
# ser.stopbits = 1
# ser.parity = 'N'
#
# ser_1.port = getport()[0]
# ser_1.baudrate = 19200
# ser_1.bytesize = 8
# ser_1.stopbits = 1
# ser_1.parity = 'N'
# ser.open()
# ser_1.close()
# print('hello')
