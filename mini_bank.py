import tkinter as tk
from tkinter import messagebox

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            return None
        else:
            return "Fonds insuffisants"

    def afficher_solde(self):
        return f"Solde de {self.titulaire}: {self.solde} euros"

# Création de l'interface graphique
def mettre_a_jour_solde():
    label_solde.config(text=compte.afficher_solde())

def deposer_argent():
    try:
        montant = float(entry_montant.get())
        compte.deposer(montant)
        mettre_a_jour_solde()
        entry_montant.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")

def retirer_argent():
    try:
        montant = float(entry_montant.get())
        message = compte.retirer(montant)
        if message:
            messagebox.showerror("Erreur", message)
        mettre_a_jour_solde()
        entry_montant.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un montant valide.")

# Instance du compte bancaire
compte = CompteBancaire("MR TOUFFAHI HATIM ", 1000)

# Interface principale
root = tk.Tk()
root.title("Gestion de Compte Bancaire")
root.geometry("700x300")  # Taille de la fenêtre

# Solde actuel
label_solde = tk.Label(root, text=compte.afficher_solde(), font=("Helvetica", 20, "bold"))
label_solde.pack(pady=20)

# Entrée pour le montant
entry_montant = tk.Entry(root, font=("Helvetica", 18), width=10)
entry_montant.pack(pady=10)

# Bouton pour déposer de l'argent
btn_deposer = tk.Button(
    root, text="Déposer", command=deposer_argent, font=("Helvetica", 16), bg="green", fg="white", width=12
)
btn_deposer.pack(pady=10)

# Bouton pour retirer de l'argent
btn_retirer = tk.Button(
    root, text="Retirer", command=retirer_argent, font=("Helvetica", 16), bg="red", fg="white", width=12
)
btn_retirer.pack(pady=10)

# Lancement de l'interface
root.mainloop()
