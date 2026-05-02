from customtkinter import *
from frontend.theme import COLORS
from frontend.frames.confirmacao import Confirmacao
from PIL import Image

class Tabela_Scroll(CTkScrollableFrame):
    def __init__(self, dados, tipo_dado, service, funcao ,master, **kwargs):
        super().__init__(master, **kwargs)
        self.dados = dados
        self.tipo_dado = tipo_dado
        self.service = service
        self.funcao = funcao

        delete = Image.open("src/frontend/assets/delete.png")
        self.delete = CTkImage(light_image=delete, dark_image=delete,size=(24, 24))

        add = Image.open("src/frontend/assets/add.png")
        self.add = CTkImage(light_image=add, dark_image=add,size=(24, 24))
        
        self.renderizar()
    
    def renderizar(self):
        for widget in self.winfo_children():
            widget.destroy()
        # Ainda não temos nada
        if self.dados:
            for p in self.dados:
                self.criar_linha(p)

        adicionar = CTkFrame(master = self, fg_color=COLORS["cards"])
        adicionar.pack(fill="x", padx=2, pady=2)

        btn_adicionar = CTkButton(master= adicionar,image= self.add, text="Adicionar " + self.tipo_dado,fg_color=COLORS["cards"],hover_color=COLORS["hover"],corner_radius= 4 ,anchor="center")
        btn_adicionar.pack(side="left", fill="x", expand=True, padx=(8, 4))
    
    def criar_linha(self, dado):
        linha = CTkFrame(master = self, fg_color=COLORS["cards"])
        linha.pack(fill="x", padx=2, pady=2)
        botao_nome = CTkButton(
            linha,
            text=dado,
            fg_color=COLORS["cards"],
            hover_color=COLORS["hover"],
            corner_radius= 4 ,
            anchor="w", 
            command= lambda: self.funcao(dado)
        )
        botao_delete = CTkButton(linha, 
            text="", 
            image=self.delete,
            width = 10,
            fg_color=COLORS["cards"], 
            hover_color=COLORS["hover"], 
            corner_radius= 4 ,
            anchor="w", 
            command= self.abrir_confirmacao
        )
        botao_nome.pack(side="left", fill="x", expand=True, padx=(8, 12))
        botao_delete.pack(side="right", padx=(0, 0))
        
    def abrir_confirmacao(self):
        if hasattr(self, "toplevel") and self.toplevel.winfo_exists():
            self.toplevel.focus()
            return
        self.toplevel = Confirmacao(mensagem= "Voce realmente quer apagar essa " + self.tipo_dado + "???", funcao= None)