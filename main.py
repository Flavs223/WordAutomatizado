import customtkinter as ctk
from vista.formulario_presupuesto import FormularioPresupuesto
from vista.formulario_recibo import FormularioRecibo

class OfiDocsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("OfiDocs")
        self.geometry("800x600")

        self.frame_contenido = ctk.CTkFrame(self)
        self.frame_contenido.pack(fill="both", expand=True)

        self.formulario_actual = None
        self.mostrar_formulario("Presupuesto")

    def mostrar_formulario(self, tipo):
        if self.formulario_actual:
            self.formulario_actual.destroy()
        if tipo == "Presupuesto":
            self.formulario_actual = FormularioPresupuesto(self.frame_contenido)
        elif tipo == "Recibo":
            self.formulario_actual = FormularioRecibo(self.frame_contenido)
        self.formulario_actual.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = OfiDocsApp()
    app.mainloop()