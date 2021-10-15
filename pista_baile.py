import tkinter as tk
from tkinter import messagebox
import random
from tkinter.constants import W

color_fondo = "#f8f2d8"
button_fondo = "#ffcf00"
color_off = "#1c1c1a"
color_options = "#2c0061"

color_rgb = ["red","green","blue"]
color_custom = ["green","yellow","cyan"]
color_custom_change =[]


## lista de colores actual
color_actual = color_rgb

cantidad_colores_maximo = 5

floor_on = False

dimension_matriz = 4


# Configuración de la raíz
root = tk.Tk()
root.title("Hola mundo")
root.geometry("700x650")
root.config(bg=color_options)
root.resizable(False,False)

################################################################################
## Creación de pista
################################################################################
frame = tk.Frame(root,bg=color_fondo,height=500,width=500)
matriz = []
for i in range(dimension_matriz):
    fila = []
    for j in range(dimension_matriz):
        label = tk.Label(frame,text='',
                        bg=color_off,
                        justify=tk.CENTER,
                        width=16,height=8)
        label.grid(row=i,column=j,padx=10,pady=10)
        fila.append(label)
    matriz.append(fila)

frame.grid(row=0,column=0)


################################################################################
## Funciones de botones start y Stop
################################################################################
def paint_dancing_floor():
    global matriz

    if floor_on == False:
        return 
    for i in range(dimension_matriz):
        for j in range(dimension_matriz):
            color_random = random.choice(color_actual)
            matriz[i][j].configure(bg=color_random)
    root.after(1000,paint_dancing_floor) # cada 1000ms 

def start_dancing_floor():
    global floor_on
    floor_on = True
    paint_dancing_floor()

def stop_dancing_floor():
    global floor_on
    floor_on = False
    for i in range(dimension_matriz):
            for j in range(dimension_matriz):
                matriz[i][j].configure(bg=color_off)
                
start_stop_frame = tk.Frame(root,bg=button_fondo,height=550,width=550)

start_button = tk.Button(start_stop_frame, text="Start",
                        command= lambda:start_dancing_floor())
start_button.grid(row=0,column=0,padx=50,pady=5)

start_button = tk.Button(start_stop_frame, text="Stop",
                        command= lambda:stop_dancing_floor())
start_button.grid(row=0,column=1,padx=50,pady=5)

start_stop_frame.grid()

################################################################################
## Funciones de opciones de colores
################################################################################
def get_random_colors():
    colores_random = []
    for i in range(cantidad_colores_maximo):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        colores_random.append('#%02x%02x%02x' % (r, g, b))
    return colores_random

def select_colors():
    global color_actual
    if opcion_color.get() == 2:
        color_actual = color_custom
    elif opcion_color.get() == 3:
        color_actual = get_random_colors()
    else:
        color_actual = color_rgb

color_option_frame = tk.Frame(root,bg=color_options,height=700,width=200)
color_option_frame.grid(row=0,column=1)

opcion_color = tk.IntVar()
opcion_color.set(1)
rgb_radio_button = tk.Radiobutton(color_option_frame,text="RGB(default)",
                                  variable=opcion_color, value=1,
                                  command=select_colors)
rgb_radio_button.pack(anchor = W,padx=10,pady=20)

custom_radio_button = tk.Radiobutton(color_option_frame,text="Custom Colors",
                                  variable=opcion_color, value=2,
                                  command=select_colors)
custom_radio_button.pack(anchor = W,padx=10,pady=20)

random_radio_button = tk.Radiobutton(color_option_frame,text="5 Random Colors",
                                  variable=opcion_color, value=3,
                                  command=select_colors)
random_radio_button.pack(anchor = W,padx=10,pady=20)


################################
###### Menus
################################
def showMensaje(titulo,mensaje):
    messagebox.showinfo(titulo,mensaje)

def change_custom_colors():
    
    def change_colors(colores,window):
        global color_custom
        global color_actual
        if type(colores) == str:
            color_custom = colores.split(',')
        elif type(colores) == list:
            color_custom = colores
        color_actual = color_custom
        window.destroy()
        window.update()

    custom_window = tk.Toplevel(root)
    custom_window.geometry("500x200")
    color_label = tk.Label(custom_window,text="Colores actuales: "+ str(color_custom))
    color_label.grid(row=0,column=0)

    new_color_label = tk.Label(custom_window,text="Ingrese nuevos colores (separados por comas ','): ")
    new_color_label.grid(row=1,column=0)

    colores_var = tk.StringVar()
    coloresEntry = tk.Entry(custom_window,textvariable=colores_var)
    coloresEntry.grid(row=1,column=1)

    new_custom_label = tk.Label(custom_window,text="Formato: 'blue','green',etc o hex: #ffffff ")
    new_custom_label.grid(row=2,column=0)

    update_button = tk.Button(custom_window, text="Update", command=lambda:change_colors(colores_var.get(),custom_window))
    update_button.grid(row=3,column=0)
    randomize_button = tk.Button(custom_window, text="5 Random colors", command=lambda:change_colors(get_random_colors(),custom_window))
    randomize_button.grid(row=3,column=1)

    custom_window.mainloop()

menubar = tk.Menu(root)
colormenu = tk.Menu(menubar,tearoff=0)
colormenu.add_command(label="Show RGB Colors",command=lambda: showMensaje("Colores RGB",str(color_rgb)))
colormenu.add_command(label="Show Custom Colors",command=lambda: showMensaje("Colores Personalizados",str(color_custom)))
colormenu.add_command(label="Add Custom Colors",command=change_custom_colors )
colormenu.add_command(label="Show Actual Colors",command=lambda: showMensaje("Colores en pantalla",str(color_actual)))

menubar.add_cascade(label="Colors",menu=colormenu)

def show_info():
    return """Creado por Zhong Liu
              Una pista de baile que cambia de colores.
              Disfruten el baile
              """

infomenu = tk.Menu(menubar,tearoff=0)
infomenu.add_command(label="Acerca de",command=lambda:showMensaje("Acerca de",show_info()))

menubar.add_cascade(label="Info",menu=infomenu)

root.configure(menu=menubar)

# Finalmente bucle de la aplicación
root.mainloop()