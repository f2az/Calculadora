from tkinter import *
from math import *
from tkinter import ttk

raiz = Tk()
raiz.title("Calculadora binaria")

raiz.geometry("230x210")
raiz.resizable(False,False)
raiz.configure(background="azure3")

colorBtn = "light yellow"
anchoBtn = 5
operador = ""
num1 = ""
num2 = ""
numero = ""
cond = 1
txtPantalla = StringVar()

#Funcion para limpiar la pantalla
def clear():
    global operador
    global numero
    global cond
    
    numero = ""
    operador = ""
    cond = 1
    txtPantalla.set("0")

#Funcion para mostrar el contenido del boton
def click(num):
    global operador
    global numero
    numero = numero + str(num)
    txtPantalla.set(numero)

#Funcion para mostrar el contenido de la operacion
def clickOp(num):
    global operador
    global numero
    global num1
    global cond

    if (cond == 1):
        num1 = str(int(numero, 2))
        numero = ""
        cond = cond + 1  
    operador = str(num)
    txtPantalla.set(operador)
    

#Funcion para determinar y mostrar el resultado
def resultado():
    global operador
    global numero
    global num1
    global result
    num2 = str(int(numero, 2))
    cadena = num1 + operador + num2

    try:
        result = str(eval(cadena))
    except:
        result="Math Error"

    result = bin(int(result))
    txtPantalla.set(result)

def tecladoOp(event):
    clickOp()

def tecladoNum(event):
    click()

clear()

Pantalla = Entry(raiz, font=("arial", 20, "bold"), width = 12, background="floral white", textvariable = txtPantalla)
Pantalla.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10, sticky = (W, E))

ttk.Label(raiz, text = "   ", background = "azure3").grid(row = 1, column =0)
ttk.Label(raiz, text = "   ", background = "azure3").grid(row = 1, column =3)

#Botones de la primera fila
Btn0 = Button(raiz, font=("arial", 15), text = "0", bg = colorBtn, width = anchoBtn, command=lambda:click(0)).grid(row=1,column=1, padx = 1, pady=4)
Btn1 = Button(raiz, font=("arial", 15), text = "1", bg = colorBtn, width = anchoBtn, command=lambda:click(1)).grid(row=1,column=2, padx = 1, pady=4)

#Botones de la segunda fila
Btncle = Button(raiz, font=("arial", 15), text = "C", bg = colorBtn, width = anchoBtn, command=clear).grid(row=2,column=1, padx = 1, pady=4)
Btnigu = Button(raiz, font=("arial", 15), text = "=", bg = colorBtn, width = anchoBtn, command=resultado).grid(row=2,column=2, padx = 1, pady=4)

#Botones de la tercera fila
Btnsum = Button(raiz, font=("arial", 15), text = "+", bg = colorBtn, width = anchoBtn, command=lambda:clickOp("+")).grid(row=3,column=1, padx = 1, pady=1)
Btnres = Button(raiz, font=("arial", 15), text = "-", bg = colorBtn, width = anchoBtn, command=lambda:clickOp("-")).grid(row=3,column=2, padx = 1, pady=1)

#Si el usuario presiona el teclado es lo mismo que presionar los botones creados
raiz.bind('<KP_Enter>', lambda event: resultado())
raiz.bind('<KP_0>', lambda event: click(0))
raiz.bind('<KP_1>', lambda event: click(1))

raiz.bind('<KP_Add>', lambda event: clickOp("+"))
raiz.bind('<KP_Subtract>', lambda event: clickOp("-"))

raiz.mainloop()
