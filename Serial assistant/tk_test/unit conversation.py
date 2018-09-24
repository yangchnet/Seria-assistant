from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


root = Tk()  # 创建一个窗口对象
root.title("Feet to Meters")  # 设置标题

mainframe = ttk.Frame(root, padding='3 3 12 12')  # Frame(父窗口， 框架内部和内部小部件外部之间距离（左，上，右，下）)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))  # 放置于第一行，第二列，居中

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meter").grid(column=3, row=2, sticky=W)
#
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)  # 不使用此句，则每个网格中正好放下控件，使用后空间变大

feet_entry.focus()
root.bind('<Return>', calculate)  # 绑定事件

root.mainloop()
