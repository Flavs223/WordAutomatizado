import customtkinter as ctk
from vista.componentes_gui import BotonPrincipal, CampoTexto

class FormularioPresupuesto(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Formulario de Presupuesto", font=("Arial", 18)).pack(pady=10)

        self.entrada_empresa = CampoTexto(self, "Nombre de la empresa")
        self.entrada_empresa.pack(pady=5)

        self.entrada_atencion = CampoTexto(self, "Atención a:")
        self.entrada_atencion.pack(pady=5)

        self.boton_generar = BotonPrincipal(self, "Generar Presupuesto", comando=self.generar_documento)
        self.boton_generar.pack(pady=10)

    def generar_documento(self):
        print("[DEBUG] Generando documento de presupuesto...")