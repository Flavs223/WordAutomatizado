import customtkinter as ctk
from vista.formulario_presupuesto import FormularioPresupuesto

class App:
    def __init__(self):
        ctk.set_appearance_mode("system")  # "light", "dark", "system"
        ctk.set_default_color_theme("blue")  # Puedes probar otros como "green", "dark-blue"
        self.ventana = None

    def iniciar_app(self):
        self.ventana = FormularioPresupuesto()
        self.ventana.mainloop()