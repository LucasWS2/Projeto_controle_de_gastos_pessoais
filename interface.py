import tkinter as tk
from tkinter import ttk
from gastos import adicionar_gasto, listar_gastos, total_gastos
from database import create_table

create_table()

def atualizar_lista():
    for item in tree.get_children():
        tree.delete(item)
    for gasto in listar_gastos():
        tree.insert('', tk.END, values=gasto)
    total_label.config(text=f"Total: R$ {total_gastos():.2f}")

def adicionar():
    desc = entrada_descricao.get()
    valor = entrada_valor.get()
    categoria = entrada_categoria.get()
    if desc and valor:
        try:
            adicionar_gasto(desc, float(valor), categoria)
            entrada_descricao.delete(0, tk.END)
            entrada_valor.delete(0, tk.END)
            entrada_categoria.delete(0, tk.END)
            atualizar_lista()
        except ValueError:
            print("Valor inválido.")

# Janela principal
janela = tk.Tk()
janela.title("💸 Controle de Gastos")
janela.geometry("600x400")
janela.resizable(False, False)

# Entradas
tk.Label(janela, text="Descrição").grid(row=0, column=0, padx=5, pady=5)
entrada_descricao = tk.Entry(janela, width=30)
entrada_descricao.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Valor (R$)").grid(row=1, column=0, padx=5, pady=5)
entrada_valor = tk.Entry(janela)
entrada_valor.grid(row=1, column=1, padx=5, pady=5)

tk.Label(janela, text="Categoria").grid(row=2, column=0, padx=5, pady=5)
entrada_categoria = tk.Entry(janela)
entrada_categoria.grid(row=2, column=1, padx=5, pady=5)

tk.Button(janela, text="Adicionar Gasto", command=adicionar).grid(row=3, column=0, columnspan=2, pady=10)

# Tabela de gastos
colunas = ("ID", "Descrição", "Valor", "Categoria", "Data")
tree = ttk.Treeview(janela, columns=colunas, show="headings")
for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Total
total_label = tk.Label(janela, text="Total: R$ 0.00", font=("Arial", 12, "bold"))
total_label.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar
atualizar_lista()
janela.mainloop()
