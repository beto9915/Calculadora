import tkinter as tk
ventana_principal=tk.Tk()
ventana_principal.title("Calculadora basica, pero muy basica")
ventana_principal.geometry("1080x720")
etiqueta1=tk.Label(ventana_principal, text= "Ingrese numero 1: ")
etiqueta1.pack(pady=5)
entrada1=tk.Entry(ventana_principal)
entrada1.pack(pady=5)
etiqueta2=tk.Label(ventana_principal, text="Ingrese numero 2: ")
etiqueta2.pack(pady=5)
entrada2=tk.Entry(ventana_principal)
entrada2.pack(pady=5)
etiqueta3=tk.Label(ventana_principal, text="Resultado: ")
entrada1.focus()
def Suma():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())
    suma=numero1+numero2
    etiqueta3.config(text=suma)
def Resta():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())
    resta=numero1-numero2
    etiqueta3.config(text=resta)
def Multiplicacion():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())
    multiplicacion=numero1*numero2
    etiqueta3.config(text=multiplicacion)
def Division():
    numero1=float(entrada1.get())
    numero2=float(entrada2.get())
    if numero2==0:
        etiqueta3.config(text="No se puede dividir entre 0")
        return
    else:
        division=numero1/numero2
        etiqueta3.config(text=division)
def Limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta3.config(text="Resultado: ")
    entrada1.focus()


boton_suma=tk.Button(ventana_principal, text="+", command=Suma)
boton_suma.pack(pady=5)
boton_resta=tk.Button(ventana_principal, text="-", command=Resta)
boton_resta.pack(pady=5)
boton_multiplicacion=tk.Button(ventana_principal, text="*", command=Multiplicacion)
boton_multiplicacion.pack(pady=5)
boton_division=tk.Button(ventana_principal, text="/", command=Division)
boton_division.pack(pady=5)
etiqueta3.pack(pady=5)
boton_limpiar=tk.Button(ventana_principal, text="Limpiar", command=Limpiar)
boton_limpiar.pack(pady=5)

ventana_principal.mainloop()



