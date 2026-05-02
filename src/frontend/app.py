from customtkinter import *
from tkinter import filedialog, Menu
from frontend.screens.principal import Principal
from frontend.screens.inicial import Inicial
from frontend.theme import COLORS

set_appearance_mode("Dark")

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Ranking CIA12")
        self.config(bg=COLORS["bg"])
        self.prova_selecionada = None
        self.competicao_selecionada = None
        
        
        self.container = CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.mostrar_tela("principal")

    def mostrar_tela(self, tela):
        for widget in self.container.winfo_children():
            widget.destroy()
        if tela == "inicial":
            self.tela_atual = Inicial(app=self, master= self.container)
        if tela == "principal":
            self.tela_atual = Principal(app=self, master= self.container)

        self.tela_atual.pack(fill="both", expand=True)