from tkinter import *
import tkinter.font as font
from tkinter import ttk
import math
def mainFunction():
    calc_his = []
    def history():
        def history_open():
            en.config(state="normal")
            en.delete(0, END)
            act = listbox.get(ACTIVE)
            fin = act.find(" ", 1)
            tinp = act[1:fin]
            en.insert(END, tinp)
            root_his.destroy()
            en.config(state="readonly", readonlybackground = "white")
        def clear_all():
            def can():
                root_error.destroy()
            def delt():
                del calc_his[:]
                listbox.delete(0, END)
                root_error.destroy()
            root_error = Tk()
            root_error.iconbitmap(default='icon.ico')
            root_error.title("Calculator")
            root_error.resizable(0, 0)
            root_error.geometry('%dx%d+%d+%d' % (153, 102, 606.5, 340.5))
            l1 = Label(root_error, background = "#ff8080", text = "Are you sure you want to clear all?", wraplength = 95).grid(row = 0, column = 0, columnspan = 2, ipady = 15, sticky = EW)
            b1 = Button(root_error, text = "Ok", height = 1, width = 8, command = delt).grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)
            b2 = Button(root_error, text = "Cancel", height = 1, width = 8, command = can).grid(row = 1, column = 1, sticky = E, padx = 5, pady = 5)
            root_error.mainloop()
        root_his = Tk()
        root_his.iconbitmap(default='icon.ico')
        root_his.title("History")
        root_his.resizable(0,0)
        root_his.geometry('%dx%d+%d+%d' % (195, 213, 592.5, 277.5))
        listbox = Listbox(root_his)
        scrollbar = Scrollbar(root_his, orient=VERTICAL)
        scrollbar2 = Scrollbar(root_his, orient=HORIZONTAL)
        btt1 = Button(root_his, text = "Open", height = 1, width = 11, command = history_open)
        btt2 = Button(root_his, text = "Cear all", height = 1, width = 11, command = clear_all)
        listbox.grid(row = 1, column = 1, ipadx = 28, columnspan = 2, sticky = W)
        scrollbar.grid(row = 1, column = 2, sticky = N+S+E, padx = (90, 0))
        scrollbar2.grid(row = 2, column = 1, sticky = E+W, columnspan = 2)
        btt1.grid(row = 3, column = 1, sticky = W, pady = (5, 0))
        btt2.grid(row = 3, column = 2, sticky = E, pady = (5, 0))
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        listbox.config(xscrollcommand = scrollbar2.set)
        scrollbar2.config(command = listbox.xview)
        calc_his.reverse()
        for i in calc_his:
           listbox.insert(END, " " + i +" ")
        root_his.mainloop()
    def key_press(event):
        en.config(state="normal")
        key = event.char
        en.insert(END, key)
        en.config(state="readonly", readonlybackground = "white")
    def inpnum(data):
        en.config(state="normal")
        en.insert(END, data)
        en.config(state="readonly", readonlybackground = "white")
    def inpc(data):
        en.config(state="normal")
        da = en.get()
        if da == "":
            pass
        else:
            en.insert(END, data)
        en.config(state="readonly", readonlybackground = "white")
    def equal(event):
        try:
            en.config(state="normal")
            data = en.get()
            en.delete(0, END)
            ans = eval(data)
            lab.configure(text = data + " ")
            en.insert(END, ans)
            towrite = str(data) + " " + "=" + " " + str(ans) + "\n"
            calc_his.append(towrite)
            en.config(state="readonly", readonlybackground = "white")
        except:
            pass
    def equal_os():
        try:
            en.config(state="normal")
            data = en.get()
            en.delete(0, END)
            ans = eval(data)
            lab.configure(text = data + " ")
            en.insert(END, ans)
            towrite = str(data) + " " + "=" + " " + str(ans) + "\n"
            calc_his.append(towrite)
            en.config(state="readonly", readonlybackground = "white")
        except:
            pass
    def clear(event):
        en.config(state="normal")
        en.delete(0, END)
        lab.configure(text = "")
        en.config(state="readonly", readonlybackground = "white")
    def dele(event):
        en.config(state="normal")
        data = en.get()
        st = len(data)-1
        en.delete(st, END)
        en.config(state="readonly", readonlybackground = "white")
    def clear_os():
        en.config(state="normal")
        en.delete(0, END)
        lab.configure(text = "")
        en.config(state="readonly", readonlybackground = "white")
    def dele_os():
        en.config(state="normal")
        data = en.get()
        st = len(data)-1
        en.delete(st, END)
        en.config(state="readonly", readonlybackground = "white")
    def sRoot():
        try:
            en.config(state="normal")
            data = en.get()
            if data == "":
                pass
            else:
                lab.configure(text = "√"+data+" ")
                en.delete(0, END)
                en.insert(END, math.sqrt(int(data)))
            en.config(state="readonly", readonlybackground = "white")
        except:
            pass
    def neg():
        try:
            en.config(state="normal")
            mdata = en.get()
            if mdata == "":
                pass
            else:
                data = list(mdata)
                tot = len(data)
                if "-" not in data and "+" not in data and "*" not in data and "/" not in data:
                    en.insert(0, "-")
                else:
                    for i in data:
                        tot = tot-1
                        if data[tot] == "+" or data[tot] == "/" or data[tot] == "*" or data[tot] == "-":
                            en.insert(tot+1, "-")
            en.config(state="readonly", readonlybackground = "white")
        except:
            pass
    global en
    global lab
    root = Tk()
    root.iconbitmap(default='icon.ico')
    root.resizable(0,0)
    root.title("Calculator")
    root.configure(bg = "green")
    men = Menu()
    root.config(menu = men)
    hisMenu = Menu(men, tearoff=0)
    men.add_cascade(label = "Menu", menu = hisMenu)
    hisMenu.add_command(label = "History", command = history)
    w = 298
    h = 465
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    btFont = font.Font(size = 11)
    pointFont = font.Font(size = 11, weight = "bold")
    enFont = font.Font(size = 15)
    numFont = font.Font(size = 11, weight = "bold")
    lab = Label(root, text = "Welcome ", bg = "white", anchor=E)
    en = Entry(root, relief = FLAT, readonlybackground ="white",state="readonly")
    scroll = Scrollbar(root, orient=HORIZONTAL)
    bt1 = Button(root, text = "CE", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = clear_os)
    bt2 = Button(root, text = "D", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = dele_os)
    bt3 = Button(root, text = "√", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = sRoot)
    bt4 = Button(root, text = "/", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = lambda: inpc("/"))

    bt5 = Button(root, text = "7", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("7"), background = "#bfbfbf")
    bt6 = Button(root, text = "8", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("8"), background = "#bfbfbf")
    bt7 = Button(root, text = "9", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("9"), background = "#bfbfbf")
    bt8 = Button(root, text = "x", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = lambda: inpc("*"))

    bt9 = Button(root, text = "4", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("4"), background = "#bfbfbf")
    bt10 = Button(root, text = "5", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("5"), background = "#bfbfbf")
    bt11 = Button(root, text = "6", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("6"), background = "#bfbfbf")
    bt12 = Button(root, text = "-", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = lambda: inpc("-"))

    bt13 = Button(root, text = "1", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("1"), background = "#bfbfbf")
    bt14 = Button(root, text = "2", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("2"), background = "#bfbfbf")
    bt15 = Button(root, text = "3", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("3"), background = "#bfbfbf")
    bt16 = Button(root, text = "+", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = lambda: inpc("+"))

    bt17 = Button(root, text = "±", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = neg)
    bt18 = Button(root, text = "0", height = 3, width = 7, relief = FLAT, command = lambda: inpnum("0"), background = "#bfbfbf")
    bt19 = Button(root, text = ".", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = lambda: inpnum("."))
    bt20 = Button(root, text = "=", height = 3, width = 7, relief = FLAT, background = "#e6e6e6", command = equal_os)

    en['font'] = enFont

    bt1['font'] = btFont
    bt2['font'] = btFont
    bt3['font'] = btFont
    bt4['font'] = btFont

    bt8['font'] = btFont
    bt7['font'] = btFont
    bt6['font'] = btFont
    bt5['font'] = btFont

    bt9['font'] = btFont
    bt10['font'] = btFont
    bt11['font'] = btFont
    bt12['font'] = btFont

    bt13['font'] = btFont
    bt14['font'] = btFont
    bt15['font'] = btFont
    bt16['font'] = btFont

    bt17['font'] = btFont
    bt18['font'] = btFont
    bt19['font'] = btFont
    bt20['font'] = btFont
    lab.grid(row = 0, column = 0, columnspan = 2, sticky = EW)
    en.grid(row = 1, column = 0, ipadx = 37, ipady = 35, columnspan = 2)
    scroll.grid(row = 2, column = 0, sticky = E+W, columnspan = 2)
    bt1.grid(row = 3, column = 0, columnspan = 2, sticky = W, pady = (2, 0))
    bt2.grid(row = 3, column = 1, columnspan = 2, sticky = W, padx = (0, 150), pady = (2, 0))
    bt3.grid(row = 3, column = 1, columnspan = 2, sticky = W, padx = (75, 0), pady = (2, 0))
    bt4.grid(row = 3, column = 0, columnspan = 2, sticky = E, pady = (2, 0))

    bt5.grid(row = 4, column = 0, columnspan = 2, sticky = W, pady = (2, 0))
    bt6.grid(row = 4, column = 1, columnspan = 2, sticky = W, padx = (0, 150), pady = (2, 0))
    bt7.grid(row = 4, column = 1, columnspan = 2, sticky = W, padx = (75, 0), pady = (2, 0))
    bt8.grid(row = 4, column = 0, columnspan = 2, sticky = E, pady = (2, 0))

    bt9.grid(row = 5, column = 0, columnspan = 2, sticky = W, pady = (2, 0))
    bt10.grid(row = 5, column = 1, columnspan = 2, sticky = W, padx = (0, 150), pady = (2, 0))
    bt11.grid(row = 5, column = 1, columnspan = 2, sticky = W, padx = (75, 0), pady = (2, 0))
    bt12.grid(row = 5, column = 0, columnspan = 2, sticky = E, pady = (2, 0))

    bt13.grid(row = 6, column = 0, columnspan = 2, sticky = W, pady = (2, 0))
    bt14.grid(row = 6, column = 1, columnspan = 2, sticky = W, padx = (0, 150), pady = (2, 0))
    bt15.grid(row = 6, column = 1, columnspan = 2, sticky = W, padx = (75, 0), pady = (2, 0))
    bt16.grid(row = 6, column = 0, columnspan = 2, sticky = E, pady = (2, 0))

    bt17.grid(row = 7, column = 0, columnspan = 2, sticky = W, pady = (2, 0))
    bt18.grid(row = 7, column = 1, columnspan = 2, sticky = W, padx = (0, 150), pady = (2, 0))
    bt19.grid(row = 7, column = 1, columnspan = 2, sticky = W, padx = (75, 0), pady = (2, 0))
    bt20.grid(row = 7, column = 0, columnspan = 2, sticky = E, pady = (2, 0))

    en.config(xscrollcommand = scroll.set)
    scroll.config(command = en.xview)
    root.bind('<Return>', equal)
    root.bind('<Key>', lambda a : key_press(a))
    root.bind('<BackSpace>', dele)
    root.bind('<Delete>', clear)
    root.mainloop()
if __name__ == '__main__':
    try:
        mainFunction()
    except:
        pass
