from tkinter import *
from tkinter import ttk
import tkinter as tk
import serial
import serial.tools.list_ports
import threading
import binascii


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.bottom_msg = StringVar()
        self.on_off_msg = StringVar()
        self.coding_style = StringVar()
        self.coding = ''
        self.receiveDisabel = False  # 设置为可接收
        self.addWidget()
        self.initTool()
        self.setgrid()

    def initTool(self):
        self.ser = serial.Serial()
        return

    def addWidget(self):
        '''添加各个小部件, 设置其基本属性'''

        # root下的六个部分
        self.serial_lf = ttk.Labelframe(self, text='串口设置', padding='10 10 10 10')  # 串口设置帧
        self.receive_lf = ttk.Labelframe(self, text='接收设置', padding='10 10 10 10')  # 接收设置帧
        self.send_lf = ttk.Labelframe(self, text='发送设置', padding='10 10 10 10')  # 发送设置帧
        self.on_off_button = ttk.Button(self, textvariable=self.on_off_msg, command=self.open_close)  # 打开/关闭串口
        self.msg_lable = ttk.Label(self, padding='10 10 10 10', textvariable=self.bottom_msg)  # 串口信息标签
        self.serial_text = Text(self, wrap='word', width=50, height=15, state='normal')  # 接收信息窗口
        self.scroll = Scrollbar(self, orient=VERTICAL, command=self.serial_text.yview)
        self.serial_text.configure(yscrollcommand=self.scroll.set)
        self.on_off_msg.set('open')

        # 向self.serial_lf中添加选项
        self.serial_lable = ttk.Label(self.serial_lf, text='串口选择')
        self.serial_selected = ttk.Combobox(self.serial_lf, values=self.get_port(), state='readonly')
        self.serial_selected.set(self.get_port()[0])

        self.b_lable = ttk.Label(self.serial_lf, text='波特率')
        self.b_selected = ttk.Combobox(self.serial_lf, values=('9600', '14400', '19200', '28800', '115200'),
                                       state='readonly')
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
        self.hex_radio = ttk.Radiobutton(self.receive_lf, text='16进制显示', variable=self.coding_style, value='16')
        self.ascii_radio = ttk.Radiobutton(self.receive_lf, text='ascii码显示', variable=self.coding_style, value='ascii')
        self.empty_button = ttk.Button(self.receive_lf, text='清空', command=self.empty)
        self.coding_style.set('16')

        # 向self.self.send_lf中添加选项
        self.send_text = Text(self.send_lf, width=20, height=5)
        self.send_text.rowconfigure(0, weight=2)
        self.send_text.columnconfigure(0, weight=1)
        self.send_button = ttk.Button(self.send_lf, text='发送')

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
        self.serial_text.grid(row=0, column=2, columnspan=5, rowspan=4, sticky=(W, E), padx='10', pady='20')
        self.serial_text.rowconfigure(0, weight=4)
        self.serial_text.columnconfigure(2, weight=2)

        self.scroll.grid(row=0, column=6, rowspan=4, columnspan=1, sticky=(N, S),pady = 20)
        self.scroll.rowconfigure(0, weight=4)
        self.scroll.columnconfigure(6, weight=1)


        # 二级排布
        self.serial_lable.grid(row=0, column=0, pady=10)
        self.serial_selected.grid(row=0, column=1)
        self.b_lable.grid(row=1, column=0, pady=10)
        self.b_selected.grid(row=1, column=1)
        self.parity_lable.grid(row=2, column=0, pady=10)
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

        return

    def empty(self):
        print('empty')
        return self.serial_text.delete(0.0, END)

    def get_port(self):
        port = list(serial.tools.list_ports.comports())
        if len(port) <= 0:
            return -1
        else:
            port_list = []
            for p in port:
                port_list.append(p[0])
        return port_list

    def widget_disable(self):
        self.serial_selected['state'] = 'disabled'
        self.parity['state'] = 'disabled'
        self.bytesize['state'] = 'disabled'
        self.stop_selected['state'] = 'disabled'
        self.b_selected['state'] = 'disabled'

    def widget_able(self):
        self.serial_selected['state'] = 'normal'
        self.parity['state'] = 'normal'
        self.bytesize['state'] = 'normal'
        self.stop_selected['state'] = 'normal'
        self.b_selected['state'] = 'normal'

    def open_close(self):
        if not self.receiveDisabel:
            if not hasattr(self, 'worker'):
                self.setup_worker()
            self.on_off_msg.set('close')
            self.bottom_msg.set('port is open')
            self.worker.start()
            self.worker.receiveDisabel = True
            self.receiveDisabel = True
        elif self.receiveDisabel:
            self.bottom_msg.set('the port is close')
            self.worker.force_quit = True
            self.worker.receiveDisable = True
            del self.worker
            self.widget_able()
            self.receiveDisabel = False
            self.on_off_msg.set('open')

    def setup_worker(self):
        self.ser.port = self.serial_selected.get()
        self.ser.baudrate = self.b_selected.get()
        self.ser.stopbits = int(self.stop_selected.get())
        self.ser.parity = self.parity.get()
        self.ser.bytesize = int(self.bytesize.get())
        self.coding = self.coding_style.get()
        worker = ReceiveWorker(self)
        self.worker = worker

    def update_serial_text(self, information):
        return self.serial_text.insert(INSERT, information)


class ReceiveWorker(threading.Thread):
    def __init__(self, master):
        super().__init__()
        self.ser = master.ser
        self.master = master

        self.receiveDisable = False
        self.force_quit = False

    def run(self):
        while True:
            if not self.receiveDisable:
                if not self.ser.is_open:
                    self.ser.open()
                    self.master.widget_disable()
                if self.master.coding == '16':
                    b = self.ser.read()
                    print(b)
                    self.master.update_serial_text(b.hex())
                elif self.master.coding == 'ascii':
                    b = self.ser.read()
                    b = binascii.a2b_hex(b.hex())
                    self.master.update_serial_text(b)
            elif self.force_quit:
                # self.master.widget_able()
                del self.master.worker
                return


if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
