import tkinter as tk
ventana_principal=tk.Tk()
ventana_principal.title("Calculadora basica, pero muy basica")
ventana_principal.geometry("1080*720")
etiqueta1=tk.Label(ventana_principal, text= "Ingrese numero 1: ")
etiqueta1.pack(pady=5)
entrada1=tk.Entry(ventana_principal)
entrada1.pack(pady=5)
etiqueta2=tk.Label(ventana_principal, text="Ingrese numero 2: ")
etiqueta2.pack(pady=5)
entrada2=tk.Entry(ventana_principal)
entrada2.pack(pady=5)
etiqueta3=tk.Label(ventana_principal, text="Resultado: ")
etiqueta3.pack(pady=5)
def Suma():
    numero1=entrada1.get()
    numero2=entrada2.get()
    suma=numero1+numero2

def Resta():
    numero1=entrada1.get()
    numero2=entrada2.get()
    resta=numero1-numero2
def Multiplicacion():
    numero1=entrada1.get()
    numero2=entrada2.get()
    multiplicacion=numero1*numero2
def Division():

    pass



