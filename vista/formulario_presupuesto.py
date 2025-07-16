import customtkinter as ctk

class FormularioPresupuesto(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Formulario de Presupuesto", font=("Arial", 18, "bold")).pack(pady=10)

        # Sección de datos generales
        self.empresa_entry = ctk.CTkEntry(self, placeholder_text="Nombre de la empresa")
        self.empresa_entry.pack(pady=5)

        self.atencion_entry = ctk.CTkEntry(self, placeholder_text="Atención a:")
        self.atencion_entry.pack(pady=5)

        self.proyecto_opciones = ctk.CTkOptionMenu(self, values=["RED", "CCTV", "AUDIO", "TELEFONÍA"])
        self.proyecto_opciones.set("RED")
        self.proyecto_opciones.pack(pady=5)

        # Aquí iría la tabla de productos (por ahora solo etiqueta)
        ctk.CTkLabel(self, text="(Aquí irá la tabla de productos)", font=("Arial", 12, "italic")).pack(pady=10)

        # Totales simulados
        ctk.CTkLabel(self, text="Subtotal: $____").pack()
        ctk.CTkLabel(self, text="IVA: $____").pack()
        ctk.CTkLabel(self, text="ISR: $____").pack()
        ctk.CTkLabel(self, text="TOTAL: $____").pack(pady=5)

        # Botones de acción
        ctk.CTkButton(self, text="Vista previa").pack(pady=5)
        ctk.CTkButton(self, text="Generar documento").pack(pady=5)
        ctk.CTkButton(self, text="Imprimir").pack(pady=5)
