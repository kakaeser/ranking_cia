from customtkinter import *
from frontend.theme import COLORS

class Pontuacao_Provas(CTkScrollableFrame):
    def __init__(self, master,selected, **kwargs):
        super().__init__(master, **kwargs)
        self.selected = selected

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
        equipes_participantes = []
        # Ainda não temos
        if not equipes_participantes:
            CTkLabel(
                self,
                text="Nenhuma equipe foi adicionada"
            ).pack(pady=20)
            return
        else:
            for p in equipes_participantes:
                self.criar_linha(p)
    
    def criar_linha(self, equipe):
        linha = CTkFrame(master = self, fg_color=COLORS["cards"])
        linha.pack(fill="x", padx=2, pady=2)

        nome_equipe = CTkLabel(
            linha,
            text=f"{equipe['nome']}:",
            fg_color="transparent"
        )

        pontos = CTkEntry(
            linha,
            text="",
            fg_color=COLORS["primary2"],
            hover_color=COLORS["primary2"],
            corner_radius= 0
        
        )
        
        nome_equipe.pack(side="left", expand=True, padx=(8, 4))
        pontos.pack(side="right", padx=(4, 8))