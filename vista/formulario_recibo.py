import customtkinter as ctk
from vista.componentes_gui import BotonPrincipal, CampoTexto

class FormularioRecibo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Formulario de Recibo", font=("Arial", 18)).pack(pady=10)

        self.entrada_nombre = CampoTexto(self, "Recibí de:")
        self.entrada_nombre.pack(pady=5)

        self.entrada_concepto = CampoTexto(self, "Por concepto de:")
        self.entrada_concepto.pack(pady=5)

        self.boton_generar = BotonPrincipal(self, "Generar Recibo", comando=self.generar_recibo)
        self.boton_generar.pack(pady=10)

    def generar_recibo(self):
        print("[DEBUG] Generando recibo...")