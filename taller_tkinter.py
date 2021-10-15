import tkinter as tk
from tkinter import messagebox
import random


colors_rgb = ["red","blue","green"]
colors_custom = ["blue","pink","magenta","#5f0931"]

colors_actual = colors_rgb


## banderas
floor_on = False


ventana = tk.Tk()
ventana.title("Hola Mundo")
ventana.geometry("700x650")
ventana.config(bg="pink")
ventana.resizable(False,False)

pista_frame = tk.Frame(ventana,bg="#f8f2d8",height=500,width=500)

matriz = []

for i in range(4):
    fila = []
    for j in range(4):
        cuadro = tk.Label(pista_frame,bg="black",height=8,width=16)
        cuadro.grid(row=i,column=j,padx=10,pady=10)
        fila.append(cuadro)
    matriz.append(fila)

pista_frame.grid(row=0,column=0)

###########################################################

def start_dancing_floor():
    global matriz

    if floor_on == False:
        return
    for i in range(4):
        for j in range(4):
            matriz[i][j].config(bg=random.choice(colors_actual))

    ventana.after(1000,start_dancing_floor) 


def start_dancing():
    global floor_on
    floor_on = True
    start_dancing_floor()


def stop_dancing():
    global matriz
    global floor_on

    floor_on = False
    
    for i in range(4):
        for j in range(4):
            matriz[i][j].config(bg="black")

buttons_frame = tk.Frame(ventana,bg="red",height=50,width=100)

start_button = tk.Button(buttons_frame,text="Start",
                         command= lambda: start_dancing())
start_button.grid(row=0,column=0)

stop_button = tk.Button(buttons_frame,text="Stop",
                        command= lambda: stop_dancing())
stop_button.grid(row=0,column=1)

buttons_frame.grid(row=1,column=0)


######################################################
def random_colors():
    lista_random = []
        
    for i in range(5):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        color = "#%02x%02x%02x" % (r,g,b)
        lista_random.append(color)
        
    return lista_random

def set_colors(value):
    global colors_actual
    
    ## custom
    if value == 2:
        colors_actual = colors_custom
    ## random
    elif value==3:

        colors_actual = random_colors()
    ##default
    else:
        colors_actual = colors_rgb


option_frame = tk.Frame(ventana,height=700,width=200)



optionValue = tk.IntVar()
optionValue.set(1)

rgb_radio = tk.Radiobutton(option_frame,text="RGB(default)",
                           variable=optionValue,value=1,
                           command=lambda:set_colors(optionValue.get()))
rgb_radio.grid(row=0,column=0)

custom_radio = tk.Radiobutton(option_frame,text="Custom colors",
                           variable=optionValue,value=2,
                           command=lambda:set_colors(optionValue.get()))
custom_radio.grid(row=1,column=0)

random_radio = tk.Radiobutton(option_frame,text="5 random colors",
                           variable=optionValue,value=3,
                           command=lambda:set_colors(optionValue.get()))
random_radio.grid(row=2,column=0)

option_frame.grid(row=0,column=1)

###########################################################
def add_custom_colors():
    
    def change_custom(colores,ventana):
        global colors_custom
        global colors_actual

        if type(colores) == str:
            lista_colores = colores.split(",")
        elif type(colores) == list:
            lista_colores = colores
            
        colors_custom = lista_colores
        colors_actual = colors_custom

        ventana.destroy()
        ventana.update()

    def randomize_custom (ventana):
        change_custom(random_colors(),ventana)
        
    
    secundaria = tk.Toplevel(ventana)
    secundaria.title("Add Custom")
    secundaria.geometry("500x200")

    colores_label = tk.Label(secundaria,text="Colores actuales= " + str(colors_custom))
    colores_label.grid(row=0,column=0)

    colors_entry_value = tk.StringVar()
    
    colores_entry = tk.Entry(secundaria,textvariable=colors_entry_value)
    colores_entry.grid(row=1,column=1)


    update_button = tk.Button(secundaria,text="Update",
                              command=lambda:change_custom(colors_entry_value.get(),secundaria))
    update_button.grid(row=2,column=0)

    randomize_button = tk.Button(secundaria,text="Randomize",
                                 command= lambda:randomize_custom(secundaria))
    randomize_button.grid(row=2,column=1)    
    secundaria.mainloop()


def showMessage(titulo,mensaje):
    messagebox.showinfo(titulo,mensaje)
    

menubar = tk.Menu(ventana)

color_menu = tk.Menu(menubar,tearoff=0)

color_menu.add_command(label="Show actual colors",
                       command=lambda:showMessage("Colores Actuales",str(colors_actual)))
color_menu.add_command(label="Show custom colors",
                       command=lambda:showMessage("Colores Custom",str(colors_custom)))
color_menu.add_command(label="Show RGB colors",
                       command=lambda:showMessage("Colores RGB",str(colors_rgb)))
color_menu.add_command(label="Add custom colors",
                       command=lambda:add_custom_colors())

menubar.add_cascade(label="Colors",menu=color_menu )

info_menu = tk.Menu(menubar,tearoff=0)

info_menu.add_command(label="Acerca de",
                      command=lambda:showMessage("Acerca de","Creado para bailar sabrosamente"))

menubar.add_cascade(label="Info",menu=info_menu)


ventana.configure(menu=menubar)

ventana.mainloop()

