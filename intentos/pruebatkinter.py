import tkinter

win1 = tkinter.Tk()
win1.geometry("600x600")
win1.colormapwindows()


def saludo():
    print("Hola tu nombre es: ?")

    
label1 = tkinter.Label(win1, text = "Hola mundo", bg = "#00FFFF")
label1.pack()

boton1 = tkinter.Button(win1, text = "Presiona", padx = 50, pady = 20, command = saludo)
boton1.pack()

caja = tkinter.Entry(win1)
caja.pack()

win1.mainloop()