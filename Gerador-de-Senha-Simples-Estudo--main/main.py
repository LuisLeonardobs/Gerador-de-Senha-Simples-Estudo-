import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def gerar_senha():
    comprimento = int(entry_tamanho.get())
    usar_letras = var_letras.get()
    usar_numeros = var_numeros.get()
    usar_simbolos = var_simbolos.get()

    if not (usar_letras or usar_numeros or usar_simbolos):
        messagebox.showwarning("Aviso", "Selecione pelo menos um tipo de caractere!")
        return

    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, senha)

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        pyperclip.copy(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

# Interface
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("350x300")
janela.resizable(False, False)

tk.Label(janela, text="Tamanho da senha:").pack(pady=5)
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

var_letras = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

tk.Checkbutton(janela, text="Letras", variable=var_letras).pack()
tk.Checkbutton(janela, text="Números", variable=var_numeros).pack()
tk.Checkbutton(janela, text="Símbolos", variable=var_simbolos).pack()

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

entry_senha = tk.Entry(janela, font=("Arial", 14), justify="center")
entry_senha.pack(pady=5)

tk.Button(janela, text="Copiar", command=copiar_senha).pack()

janela.mainloop()
