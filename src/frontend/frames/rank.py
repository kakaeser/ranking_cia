from customtkinter import *
from frontend.theme import COLORS

class Rank(CTkScrollableFrame):
    def __init__(self, master, service, selected,**kwargs):
        super().__init__(master, **kwargs)
        self.service = service
        self.selected = selected
        self.ranking = self.service.calcular_rank(self.selected["id"])
        
        self.renderizar()

    def renderizar(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.ranking = self.service.calcular_rank(self.selected["id"])
        if not self.ranking:
            CTkLabel(
                self,
                text="Nenhuma nota foi computada"
            ).pack(pady=20)
            return
        
        i = 0
        for p in self.ranking:
            i +=1
            self.criar_linha(p, i)
    
    def criar_linha(self, rank, num):
        nota_valor = rank.get("nota")
        if nota_valor != "-":
            nota_texto = f"{float(nota_valor):.2f}"
        else:
            nota_texto = nota_valor

        linha = CTkFrame(master = self, fg_color=COLORS["primary"])
        linha.pack(fill="x", padx=2, pady=2)

        posicao = CTkLabel(linha,text=f"#{num}",fg_color="transparent", anchor= "w", width = 20)

        sep1 = CTkFrame(linha, width=4, fg_color="#111111", height=30)

        nome = CTkLabel(linha,text=f"{rank['nome']}",fg_color="transparent", anchor= "w")

        sep2 = CTkFrame(linha, width=4, fg_color="#111111", height=30)

        nota = CTkLabel(linha,text=f"{nota_texto}",fg_color="transparent", anchor= "e", width = 45)
        
        
        posicao.pack(side="left", padx= 5)
        sep1.pack(side="left", padx= 5)
        nome.pack(side="left", padx= 5)
        nota.pack(side="right", padx= 20)
        sep2.pack(side="right", padx= 5)

        nome_equipe = rank['nome'] 

        if nome_equipe == "Sarça Ardente":
            # Laranja
            linha.configure(fg_color="#F05A28")
            sep1.configure(fg_color="#C1451B")
            sep2.configure(fg_color="#C1451B")
            
        elif nome_equipe == "Figueira":
            # Cinza
            linha.configure(fg_color="#8B8D8E")
            sep1.configure(fg_color="#6A6B6D")
            sep2.configure(fg_color="#6A6B6D")
            
        elif nome_equipe == "Carvalho":
            # Preto
            linha.configure(fg_color="#231F20")
            sep1.configure(fg_color="#000000")
            sep2.configure(fg_color="#000000")
            
        elif nome_equipe == "Pinheiro":
            # Azul Claro
            linha.configure(fg_color="#00AEEF")
            sep1.configure(fg_color="#0082B3")
            sep2.configure(fg_color="#0082B3")
            
        elif nome_equipe == "Videira":
            # Rosa/Magenta
            linha.configure(fg_color="#EC008C")
            sep1.configure(fg_color="#B2006A")
            sep2.configure(fg_color="#B2006A")
            
        elif nome_equipe == "Cedro Líbano":
            # Verde Claro
            linha.configure(fg_color="#39B54A")
            sep1.configure(fg_color="#298736")
            sep2.configure(fg_color="#298736")
            
        elif nome_equipe == "Bálsamo":
            # Azul Escuro
            linha.configure(fg_color="#2E3192")
            sep1.configure(fg_color="#1F226B")
            sep2.configure(fg_color="#1F226B")
            
        elif nome_equipe == "Ameixeira":
            # Branco
            linha.configure(fg_color="#FFFFFF")
            sep1.configure(fg_color="#CCCCCC")
            sep2.configure(fg_color="#CCCCCC")
            posicao.configure(text_color="#000000")
            nome.configure(text_color="#000000")
            nota.configure(text_color="#000000")
            
        elif nome_equipe == "Jacarandá":
            # Roxo
            linha.configure(fg_color="#662D91")
            sep1.configure(fg_color="#4D216D")
            sep2.configure(fg_color="#4D216D")
            
        elif nome_equipe == "Tamareira":
            # Verde Escuro
            linha.configure(fg_color="#006838")
            sep1.configure(fg_color="#004223")
            sep2.configure(fg_color="#004223")
            
        elif nome_equipe == "Acácia":
            # Amarelo
            linha.configure(fg_color="#FFF200")
            sep1.configure(fg_color="#CFC400")
            sep2.configure(fg_color="#CFC400")
            posicao.configure(text_color="#000000")
            nome.configure(text_color="#000000")
            nota.configure(text_color="#000000")
            
        elif nome_equipe == "Oliveira":
            # Marrom
            linha.configure(fg_color="#603813")
            sep1.configure(fg_color="#42260D")
            sep2.configure(fg_color="#42260D")
        