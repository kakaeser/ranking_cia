from customtkinter import *
from frontend.theme import COLORS
from frontend.frames.tabela_scroll import Tabela_Scroll
from tkinter import filedialog

class Configuracoes(CTkToplevel):
    def __init__(self,app, master,on_update, **kwargs):
        super().__init__(master, **kwargs)
        self.on_update = on_update
        self.app = app

        self.frame = CTkFrame(
            master= self, 
            fg_color=COLORS["bg2"]
        )
        self.frame.pack(fill="both")

        self.label = CTkLabel(
            master= self.frame, 
            text = "Gerenciador de equipes", 
            text_color=COLORS["text"], 
            font= ("Montserrat", 20)
        )
        self.label.pack(pady = 8, padx= 16, anchor ="center")

        self.participantes = Tabela_Scroll(
            fg_color=COLORS["bg"], 
            corner_radius=0, 
            dados= [], 
            tipo_dado="Equipes",
            service = None, 
            funcao = None, 
            app= self.app,
            master= self.frame, 
            width= 250, 
            height = 350
        )
        self.participantes.pack(pady = 8, padx= 16, anchor ="center")

        self.import_fake = CTkButton(
            master = self.frame, corner_radius= 0, 
            text = "Importar Clãs Padrão", 
            fg_color=COLORS["primary"],
            hover_color=COLORS["hover"], 
            command = None
        )
        self.import_fake.pack(pady = 8, padx= 16, anchor ="center")

        self.import_real = CTkButton(
            master = self.frame, 
            corner_radius= 0, 
            text = "Importar Times de cores padrão", 
            fg_color=COLORS["primary"],
            hover_color=COLORS["hover"], 
            command = None
        )
        self.import_real.pack(pady = 8, padx= 16, anchor ="center")

    