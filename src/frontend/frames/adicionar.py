from customtkinter import *
from frontend.theme import COLORS

class Adicionar (CTkToplevel):
    def __init__(self, tipo_dado, funcao):
        super().__init__()
        self.tipo_dado = tipo_dado
        self.funcao = funcao
        self.title("Adicionar " + self.tipo_dado)
        self.geometry("600x180")
        self.resizable(False, False)
        self.configure(fg_color = COLORS["bg"])
        self.attributes('-topmost', True)

        centralizar_janela(self, 600, 180)

        # Configuração do Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Entry
        self.entry = CTkEntry(self, placeholder_text="Adicionar "+ self.tipo_dado)
        self.entry.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # Botões
        self.frame_botoes = CTkFrame(self, fg_color=COLORS["bg"])
        self.frame_botoes.grid(row=2, column=0, padx=20, pady=5, sticky="nsew")
        self.frame_botoes.grid_columnconfigure(0, weight=1)

        self.error_label = CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=1, column=0, padx=10, pady=0)

        self.botao_add = CTkButton(self.frame_botoes, text="Adicionar", command=self.add, fg_color=COLORS["primary"], hover_color=COLORS["hover"])
        self.botao_add.grid(row=0, column=0, padx=10, pady=5)

    def add(self):
        if not self.entry.get():
            self.error_label.configure(text="Voce nao colocou nome da " + self.tipo_dado + "!!!")
            return
        if self.funcao:
            self.funcao(self.entry.get())
        self.destroy()

    

def centralizar_janela(janela, largura=300, altura=200):
    janela.update_idletasks()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = int((largura_tela / 2) - (largura / 2))
    y = int((altura_tela / 2) - (altura / 2))

    janela.geometry(f"{largura}x{altura}+{x}+{y}")
