import customtkinter as ctk

class FormularioRecibo(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Formulario de Recibo", font=("Arial", 18, "bold")).pack(pady=10)

        self.bueno_por = ctk.CTkEntry(self, placeholder_text="Bueno por: (ej. $200.00)")
        self.bueno_por.pack(pady=5)

        self.recibi_de = ctk.CTkEntry(self, placeholder_text="Recibí de:")
        self.recibi_de.pack(pady=5)

        self.cantidad_texto = ctk.CTkEntry(self, placeholder_text="La cantidad de: (en texto)")
        self.cantidad_texto.pack(pady=5)

        self.concepto = ctk.CTkEntry(self, placeholder_text="Por concepto de:")
        self.concepto.pack(pady=5)

        self.fecha = ctk.CTkEntry(self, placeholder_text="Fecha: (ej. 14 de julio de 2025)")
        self.fecha.pack(pady=5)

        ctk.CTkButton(self, text="Vista previa").pack(pady=5)
        ctk.CTkButton(self, text="Generar documento").pack(pady=5)
        ctk.CTkButton(self, text="Imprimir").pack(pady=5)
