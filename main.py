#Librerías necesarias
import customtkinter as ctk
from vista.formulario_presupuesto import FormularioPresupuesto
from vista.formulario_recibo import FormularioRecibo

class OfiDocsApp(ctk.CTk): # Clase principal de la aplicación
    def __init__(self): # Constructor de la clase
        super().__init__()# Inicializar la clase base CTk
        self.title("OfiDocs - Generador de Documentos")  #Titulo de la ventana
        self.geometry("900x650") #Dimensiones de la ventana
        self.resizable(False, False) # No permitir redimensionamiento

        # Menú de selección
        self.label_titulo = ctk.CTkLabel(self, text="Selecciona el tipo de documento:", font=("Arial", 16)) # Etiqueta de título 
        self.label_titulo.pack(pady=10) # Espaciado vertical
        
        # Crear un menú desplegable para seleccionar el tipo de documento
        self.opciones = ctk.CTkOptionMenu(self, values=["Presupuesto", "Recibo"], command=self.mostrar_formulario)# Menú desplegable para seleccionar el tipo de documento 
        self.opciones.pack(pady=10) # Espaciado vertical
        self.opciones.set("Presupuesto") # Establecer valor por defecto

        # Frame dinámico para cargar formulario
        self.frame_contenido = ctk.CTkFrame(self, corner_radius=10)# Frame para contener los formularios
        self.frame_contenido.pack(pady=10, padx=20, fill="both", expand=True) # Espaciado y expansión del frame

        # Inicializar el formulario actual
        self.formulario_actual = None # Inicializar el formulario actual como None
        self.mostrar_formulario("Presupuesto") # Mostrar el formulario de presupuesto por defecto

    def mostrar_formulario(self, seleccion): # Método para mostrar el formulario seleccionado
        # Elimina formulario anterior
        for widget in self.frame_contenido.winfo_children(): # Eliminar widgets del frame
            widget.destroy() #  Destruir widget

        # Cargar el formulario correspondiente
        if seleccion == "Presupuesto": # Si la selección es presupuesto
            self.formulario_actual = FormularioPresupuesto(self.frame_contenido) #  Crear instancia del formulario de presupuesto
        elif seleccion == "Recibo": # Si la selección es recibo
            self.formulario_actual = FormularioRecibo(self.frame_contenido) # Crear instancia del formulario de recibo
        
        #Sale de escena el formulario según la selección
        self.formulario_actual.pack(fill="both", expand=True) # Empaquetar el formulario actual para que ocupe todo el espacio disponible

# Ejecutar la aplicación
if __name__ == "__main__": # Punto de entrada de la aplicación
    ctk.set_appearance_mode("light")  #Modo oscuro "dark" o claro "light"    
    ctk.set_default_color_theme("blue") # Establecer tema de color por defecto
    app = OfiDocsApp() # Crear instancia de la aplicación
    app.mainloop()  # Iniciar el bucle principal de la aplicación
