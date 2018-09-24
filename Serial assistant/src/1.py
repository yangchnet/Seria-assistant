from tkinter import *

root = Tk()

text1 = Text(root,width=30,height=2)
text1.pack()
text1.insert(INSERT,'I love you')

def show():
     print('吆喝，我被点了一下')
#text还可以插入按钮  图片等
b1 = Button(text1,text='点我点我',command=show)
#在text创建组件的命令
text1.window_create(INSERT,window=b1)

mainloop()