from tkinter import *
from tkinter import ttk

root = Tk()
root.title('color test')

red_frame = ttk.Frame(root, padding='20 20 20 20')  # 创建文本帧
red_frame['borderwidth'] = 2
red_frame['relief'] = 'sunken'
red_frame.grid(row=0, column=0, sticky=S)
red_frame.columnconfigure(1, weight=1)
red_frame.rowconfigure(1, weight=1)
red_label = ttk.Label(red_frame, text="red", anchor='e').grid(row=1, column=1, sticky=(N, W, E, S))

button_frame = ttk.Frame(root, padding='20 20 20 20')  # 按键帧
button_frame.grid(row=1, column=1, sticky=N)
button_frame.columnconfigure(1, weight=1)
button_frame.rowconfigure(1, weight=1)
button_0 = ttk.Button(button_frame, text='Button_0').grid(row=0, column=0, sticky=W)  # sticky设置对齐
button_1 = ttk.Button(button_frame, text='1').grid(row=1, column=0, sticky=W)

checkButton_frame = ttk.Frame(root, padding='20 20 20 20')  # 复选框帧
checkButton_frame.grid(row=2, column=2, sticky=E)
checkButton_frame.columnconfigure(2, weight=1)
checkButton_frame.rowconfigure(2, weight=1)
check_1 = ttk.Checkbutton(checkButton_frame, text='check_1').grid(row=0, column=0)
check_2 = ttk.Checkbutton(checkButton_frame, text='check_2').grid(row=1, column=0)
check_3 = ttk.Checkbutton(checkButton_frame, text='check_3').grid(row=1, column=1, columnspan=2)

radio_frame = ttk.Frame(root, padding='20 20 20 20')  # 单选按钮帧
radio_frame.grid(row=3, column=3)
radio_frame.columnconfigure(3, weight=1)
radio_frame.rowconfigure(3, weight=1)
radio_1 = ttk.Radiobutton(radio_frame, text='radio_1', value='1').grid(row=0, column=0)
radio_2 = ttk.Radiobutton(radio_frame, text='radio_2', value='2').grid(row=1, column=1)

entry_frame = ttk.Frame(root, padding='20 20 20 20')  # 输入框帧
entry_frame.grid(row=4, column=4)
entry_frame.rowconfigure(4, weight=1)
entry_frame.columnconfigure(4, weight=1)
usename = StringVar()
entry_1 = ttk.Entry(entry_frame, textvariable=usename, show='*').grid(row=0, column=0)


def put():
    print("hello")


combobox_frame = ttk.Frame(root, padding='20 20 20 20')  # 下拉框帧
combobox_frame.grid(row=5, column=5)
combobox_frame.rowconfigure(5, weight=1)
combobox_frame.columnconfigure(5, weight=1)
countryvar = StringVar()
# countryvar['values'] = ('1', '2', '3')
combobox_1 = ttk.Combobox(combobox_frame, textvariable=countryvar, values=('1', '2', '3'))
combobox_1.bind('<<ComboboxSelected>>', put())
combobox_1.grid(row=1, column=1)

lf = ttk.Labelframe(root, padding='20 20 20 20', text='test')
lf.grid(row=6, column=6)
lf.columnconfigure(6, weight=1)
lf.rowconfigure(6, weight=1)
l = ttk.Label(lf, text = 'test').grid(column = 0, row = 0)
root.mainloop()
