def prework():
    import tkinter as tk
    from PIL import Image, ImageTk
    m=Image.open("merlin.jpg")
    p=Image.open("percival.jpg")
    g=Image.open("good.jpg")
    b=Image.open("bad.jpg")
    a=Image.open("assassin.jpg")
    mo=Image.open("morgana.jpg")
    merlin=ImageTk.PhotoImage(m)
    percival=ImageTk.PhotoImage(p)
    good=ImageTk.PhotoImage(g)
    assassin=ImageTk.PhotoImage(a)
    morgana=ImageTk.PhotoImage(mo)
    label1=tk.Label(image=merlin)
    label1.image=merlin
    label2=tk.Label(image=percival)
    label2.image=percival
    label3=tk.Label(image=good)
    label3.image=good
    label4=tk.Label(image=assassin)
    label4.image=assassin
    label5=tk.Label(image=morgana)
    label5.image=morgana
    #label1 = tk.Label(image=image)
    #label1 = tk.Label(win, text='net file :')
    label1.grid(column=0, row=15)
    label2.grid(column=2, row=15)
    label3.grid(column=3, row=15)
    label4.grid(column=5, row=15)
    label5.grid(column=6, row=15)