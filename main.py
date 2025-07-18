import customtkinter as ctk
# Asumo que vista.formulario_presupuesto y vista.formulario_recibo existen
# y son clases válidas de customtkinter.CTkFrame o similares.
from vista.formulario_presupuesto import FormularioPresupuesto
from vista.formulario_recibo import FormularioRecibo

class OfiDocsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("OfiDocs")

        # --- Lógica para posicionar la ventana en la mitad derecha ---
        # Obtener las dimensiones de la pantalla
        # Es importante llamar a update_idletasks() para asegurar que winfo_screenwidth()
        # y winfo_screenheight() devuelvan valores correctos al inicio.
        self.update_idletasks()
        screen_width = self.winfo_screenwidth() #Obtiene el ancho de la pantalla
        screen_height = self.winfo_screenheight() #Obtiene la altura de la pantalla

        # Imprimir las medidas de la pantalla en la consola
        print(f"Ancho de la pantalla: {screen_width} px")
        print(f"Altura de la pantalla: {screen_height} px")

        # Calcular las nuevas dimensiones para la ventana (que ocupe la mitad derecha completa de la pantalla)
        window_width = screen_width // 2
        window_height = screen_height
        print(f"Altura de la pantalla: {window_height} px")
        print(f"Altura de la pantalla: {window_width} px")

        # Calcular la posición X e Y para que la ventana inicie en la mitad derecha
        # La posición X se establece en la mitad del ancho de la pantalla,
        # lo que hace que la ventana comience justo en el centro horizontal y se extienda hacia la derecha.
        x_position = screen_width // 2
        y_position = 0 # Arriba de la pantalla

        # Establecer la geometría de la ventana: "ancho_x_alto+pos_x+pos_y"
        # Esto coloca la ventana para que ocupe toda la mitad derecha de la pantalla.
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        # --- Fin de la lógica de posicionamiento ---

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