from customtkinter import *
from tkinter import filedialog, Menu
from frontend.frames.tabela_scroll import Tabela_Scroll
from frontend.screens.configuracoes import Configuracoes
from frontend.frames.pontuacao import Pontuacao_Provas
from frontend.frames.rank import Rank
from frontend.theme import COLORS

class Principal(CTkFrame):
    def __init__(self, master, app,  **kwargs):
        super().__init__(master, **kwargs)

        self.app = app

        #Inicilização do menu
        self.menu = CTkFrame(
            master = self, 
            fg_color=COLORS["cards"], 
            corner_radius=0
        )
        self.menu.place(relx = 0.5, rely = 0.02, relwidth = 1, relheight = 0.04, anchor = "center")

        self.arquivos = CTkButton(
            master = self.menu, 
            fg_color= "transparent", 
            hover_color= COLORS["hover"], 
            text = "Arquivos", 
            corner_radius= 0
        )
        self.arquivos.pack(side="left")
        self.arquivos.bind("<Button-1>", self.abrir_menu_arquivos)

        self.central_frame= CTkFrame(
            master = self, 
            fg_color=COLORS["bg2"], 
            corner_radius=32
        )
        self.central_frame.place(relx = 0.5, rely= 0.5, anchor= "center", relwidth = 0.96, relheight = 0.85)
        
        #Inicialização da Lista de Provas
        self.lista = Tabela_Scroll(
            master = self.central_frame, 
            fg_color=COLORS["bg"], 
            corner_radius=0, 
            dados = ["Um", "Dois"], 
            tipo_dado= "prova", 
            service= None, 
            funcao= self.selecionar_prova
        )
        self.lista.place(relx = 0.19, rely = 0.5, relwidth = 0.3, relheight = 0.77, anchor = "center")
        
        self.barra_nome_lista = CTkFrame(
            master = self.central_frame, 
            fg_color=COLORS["bg3"], 
            corner_radius=0
        )
        self.barra_nome_lista.place(relx = 0.19, rely = 0.09, relwidth = 0.3, relheight = 0.05, anchor = "center")

        self.nome_lista = CTkLabel(
            master = self.barra_nome_lista, 
            text="Provas"
        )
        self.nome_lista.place(relx = 0.5, rely = 0.5, anchor = "center")

        
        #Inicialização dos pontos das provas
        
        self.pontuacao = Pontuacao_Provas(
            master = self.central_frame, 
            selected= self.app.prova_selecionada, 
            fg_color=COLORS["bg"], 
            corner_radius=0
        )
        self.pontuacao.place(relx = 0.5, rely = 0.5, relwidth = 0.3, relheight = 0.77, anchor = "center")

        self.barra_pontuacao = CTkFrame(
            master = self.central_frame, 
            fg_color=COLORS["bg3"], 
            corner_radius=0
        )
        self.barra_pontuacao.place(relx = 0.5, rely = 0.09, relwidth = 0.3, relheight = 0.05, anchor = "center")

        self.pontuacao_label = CTkLabel(
            master = self.barra_pontuacao, 
            text=f"Prova: Não selecionada"
        )
        self.pontuacao_label.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.barra_gabarito = CTkFrame(
            master = self.central_frame, 
            corner_radius=0
        )
        self.barra_gabarito.place(relx = 0.5, rely = 0.885, relwidth = 0.3, relheight = 0.05, anchor = "center")

        self.aplicar_rank = CTkButton(
            master = self.barra_gabarito, 
            width = 128, fg_color=COLORS["primary"], 
            hover_color=COLORS["hover"], 
            corner_radius=0, 
            text = "Aplicar", 
            command = lambda: self.rank.renderizar()
        )
        self.aplicar_rank.pack(side = "left", fill = "both")

        self.marcar_todos = CTkButton(
            master = self.barra_gabarito, 
            width = 128, fg_color=COLORS["cards"], 
            hover_color=COLORS["hover"], 
            corner_radius=0, 
            text = "Marcar tudo", 
            command = lambda: self.marcacao(1)
        )
        self.marcar_todos.pack(side = "left", fill = "both")

        self.desmarcar_todos = CTkButton(
            master = self.barra_gabarito, 
            width = 128, fg_color=COLORS["cards"], 
            hover_color=COLORS["hover"], 
            corner_radius=0, 
            text = "Desmarcar tudo", 
            command = lambda: self.marcacao(0)
        )
        self.desmarcar_todos.pack(side = "left", fill = "both")

        #Inicialização do Ranking 
        self.rank = Rank(
            master = self.central_frame, 
            fg_color=COLORS["bg"], 
            corner_radius=0
        )
        self.rank.place(relx = 0.81, rely = 0.5, relwidth = 0.3, relheight = 0.77, anchor = "center")

        self.barra_nome_rank = CTkFrame(
            master = self.central_frame, 
            fg_color=COLORS["bg3"], 
            corner_radius=0
        )
        self.barra_nome_rank.place(relx = 0.81, rely = 0.09, relwidth = 0.3, relheight = 0.05, anchor = "center")

        self.nome_rank = CTkLabel(
            master = self.barra_nome_rank, 
            text="Ranking"
        )
        self.nome_rank.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.label_rank = CTkLabel(
            master= self.central_frame, 
            text= ""
        )
        self.label_rank.place(relx= 0.81, rely= 0.93, anchor= "center")
        
        self.credits = CTkLabel(
            master= self.central_frame, 
            text= "Made by kakaeser", 
            fg_color=COLORS["bg2"], 
            text_color= COLORS["text"]
        )
        self.credits.place(relx= 0.09, rely= 0.95, anchor= "center")

    
    def abrir_configs(self):
        if hasattr(self, "toplevel") and self.toplevel.winfo_exists():
            self.toplevel.focus()
            return
        self.toplevel = Configuracoes(master= self, on_update= self.atualizar_telas)
        self.toplevel.title("Configurações")
        self.toplevel.geometry("500x500")
        self.toplevel.lift()
        self.toplevel.attributes("-topmost", True)
        self.toplevel.after(100, lambda: self.toplevel.attributes("-topmost", False))

    def marcacao(self, mark):
        self.question_service.marcar_todos(self.aluno_selecionado["id"], mark)
        self.gabarito.renderizar()
    
    def atualizar_telas(self):
        self.lista.renderizar()
        self.gabarito.renderizar()
        self.rank.renderizar()
    
    def copiar_rank(self):
        texto = ""
        
        for i, r in enumerate(self.rank.ranking, start=1):
            if r["nota"] == "-":
                nota = 0
            else:
                nota = float(r["nota"])
            texto += f"{i}º - {r['nome']} - {nota:.2f}\n"


        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()
        self.label_rank.configure(text = "Rank copiado!!!")

    
    def importar_lista(self):
        caminho = filedialog.askopenfilename(
            title="Selecionar arquivo Excel",
            filetypes=[("Excel", "*.xlsx *.xls")],
            parent=self
        )

        if not caminho:
            print("Problema no caminho")
            return  

    def abrir_menu_arquivos(self, event):
        menu = Menu(self, tearoff=0, bg=COLORS["cards"], fg=COLORS["text"],activebackground=COLORS["hover"])

        menu.add_command(label="Abrir competicao")
        menu.add_separator()
        menu.add_command(label="Adicionar Equipes", command= self.abrir_configs)
        # posição logo abaixo do botão
        x = event.widget.winfo_rootx()
        y = event.widget.winfo_rooty() + event.widget.winfo_height()

        menu.post(x, y)

    def selecionar_prova(self, prova):
        self.prova_selecionada = prova
        self.pontuacao_label.configure(text = "Prova: " + self.prova_selecionada)
        self.pontuacao.renderizar()
