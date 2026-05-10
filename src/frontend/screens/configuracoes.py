from customtkinter import *
from backend.services.equipes_service import Equipes_Service
from frontend.theme import COLORS
from frontend.assets.default import CLANS, TCORES
from frontend.frames.tabela_scroll import Tabela_Scroll
from frontend.frames.confirmacao import Confirmacao
from tkinter import filedialog

class Configuracoes(CTkToplevel):
    def __init__(self,app, master,on_update, **kwargs):
        super().__init__(master, **kwargs)
        self.on_update = on_update
        self.service = Equipes_Service()
        self.app = app
        self.c_id = self.app.competicao_selecionada["id"]
        self.equipe_dados = self.service.listar(self.c_id)

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
            dados= self.equipe_dados, 
            tipo_dado="Equipes",
            service = self.service, 
            funcao = None, 
            app= self.app,
            master= self.frame, 
            width= 250, 
            height = 350
        )
        self.participantes.pack(pady = 8, padx= 16, anchor ="center")

        self.import_clans = CTkButton(
            master = self.frame, corner_radius= 0, 
            text = "Importar Clãs Padrão", 
            fg_color=COLORS["primary"],
            hover_color=COLORS["hover"], 
            command = lambda: self.botao_command(CLANS)
        )
        self.import_clans.pack(pady = 8, padx= 16, anchor ="center")

        self.import_cores = CTkButton(
            master = self.frame, 
            corner_radius= 0, 
            text = "Importar Times de cores padrão", 
            fg_color=COLORS["primary"],
            hover_color=COLORS["hover"], 
            command = lambda: self.botao_command(TCORES)
        )
        self.import_cores.pack(pady = 8, padx= 16, anchor ="center")

    def botao_command(self, lista):
        confirmacao = Confirmacao("Voce realmente quer importar essas equipes?", lambda:self.render(lista))

    def render(self, lista):
        self.service.criar_lista(lista, self.c_id)
        self.participantes.dados = self.service.listar(self.c_id)
        self.participantes.renderizar()

    