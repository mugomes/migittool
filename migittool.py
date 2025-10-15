# Copyright (C) 2025 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Site: https://www.mugomes.com.br

import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.constants import *
import subprocess
import os

def run_command(cmd, cwd=None):
    text.insert(tk.END, f"$ {cmd}\n")
    text.see(tk.END)
    text.update()

    process = subprocess.Popen(cmd, shell=True, cwd=cwd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    output, error = process.communicate()

    if output:
        text.insert(tk.END, output + "\n")
    if error:
        text.insert(tk.END, error + "\n")

    text.see(tk.END)

def executar_git():
    username = entry.get().strip()
    repo = entry2.get().strip()
    if not username:
        messagebox.showwarning("Aviso", "Informe o nome do usuário!")
        return
        
    if not repo:
        messagebox.showwarning("Aviso", "Informe o nome do repositório!")
        return

    # Define pasta alvo
    target_dir = os.getcwd()
    if var_pasta.get():
        target_dir = os.path.join(target_dir, repo, repo)
        os.makedirs(target_dir, exist_ok=True)

    # Executar Comando
    run_command(f"git clone https://github.com/{username}/{repo}.git .", cwd=target_dir)
    run_command("git branch -m main", cwd=target_dir)
    run_command(f"git remote set-url origin git@github.com:{username}/{repo}.git", cwd=target_dir)

# ---- GUI ----
root = tk.Tk()
root.title("MiGitTool")

style = ttk.Style()
style.configure("MeuBotao.TButton", font=("", 12, "bold"))
style.configure("MeuCheckButton.TCheckbutton", font=("", 12))

text = ttk.Text(root)
text.pack(fill="both", expand=True)

label = ttk.Label(root, text="Digite o nome do usuário", font=("", 12, "bold"))
label.pack(anchor="nw", padx=5)

entry = ttk.Entry(root, bootstyle="info", font=("",12))
entry.pack(fill="x", padx=5)

label2 = ttk.Label(root, text="Digite o nome do repositório", font=("", 12, "bold"))
label2.pack(anchor="nw", padx=5)

entry2 = ttk.Entry(root, bootstyle="info", font=("",12))
entry2.pack(fill="x", padx=5)

var_pasta = tk.BooleanVar()
chk = ttk.Checkbutton(root, text="Criar Pasta", variable=var_pasta, style="MeuCheckButton.TCheckbutton", bootstyle="default-round-toggle")
chk.pack(anchor="nw", padx=5, pady=5)

btn = ttk.Button(root, text="Executar Git", style="MeuBotao.TButton", command=executar_git)
btn.pack(pady=5)
btn.pack()

root.mainloop()
