from customtkinter import *
from frontend.theme import COLORS

class Confirmacao (CTkToplevel):
    def __init__(self, mensagem, funcao):
        super().__init__()
        self.mensagem = mensagem
        self.funcao = funcao
        self.title("Confirmação")
        self.geometry("600x150")
        self.resizable(False, False)
        self.configure(fg_color = COLORS["bg"])
        self.attributes('-topmost', True)

        centralizar_janela(self, 600, 150)

        # Configuração do Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Mensagem
        self.label_mensagem = CTkLabel(self, text=self.mensagem)
        self.label_mensagem.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # Botões
        self.frame_botoes = CTkFrame(self, fg_color=COLORS["bg"])
        self.frame_botoes.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.frame_botoes.grid_columnconfigure(0, weight=1)
        self.frame_botoes.grid_columnconfigure(1, weight=1)

        self.botao_sim = CTkButton(self.frame_botoes, text="Sim", command=self.sim, fg_color=COLORS["primary"], hover_color=COLORS["hover"])
        self.botao_sim.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.botao_nao = CTkButton(self.frame_botoes, text="Não", command=self.nao, fg_color=COLORS["primary"], hover_color=COLORS["hover"])
        self.botao_nao.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def sim(self):
        self.destroy()
        if self.funcao:
            self.funcao()

    def nao(self):
        self.destroy()

def centralizar_janela(janela, largura=300, altura=200):
    janela.update_idletasks()

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = int((largura_tela / 2) - (largura / 2))
    y = int((altura_tela / 2) - (altura / 2))

    janela.geometry(f"{largura}x{altura}+{x}+{y}")
