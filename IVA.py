from tkinter import *
from tkinter import ttk, messagebox

class CalculoIVA:
    __ventana=None
    def __init__(self):
        #Ventana
        self.__ventana = Tk()
        self.__ventana.resizable(0,0)
        self.__ventana.title("Calculo de IVA")
        label_1 = Label(self.__ventana, text="Cálculo de IVA", bg="#AED6F1")
        opts = {'ipadx': 10, 'ipady': 10}
        label_1.grid(row=0, column=0, columnspan=2, sticky="ew", **opts)
        separador = ttk.Separator(self.__ventana, orient=HORIZONTAL)
        separador.grid(row=1, column=0, columnspan=2, sticky="ew", **opts)

        self.__precio = StringVar()

        #Ingresar Precio
        label_2 = Label(self.__ventana, text="Precio sin IVA")
        label_2.grid(row=2, column=0, pady=10, padx=(10, 10), **opts)
        self.entry_Precio = ttk.Entry(self.__ventana, width=15, textvariable=self.__precio)
        self.entry_Precio.grid(row=2, column=1, padx=(0, 10), **opts)

        #Radio Button
        self.valorIva = IntVar()
        self.valorIva.set(-1)
        radio = ttk.Radiobutton(self.__ventana, text="IVA 21%", value=0, variable=self.valorIva)
        radio.grid(row=3, column=0, sticky="w", padx=(20, 10), **opts)
        radio2 = ttk.Radiobutton(self.__ventana, text="IVA 10.5%", value=1, variable=self.valorIva)
        radio2.grid(row=4, column=0, sticky="w", padx=(20, 10), **opts)

        #Marcos y Etiquetas de IVA y Precio con IVA
        label_2 = Label(self.__ventana, text="IVA")
        label_2.grid(row=6, column=0, padx=(10, 10), **opts)

        self.marco_resultado_iva = ttk.Frame(self.__ventana, style="TEntry", padding=10)
        self.marco_resultado_iva.grid(row=6, column=1, columnspan=2, padx=(0, 10), pady=10, sticky="ew")
        self.etiqueta_resultado_iva = Label(self.marco_resultado_iva)
        self.etiqueta_resultado_iva.pack()

        label_2 = Label(self.__ventana, text="Precio con IVA")
        label_2.grid(row=7, column=0, padx=(10, 10), **opts)

        self.marco_resultado_precio = ttk.Frame(self.__ventana, borderwidth=2, style="TEntry", padding=10)
        self.marco_resultado_precio.grid(row=7, column=1, columnspan=2, pady=10, padx=(0,10), sticky="ew")
        self.etiqueta_resultado_precio = Label(self.marco_resultado_precio)
        self.etiqueta_resultado_precio.pack()

        #Botones calcular y salir
        estilo_calcular = ttk.Style()
        estilo_calcular.configure('BotonVerde.TButton', background='green')
        btn_calcular = ttk.Button(self.__ventana, text="Calcular", command=self.cambiarValor,  style='BotonVerde.TButton')
        btn_calcular.grid(row=8, column=0, pady=10, padx=10)

        estilo_salir=ttk.Style()
        estilo_salir.configure("Salir.TButton", background="red")
        btn_salir = ttk.Button(self.__ventana, text="Salir", command=self.__ventana.quit, style="Salir.TButton")
        btn_salir.grid(row=8, column=1, pady=10, padx=10)

        self.entry_Precio.focus()

    def cambiarValor(self):
        if self.entry_Precio.get() != "":
            try:
                valor=float(self.entry_Precio.get())
                if self.valorIva.get() == 1:
                    iva = (valor * 10.5) / 100
                    precio = valor + iva
                else:
                    if self.valorIva.get() == 0:
                        iva = (valor * 21) / 100
                        precio = valor+iva
            except ValueError:
                messagebox.showerror(title="Error de tipo", message="Debe Ingresar un valor numerico")
                self.__precio.set("")
                

        self.etiqueta_resultado_iva.config(text=iva)
        self.etiqueta_resultado_precio.config(text=precio)

    def ejecutar(self):
        self.__ventana.mainloop()

if __name__=="__main__":
    ventana=CalculoIVA()
    ventana.ejecutar()
