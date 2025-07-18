#Este archivo me permitirá crear y almancenar componentes de la GUI
import customtkinter as ctk

class BotonPrincipal(ctk.CTkButton):
    def __init__(self, master, texto, comando=None):
        super().__init__(
            master,
            text=texto,
            command=comando,
            fg_color="#23aa28",
            hover_color="#1c45cb",
            text_color="white",
            font=("Arial", 14),
            corner_radius=12,
            width=200,
            height=40
        )

class CampoTexto(ctk.CTkEntry):
    def __init__(self, master, placeholder=""):
        super().__init__(master, placeholder_text=placeholder, width=300, height=32)