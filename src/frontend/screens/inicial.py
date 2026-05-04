from customtkinter import *
from frontend.frames.tabela_scroll import Tabela_Scroll
from frontend.theme import COLORS
from PIL import Image


class Inicial(CTkFrame):
    def __init__(self, master,app,  **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        
        # Background
        background = Image.open("src/frontend/assets/background.png")
        self.background = CTkImage(light_image=background, dark_image=background, size=(1280, 720))

        self.bg_label = CTkLabel(self, text="", image= self.background)
        self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Resto
        self.frame1 = CTkFrame(
            self, 
            fg_color=COLORS["bg2"],
            bg_color="transparent",
            corner_radius= 0
        )
        self.frame1.place(relx = 0.7, rely = 0.5, relwidth = 0.32, relheight = 0.79, anchor = "center")

        self.label1 = CTkLabel(
            master= self.frame1, 
            text="Seja muito bem-vindo!",  
            font= ("Montserrat", 20)
        )
        self.label1.place(relx = 0.5, rely = 0.025, anchor = "center")

        self.frame2 = CTkFrame(
            self.frame1,
            fg_color=COLORS["bg3"],
            corner_radius= 0
        )
        self.frame2.place(relx = 0.5, rely = 0.1, relwidth = 0.9, relheight = 0.05, anchor = "center")

        self.label2 = CTkLabel(
            master= self.frame2, 
            text="Escolha sua competicao:",  
            font= ("Montserrat", 16)
        )
        self.label2.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.seletor = Tabela_Scroll(
            master = self.frame1, 
            fg_color=COLORS["bg"], 
            corner_radius=0, 
            dados=[1], 
            tipo_dado="Competicao", 
            service = None, 
            funcao = self.selecionar
        )
        self.seletor.place(relx = 0.5, rely = 0.55, relwidth = 0.9, relheight = 0.85, anchor = "center")


    def selecionar(self, dado):
        self.app.competicao_selecionada = dado
        self.app.mostrar_tela("principal")