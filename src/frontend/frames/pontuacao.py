from customtkinter import *
from frontend.theme import COLORS

class Pontuacao_Provas(CTkScrollableFrame):
    def __init__(self, master,selected, service, **kwargs):
        super().__init__(master, **kwargs)
        self.selected = selected
        self.service = service
        self.pontuacao_equipes = None
        self.variaveis_pontos = {}

        self.renderizar()

    def renderizar(self):
        for widget in self.winfo_children():
            widget.destroy()

        if not self.selected:
            CTkLabel(
                self,
                text="Nenhuma prova foi selecionada"
            ).pack(pady=20)
            return

        self.pontuacao_equipes = self.service.listar_por_prova(self.selected["id"])

        if not self.pontuacao_equipes:
            CTkLabel(
                self,
                text="Nenhuma equipe foi adicionada"
            ).pack(pady=20)
            return
        else:
            for p in self.pontuacao_equipes:
                self.criar_linha(p)
    
    def criar_linha(self, equipe):
        linha = CTkFrame(master = self, fg_color=COLORS["cards"])
        linha.pack(fill="x", padx=2, pady=2)

        nome_equipe = CTkLabel(
            linha,
            text=f"{equipe["nome"]}:",
            fg_color="transparent"
        )

        var_pontos = StringVar(value=str(equipe["pontos"]))
        self.variaveis_pontos[equipe["id"]] = var_pontos

        pontos = CTkEntry(
            linha,
            placeholder_text="",
            textvariable= var_pontos,
            fg_color=COLORS["bg2"],
            corner_radius= 0
        
        )
        
        nome_equipe.pack(side="left", expand=True, padx=(8, 4))
        pontos.pack(side="right", padx=(4, 8))

    def atualizar_pontos(self):
        for e_id, var_pontos in self.variaveis_pontos.items():
            ponto_digitado = var_pontos.get()
            try:
                ponto_numerico = int(ponto_digitado)
            except ValueError:
                ponto_numerico = 0
            self.service.atualizar_pontos(e_id=e_id, p_id= self.selected["id"], pontos= ponto_numerico)
    
    def zerar(self):
        for e_id, var_pontos in self.variaveis_pontos.items():
            self.service.atualizar_pontos(e_id=e_id, p_id= self.selected["id"], pontos= 0)
        