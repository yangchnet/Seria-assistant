from tkinter import *
from tkinter import ttk

root = Tk()  # 定义主窗口

content = ttk.Frame(root, padding=(3, 3, 12, 12))  # 内容帧
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)  # 定义内容帧
namelbl = ttk.Label(content, text="Name")  # 内容帧添加label
name = ttk.Entry(content)  # 内容帧添加entry

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, rowspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=2)
two.grid(column=1, row=2)
three.grid(column=2, row=2)
ok.grid(column=3, row=2)
cancel.grid(column=4, row=2)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=2)
content.columnconfigure(4, weight=2)
content.rowconfigure(1, weight=1)
root.mainloop()
