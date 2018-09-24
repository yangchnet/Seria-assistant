import serial.tools.list_ports
from tkinter import *
from tkinter import ttk

root = Tk()  # root帧

on_flag = BooleanVar()
on_off = StringVar()
bottom_msg = StringVar()
portname_list = StringVar()
receive_msg = StringVar()
ser = serial.Serial()

bottom_msg.set('jaklgjklajgklaj')


# 定义函数
def get_port():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        return -1
    else:
        portname_list = []
        for port in port_list:
            portname_list.append(port[0])
    return portname_list


on_off.set('打开串口')


def com_selected(*args):
    ser.port = serial_selected.get()


def baud_selected(*args):
    ser.baudrate = b_selected.get()


def checkbyte_selected(*args):
    ser.parity = check_selected.get()


def databyte_selected(*args):
    ser.bytesize = int(data_selected.get())


def stopbyte_selected(*args):
    ser.stopbits = int(stop_selected.get())


def port_open(*args):
    if on_off.get() == '打开串口':
        on_off.set('关闭串口')
        bottom_msg.set('串口打开')
        on_flag.set(1)
        ser.open()
        while on_flag.get() != 0:
            a= ser.readline()
            serial_text.insert(INSERT, ser.readline())
        return 0
    elif on_off.get() == '关闭串口':
        ser.close()
        bottom_msg.set('串口关闭')
        on_off.set('打开串口')
        return 0


# root下的六个部分
serial_lf = ttk.Labelframe(root, text='串口设置', padding='10 10 10 10')  # 串口设置帧
receive_lf = ttk.Labelframe(root, text='接收设置', padding='10 10 10 10')  # 接收设置帧
send_lf = ttk.Labelframe(root, text='发送设置', padding='10 10 10 10')  # 发送设置帧
on_off_button = ttk.Button(root, textvariable=on_off, command=port_open)  # 打开/关闭串口
msg_lable = ttk.Label(root, textvariable=bottom_msg, padding='10 10 10 10')  # 串口信息标签
serial_text = Text(root, wrap='word', width=50, height=15, state='disabled')  # 接收信息窗口

# 向serial_lf中添加选项
serial_lable = ttk.Label(serial_lf, text='串口选择')
serial_selected = ttk.Combobox(serial_lf, values=get_port(), state='readonly')
serial_selected.set(get_port()[0])
ser.port = serial_selected.get()

b_lable = ttk.Label(serial_lf, text='波特率')
b_selected = ttk.Combobox(serial_lf, values=('9600', '14400', '19200', '28800'), state='readonly')
b_selected.set('19200')
ser.baudrate = b_selected.get()

check_lable = ttk.Label(serial_lf, text='校验位')
check_selected = ttk.Combobox(serial_lf, values=('N', 'E', 'O', 'M', 'S'), state='readonly')
check_selected.set("N")
ser.parity = check_selected.get()

data_lable = ttk.Label(serial_lf, text='数据位', )
data_selected = ttk.Combobox(serial_lf, values=('5', '6', '7', '8'), state='readonly')
data_selected.set("8")
ser.bytesize = int(data_selected.get())

stop_lable = ttk.Label(serial_lf, text='停止位')
stop_selected = ttk.Combobox(serial_lf, values=('1', '1.5', '2'), state='readonly')
stop_selected.set("1")
ser.stopbits = int(stop_selected.get())

# 向receive_lf中添加选项
re_code = {'16': "16", 'ascii': 'ascii'}
hex_radio = ttk.Radiobutton(receive_lf, text='16进制显示', value='16')
ascii_radio = ttk.Radiobutton(receive_lf, text='ascii码显示', value='ascii')
empty_button = ttk.Button(receive_lf, text='清空')

# 向send_lf中添加选项
send_text = Text(send_lf, width=20, height=5)
send_text.rowconfigure(0, weight=2)
send_text.columnconfigure(0, weight=1)
send_button = ttk.Button(send_lf, text='发送')

on_off_button.bind('<ButtonPress>, <ButtonRelease>', port_open)
serial_selected.bind('<ComboboxSelected>', com_selected())
b_selected.bind('ComboboxSelected', baud_selected())
check_selected.bind('ComboboxSelected', checkbyte_selected())
data_selected.bind('ComboboxSelected', databyte_selected())
stop_selected.bind('ComboboxSelected', stopbyte_selected())

# 为六个部分分别设置布局
# 串口设置帧
serial_lf.grid(row=0, column=0, rowspan=5, columnspan=2, sticky=(N, W, E, S), padx=10, pady=10)
serial_lf.rowconfigure(0, weight=2)
serial_lf.rowconfigure(1, weight=2)
serial_lf.columnconfigure(0, weight=5)
serial_lf.columnconfigure(1, weight=5)
serial_lf.columnconfigure(2, weight=5)
serial_lf.columnconfigure(3, weight=5)
serial_lf.columnconfigure(4, weight=5)

# 接收设置帧
receive_lf.grid(row=5, column=0, rowspan=2, columnspan=2, sticky=(N, E, W, S), padx=10, pady=10)
receive_lf.rowconfigure(5, weight=2)
receive_lf.columnconfigure(0, weight=2)

# 发送设置帧
send_lf.grid(row=5, column=2, rowspan=2, columnspan=3, sticky=(N, E, W, S), padx=10, pady=10)
send_lf.rowconfigure(5, weight=4)
send_lf.columnconfigure(2, weight=5)

# 按钮帧
on_off_button.grid(row=5, column=5, sticky=S, padx=5)
on_off_button.columnconfigure(5, weight=1)
on_off_button.rowconfigure(5, weight=1)

# 串口信息标签
msg_lable.grid(row=7, column=0, columnspan=3, rowspan=1, sticky=(N, E, W, S))
msg_lable.columnconfigure(0, weight=1)
msg_lable.rowconfigure(7, weight=3)

# 接收信息窗口
serial_text.grid(row=0, column=2, columnspan=5, rowspan=4, sticky=W, padx='10', pady='20')
serial_text.rowconfigure(0, weight=4)
serial_text.columnconfigure(2, weight=2)

# 二级排布
serial_lable.grid(row=0, column=0, pady=10)
serial_selected.grid(row=0, column=1)
b_lable.grid(row=1, column=0, pady=10)
b_selected.grid(row=1, column=1)
check_lable.grid(row=2, column=0, pady=10)
check_selected.grid(row=2, column=1)
data_lable.grid(row=3, column=0, pady=10)
data_selected.grid(row=3, column=1)
stop_lable.grid(row=4, column=0, pady=10)
stop_selected.grid(row=4, column=1)
hex_radio.grid(row=0, column=0, pady=10)
ascii_radio.grid(row=1, column=0, pady=10)
empty_button.grid(row=0, column=1, rowspan=2, padx='10', pady='10')
send_text.grid(row=0, column=0, rowspan=2, columnspan=2, padx='10', pady='10')
send_button.grid(row=0, column=2, padx='10', pady='10', rowspan=2)

root.mainloop()
