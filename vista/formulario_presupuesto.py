import customtkinter as ctk

class FormularioPresupuesto(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Generador de Presupuestos")
        self.geometry("800x600")

        self.crear_widgets()

    def crear_widgets(self):
        ctk.CTkLabel(self, text="Nombre de la empresa:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entrada_empresa = ctk.CTkEntry(self, width=300)
        self.entrada_empresa.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(self, text="Atención a:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entrada_atencion = ctk.CTkEntry(self, width=300)
        self.entrada_atencion.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(self, text="Proyecto:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.combo_proyecto = ctk.CTkComboBox(self, values=["RED", "CCTV", "AUDIO", "TELEFONÍA"])
        self.combo_proyecto.grid(row=2, column=1, padx=10, pady=10)

        self.boton_generar = ctk.CTkButton(self, text="Generar documento", command=self.generar_documento)
        self.boton_generar.grid(row=4, column=0, columnspan=2, pady=20)

    def generar_documento(self):
        empresa = self.entrada_empresa.get()
        atencion = self.entrada_atencion.get()
        proyecto = self.combo_proyecto.get()
        print(f"[DEBUG] Generando documento para {empresa}, atención: {atencion}, proyecto: {proyecto}")
