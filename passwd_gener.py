import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """Génère un mot de passe en fonction des options sélectionnées."""
    length = int(length_var.get())
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    # Ensemble de caractères
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Erreur", "Veuillez sélectionner au moins un type de caractères.")
        return
    
    # Génération du mot de passe
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_result.delete(0, tk.END)
    entry_result.insert(0, password)

def copy_to_clipboard():
    """Copie le mot de passe généré dans le presse-papiers."""
    password = entry_result.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Succès", "Mot de passe copié dans le presse-papiers !")
    else:
        messagebox.showwarning("Erreur", "Aucun mot de passe à copier.")

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Hatim's Generator")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Longueur du mot de passe :", font=("Arial", 12)).pack(pady=5)
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var, width=5, font=("Arial", 12)).pack()

uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Inclure des majuscules", variable=uppercase_var).pack(anchor="w", padx=10)
tk.Checkbutton(root, text="Inclure des chiffres", variable=numbers_var).pack(anchor="w", padx=10)
tk.Checkbutton(root, text="Inclure des symboles", variable=symbols_var).pack(anchor="w", padx=10)

tk.Button(root, text="Générer", command=generate_password, font=("Arial", 12), bg="lightblue").pack(pady=10)

entry_result = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
entry_result.pack(pady=5)

tk.Button(root, text="Copier", command=copy_to_clipboard, font=("Arial", 12), bg="lightgreen").pack(pady=5)

# Boucle principale
root.mainloop()
