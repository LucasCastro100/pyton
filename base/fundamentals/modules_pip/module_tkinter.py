import tkinter as tk

# CRIANDO A JANELA
window = tk.Tk()
window.geometry("350x150")
window.title("GERENCIADOR DE FRASES")

# ADICIONANDO O FRAME - POSICIONAR OS ELEMENTOS
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# ADICIONANDO O LABEL
label = tk.Label(frame, text="")
label.pack(fill="x", expand=True)

# ADIOCIONANDO O INPUT TEXT 
frase_lab = tk.Label(frame, text='Frase')
frase_lab.pack(fill="x", expand=True)

# ENTRY - CAMPO INPUT APRA RECEBER DADOS
frase_input = tk.Entry(frame)
frase_input.pack(fill="x", expand=True)

# FUNÇÃO PARA PEGAR OS DADOS DO INPUT
def click():
    label.config(text=frase_input.get())

# ADICIONANDO O BOTÃO E PASSANDO A FUNÇÃO CLICK
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()