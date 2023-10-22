import secrets
import string
import tkinter as tk
from tkinter import ttk, messagebox


CARACTER_ESPECIAIS = '!@#$%_)(*&|{}[]'
def gerar_senha():
    comprimento = comprimento_var.get()

    caracteres = string.ascii_letters
    if incluir_numeros_var.get():
        caracteres += string.digits + string.digits + string.digits
    if incluir_especiais_var.get():
        caracteres += CARACTER_ESPECIAIS + CARACTER_ESPECIAIS + CARACTER_ESPECIAIS

    try:
        senha_gerada = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
        resultado_var.set(senha_gerada)
    except ValueError:
        messagebox.showwarning("Atenção", "Por favor, selecione opções válidas.")

def copiar_senha():
    senha = resultado_var.get()
    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        janela.update()  # Atualizar a área de transferência
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência.")
    else:
        messagebox.showwarning("Atenção", "Nenhuma senha gerada ainda.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Definir tamanho fixo da janela
largura_janela = 400
altura_janela = 300
janela.geometry(f"{largura_janela}x{altura_janela}")

# Impedir redimensionamento da janela
janela.resizable(False, False)

# Criar e posicionar widgets
frame_opcoes = ttk.LabelFrame(janela, text="OPCOES")
frame_opcoes.pack(padx=10, pady=10, fill="x")

comprimento_label = ttk.Label(frame_opcoes, text="Comprimento:")
comprimento_label.grid(row=0, column=0, padx=5, pady=5)

comprimento_var = tk.IntVar()
comprimento_entry = ttk.Entry(frame_opcoes, textvariable=comprimento_var, width=5)
comprimento_entry.grid(row=0, column=1, padx=5, pady=5)
comprimento_var.set(12)

incluir_numeros_var = tk.BooleanVar()
incluir_numeros_check = ttk.Checkbutton(frame_opcoes, text="Incluir Números", variable=incluir_numeros_var)
incluir_numeros_check.grid(row=1, column=0, columnspan=2, pady=5, sticky="W")
incluir_numeros_var.set(True)

incluir_especiais_var = tk.BooleanVar()
incluir_especiais_check = ttk.Checkbutton(frame_opcoes, text="Incluir Caracteres Especiais", variable=incluir_especiais_var)
incluir_especiais_check.grid(row=2, column=0, columnspan=2, pady=5, sticky="W")
incluir_especiais_var.set(True)

botao_gerar = ttk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar.pack(pady=10)

resultado_var = tk.StringVar()
resultado_entry = ttk.Entry(janela, textvariable=resultado_var, state="readonly")
resultado_entry.pack(padx=10, pady=10, fill="x")
resultado_entry.bind("<Button-1>", lambda e: resultado_entry.focus_set())  # Para permitir a seleção do texto

# Adicionar botão "Copiar Senha"
botao_copiar = ttk.Button(janela, text="Copiar Senha", command=copiar_senha)
botao_copiar.pack(pady=5)

# Iniciar o loop da interface gráfica
janela.mainloop()
