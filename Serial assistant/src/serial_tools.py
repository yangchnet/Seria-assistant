from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
import threading


class MainWindow():
    # receiveDisabel = BooleanVar()       # 不可接收
    # on_off = StringVar()  # 按钮字段
    # bottom_msg = StringVar()  # 底部提示字段
    # port_list = StringVar()  # 串口列表
    # re_msg = StringVar()  # 串口收到信息字段

    def __init__(self):
        self.receiveDisabel = False  # 设置为可接收
        self.addWidget()
        self.initTool()
        self.initEvent()
        self.getParameters()
        self.setgrid()

    def initTool(self):
        self.ser = serial.Serial()
        return

    def addWidget(self):
        '''添加各个小部件, 设置其基本属性'''
        self.root = Tk()
        # root下的六个部分
        self.serial_lf = ttk.Labelframe(self.root, text='串口设置', padding='10 10 10 10')  # 串口设置帧
        self.receive_lf = ttk.Labelframe(self.root, text='接收设置', padding='10 10 10 10')  # 接收设置帧
        self.send_lf = ttk.Labelframe(self.root, text='发送设置', padding='10 10 10 10')  # 发送设置帧
        self.on_off_button = ttk.Button(self.root, text='打开串口', command=self.port_open)  # 打开/关闭串口
        self.msg_lable = ttk.Label(self.root, padding='10 10 10 10')  # 串口信息标签
        self.serial_text = Text(self.root, wrap='word', width=50, height=15, state='disabled')  # 接收信息窗口

        # 向self.serial_lf中添加选项
        self.serial_lable = ttk.Label(self.serial_lf, text='串口选择')
        self.serial_selected = ttk.Combobox(self.serial_lf, values=self.get_port(), state='readonly')
        self.serial_selected.set(self.get_port()[0])

        self.b_lable = ttk.Label(self.serial_lf, text='波特率')
        self.b_selected = ttk.Combobox(self.serial_lf, values=('9600', '14400', '19200', '28800'), state='readonly')
        self.b_selected.set('19200')

        self.parity_lable = ttk.Label(self.serial_lf, text='校验位')
        self.parity = ttk.Combobox(self.serial_lf, values=('N', 'E', 'O', 'M', 'S'), state='readonly')
        self.parity.set("N")

        self.bytesize_lable = ttk.Label(self.serial_lf, text='数据位', )
        self.bytesize = ttk.Combobox(self.serial_lf, values=('5', '6', '7', '8'), state='readonly')
        self.bytesize.set("8")

        self.stop_lable = ttk.Label(self.serial_lf, text='停止位')
        self.stop_selected = ttk.Combobox(self.serial_lf, values=('1', '1.5', '2'), state='readonly')
        self.stop_selected.set("1")

        # 向self.receive_lf中添加选项
        self.hex_radio = ttk.Radiobutton(self.receive_lf, text='16进制显示', value='16')
        self.ascii_radio = ttk.Radiobutton(self.receive_lf, text='ascii码显示', value='ascii')
        self.empty_button = ttk.Button(self.receive_lf, text='清空')

        # 向self.self.send_lf中添加选项
        self.send_text = Text(self.send_lf, width=20, height=5)
        self.send_text.rowconfigure(0, weight=2)
        self.send_text.columnconfigure(0, weight=1)
        self.send_button = ttk.Button(self.send_lf, text='发送')

        return

    def initEvent(self):
        self.on_off_button.bind('<ButtonPress>, <ButtonRelease>', self.port_open)
        return

    def getParameters(self):
        return

    def setgrid(self):
        # 为六个部分分别设置布局
        # 串口设置帧
        self.serial_lf.grid(row=0, column=0, rowspan=5, columnspan=2, sticky=(N, W, E, S), padx=10, pady=10)
        self.serial_lf.rowconfigure(0, weight=2)
        self.serial_lf.rowconfigure(1, weight=2)
        self.serial_lf.columnconfigure(0, weight=5)
        self.serial_lf.columnconfigure(1, weight=5)
        self.serial_lf.columnconfigure(2, weight=5)
        self.serial_lf.columnconfigure(3, weight=5)
        self.serial_lf.columnconfigure(4, weight=5)

        # 接收设置帧
        self.receive_lf.grid(row=5, column=0, rowspan=2, columnspan=2, sticky=(N, E, W, S), padx=10, pady=10)
        self.receive_lf.rowconfigure(5, weight=2)
        self.receive_lf.columnconfigure(0, weight=2)

        # 发送设置帧
        self.send_lf.grid(row=5, column=2, rowspan=2, columnspan=3, sticky=(N, E, W, S), padx=10, pady=10)
        self.send_lf.rowconfigure(5, weight=4)
        self.send_lf.columnconfigure(2, weight=5)

        # 按钮帧
        self.on_off_button.grid(row=5, column=5, sticky=S, padx=5)
        self.on_off_button.columnconfigure(5, weight=1)
        self.on_off_button.rowconfigure(5, weight=1)

        # 串口信息标签
        self.msg_lable.grid(row=7, column=0, columnspan=3, rowspan=1, sticky=(N, E, W, S))
        self.msg_lable.columnconfigure(0, weight=1)
        self.msg_lable.rowconfigure(7, weight=3)

        # 接收信息窗口
        self.serial_text.grid(row=0, column=2, columnspan=5, rowspan=4, sticky=W, padx='10', pady='20')
        self.serial_text.rowconfigure(0, weight=4)
        self.serial_text.columnconfigure(2, weight=2)

        # 二级排布
        self.serial_lable.grid(row=0, column=0, pady=10)
        self.serial_selected.grid(row=0, column=1)
        self.b_lable.grid(row=1, column=0, pady=10)
        self.b_selected.grid(row=1, column=1)
        self.parity.grid(row=2, column=0, pady=10)
        self.parity.grid(row=2, column=1)
        self.bytesize_lable.grid(row=3, column=0, pady=10)
        self.bytesize.grid(row=3, column=1)
        self.stop_lable.grid(row=4, column=0, pady=10)
        self.stop_selected.grid(row=4, column=1)
        self.hex_radio.grid(row=0, column=0, pady=10)
        self.ascii_radio.grid(row=1, column=0, pady=10)
        self.empty_button.grid(row=0, column=1, rowspan=2, padx='10', pady='10')
        self.send_text.grid(row=0, column=0, rowspan=2, columnspan=2, padx='10', pady='10')
        self.send_button.grid(row=0, column=2, padx='10', pady='10', rowspan=2)

        self.root.mainloop()
        return

    def get_port(self):
        port = list(serial.tools.list_ports.comports())
        if len(port) <= 0:
            return -1
        else:
            port_list = []
            for p in port:
                port_list.append(p[0])
        return port_list

    def port_open(self):
        if self.ser.is_open:
            '''如果串口是打开的，那么设置receiveDisable不可用，关闭串口，并使下拉框可用'''
            self.receiveDisabel = True
            self.ser.close()
            self.on_off_button.setvar("打开串口")
            self.serial_selected.state('readonly')
            self.stop_selected.state('readonly')
            self.b_selected.state('readonly')
            self.bytesize.state('readonly')
            self.parity.state('readonly')
            self.msg_lable.setvar("串口已关闭")
        else:
            '''串口是关闭的，设置receiveDisable可用，打开串口，使下拉框不可用'''
            self.receiveDisabel = False
            self.ser.port = self.serial_selected.get()
            self.ser.baudrate = self.b_selected.get()
            self.ser.stopbits = int(self.stop_selected.get())
            self.ser.parity = self.parity.get()
            self.ser.bytesize = int(self.bytesize.get())
            self.ser.open()
            self.msg_lable.setvar("串口已打开")
            receiveProcess = threading.Thread(target=self.receiveData())
            receiveProcess.setDaemon(True)
            receiveProcess.start()

    def receiveData(self):
        self.receiveDisabel = False
        while (not self.receiveDisabel):
            b = self.ser.read()
            if b != None:
                byte = byte + str(b.hex())
                self.serial_text.insert(INSERT, byte)


def main():
    app = MainWindow()


if __name__ == '__main__':
    main()
