import tkinter as tk

def on_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

def clear_entry():
    entry.delete(0, tk.END)

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Hatim's first Calculator")

# Zone de saisie
entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Boutons de la calculatrice
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == 'C':
        btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), command=clear_entry)
    else:
        btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 14))
        btn.bind('<Button-1>', on_click)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Lancer la boucle principale
root.mainloop()
