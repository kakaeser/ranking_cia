from customtkinter import *
from frontend.frames.tabela_scroll import Tabela_Scroll
from frontend.theme import COLORS

class Inicial(CTkFrame):
    def __init__(self, master,app,  **kwargs):
        super().__init__(master, **kwargs)
        self.app = app

        self.seletor = Tabela_Scroll(
            master = self, 
            fg_color=COLORS["bg"], 
            corner_radius=0, 
            dados=[1], 
            tipo_dado="Competicao", 
            service = None, 
            funcao = self.selecionar
        )
        self.seletor.place(relx = 0.81, rely = 0.5, relwidth = 0.3, relheight = 0.77, anchor = "center")


    def selecionar(self, dado):
        self.app.competicao_selecionada = dado
        self.app.mostrar_tela("principal")