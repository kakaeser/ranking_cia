from customtkinter import *
from frontend.theme import COLORS

class Lista(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        self.renderizar()

    def renderizar(self):
        for widget in self.winfo_children():
            widget.destroy()
            
        participantes = []
        # Ainda não temos nada
        if not participantes:
            CTkLabel(
                self,
                text="Nenhuma prova cadastrada"
            ).pack(pady=20)
            return
        else:
            for p in participantes:
                self.criar_linha(p)
    
    def criar_linha(self, participante):
        linha = CTkFrame(master = self, fg_color=COLORS["cards"])
        linha.pack(fill="x", padx=2, pady=2)

        var = IntVar(value= int(participante["presente"]))
        checkbox = CTkCheckBox(
            linha,
            text="",
            variable=var,
            width = 20,
            fg_color=COLORS["primary2"],
            hover_color=COLORS["primary2"],
            corner_radius= 4,
            command=lambda pid=participante["id"], v=var:
                self.service.marcar_presenca(pid, v.get())
        )
        
        botao_nome = CTkButton(
            linha,
            text=participante["nome"],
            fg_color=COLORS["cards"],
            hover_color=COLORS["hover"],
            corner_radius= 4 ,
            anchor="w",
            command=lambda:
                self.on_select_participante(
                    participante["id"],
                    participante["nome"]
                )
        )
        botao_nome.pack(side="left", fill="x", expand=True, padx=(8, 4))
        checkbox.pack(side="right", padx=(4, 8))
