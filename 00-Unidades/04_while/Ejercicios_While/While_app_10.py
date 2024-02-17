import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lucca
apellido: Trovato
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0
        contador_negativo = 0
        contador_de_ceros = 0
        acumulador = 0 
        acumulador_negativo = 0

        while True:
            numero = prompt("Numero", "Ingrese un numero")
            if numero == None:
                break
            numero = int(numero)
            
            if numero < 0:
                acumulador_negativo = numero + acumulador_negativo
            else:
                acumulador += numero
            
            if numero > 0:
                contador += 1
            elif numero < 0:
                contador_negativo += 1
            else:
                contador_de_ceros += 1
            
            diferencia = acumulador + acumulador_negativo
            
            
            
            

        alert("Mensaje",f"La suma de los negativos es: {acumulador_negativo}\nLa suma acumulada de los positivos es: {acumulador} \nCantidad de números positivos ingresados es: {contador} \nCantidad de números negativos ingresados es: {contador_negativo} \nCantidad de ceros es: {contador_de_ceros} \nDiferencia entre la cantidad de los números positivos y negativos es: {diferencia}" )


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
