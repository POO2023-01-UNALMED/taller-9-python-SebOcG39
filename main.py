from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=50, padx=1, pady=1)

# Configuración oyentes
operador = False
operacion = ''
num1 = ''
num2 = ''

def Numero(evento):
    global num1, num2

    num = evento.widget['text']

    if not operador:
        num1 += num
        pantalla.delete(0, 'end')
        pantalla.insert('end', num1)
    else:
        num2 += num
        pantalla.delete(0, 'end')
        pantalla.insert('end', num2)


def Operador(evento):
    global operador, operacion

    operador = True
    operacion = evento.widget['text']
    pantalla.delete(0, 'end')

def Resultado(evento):
    global num1, num2, operador, operacion

    resultado = 0

    if num2!='':
        if operacion=='+':
            resultado = float(num1)+float(num2)
        elif operacion=='-':
            resultado = float(num1)-float(num2)
        elif operacion=='*':
            resultado = float(num1)*float(num2)
        elif operacion=='/':
            resultado = float(num1)/float(num2)
    else:
        resultado = float(num1)
    
    pantalla.delete(0, 'end')
    if resultado.is_integer():
        resultado = int(resultado)
    pantalla.insert('end', str(resultado))
    num1 = ''
    num2 = ''
    operacion = ''
    operador = False

def Punto(evento):
    global num1, num2, operador
    if not operador:
        if num1=='':
            num1 += '0.'
        else:
            num1 += '.'
        pantalla.delete(0, 'end')
        pantalla.insert('end', num1)
    else:
        if num2=='':
            num2 += '0.'
        else:
            num2 += '.'
        pantalla.delete(0, 'end')
        pantalla.insert('end', num2)
    


# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_1.bind('<Button-1>',Numero)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_2.bind('<Button-1>',Numero)

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_3.bind('<Button-1>',Numero)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_4.bind('<Button-1>',Numero)

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_5.bind('<Button-1>',Numero)

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_6.bind('<Button-1>',Numero)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_7.bind('<Button-1>',Numero)

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_8.bind('<Button-1>',Numero)

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_9.bind('<Button-1>',Numero)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_igual.bind('<Button-1>',Resultado)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_punto.bind('<Button-1>', Punto)

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_mas.bind('<Button-1>',Operador)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_menos.bind('<Button-1>',Operador)

boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion.bind('<Button-1>',Operador)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)
boton_division.bind('<Button-1>',Operador)


root.mainloop()