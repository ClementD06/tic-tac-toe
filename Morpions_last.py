# Importer tkinter
import tkinter as tk
from tkinter import *


# Créer la fenêtre principale
window = tk.Tk()
window.title("Jeu de morpion TicTacToe")

# Créer le plateau de jeu avec 9 boutons
buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(window, text=" ", font=("Arial", 60), width=4, height=1, fg="white", bg="grey")
        button.grid(row=i, column=j, padx=1, pady=1)
        buttons.append(button)

# Définir les variables globales
turn = "X" # Le tour du joueur
winner = None # Le gagnant du jeu
board = [" "] * 9 # Le tableau représentant le plateau de jeu

# Définir la fonction qui vérifie si le jeu est terminé
def check_game_over():
    global winner
# Vérifier les lignes
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            winner = board[i]
            return True
# Vérifier les colonnes
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            winner = board[i]
            return True
# Vérifier les diagonales
    if board[0] == board[4] == board[8] != " ":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] != " ":
        winner = board[2]
        return True
# Vérifier si le plateau est plein
    if " " not in board:
        winner = "Tie"
        return True
# Sinon, le jeu n'est pas terminé
    return False

# Définir la fonction qui colorie les boutons de la ligne gagnante
def color_win_line():
    global winner
    global board
# Les indices des boutons qui font partie de la ligne gagnante
    win_indices = []
# Vérifier les lignes
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == winner:
            win_indices = [i, i+1, i+2]
            break
    if not win_indices:
        # Vérifier les colonnes
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == winner:
                win_indices = [i, i+3, i+6]
                break
    if not win_indices:
# Vérifier les diagonales
        if board[0] == board[4] == board[8] == winner:
            win_indices = [0, 4, 8]
        elif board[2] == board[4] == board[6] == winner:
            win_indices = [2, 4, 6]

# Colorier les boutons de la ligne gagnante
    for index in win_indices:
        buttons[index].config(bg="green")


# Définir la fonction qui affiche le résultat du jeu
def show_result():
    global winner
# Créer une nouvelle fenêtre
    result_window = tk.Toplevel(window)
    result_window.title("Résultat")
# Afficher le message selon le gagnant
    if winner == "X":
        message = tk.Label(result_window, text="Le joueur X a gagné !", font=("Arial", 20))
    elif winner == "O":
        message = tk.Label(result_window, text="Le joueur O a gagné !", font=("Arial", 20))
    else:
        message = tk.Label(result_window, text="Match nul !", font=("Arial", 20))
    message.pack()
# Créer un bouton pour quitter le jeu
    quit_button = tk.Button(result_window, text="Quitter", font=("Arial", 20), fg="black", command=window.destroy)
    quit_button.pack()
# Colorier la ligne gagnante
    if winner != "Tie":
        color_win_line()
   

# Définir la fonction qui gère le clic sur un bouton du plateau
def click(button):
    global turn
    global board
# Récupérer l'index du bouton dans la liste des boutons
    index = buttons.index(button)
# Vérifier si le bouton est vide et si le jeu n'est pas terminé
    if board[index] == " " and not check_game_over():
# Mettre à jour le texte du bouton avec le symbole du joueur actuel
        button.config(text=turn)
# Mettre à jour le tableau avec le symbole du joueur actuel
        board[index] = turn
# Changer de tour
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
# Mettre à jour le label avec le joueur actuel
        update_player_label()
# Vérifier si le jeu est terminé
        if check_game_over():
# Afficher le résultat du jeu
            show_result()

# Associer la fonction click à chaque bouton du plateau
for button in buttons:
    button.config(command=lambda b=button: click(b))

# Définir la fonction qui réinitialise la grille et recommence une nouvelle partie
def restart():
    global turn
    global winner
    global board
# Réinitialiser les variables globales
    turn = "X"
    winner = None
    board = [" "] * 9
# Réinitialiser les textes des boutons
    for button in buttons:
        button.config(text=" ")

# Définir la fonction qui met à jour le label avec le joueur actuel
def update_player_label():
    global turn
    # Mettre à jour le label avec le joueur actuel
    player_label.config(text="C'est au tour de " + turn)
# Créer le label qui affiche le joueur actuel
player_label = tk.Label(window, text="C'est au tour de X", font=("Arial",15))
player_label.grid(row=3, column=1)


# Créer le bouton "Rejouer"
restart_button = tk.Button(window, text="Réinitialiser", font=("Arial", 20), command=restart)
restart_button.grid(row=3, column=0)

# Créer un bouton pour quitter le jeu
quit_button = tk.Button(window, text="Quitter", font=("Arial", 20), fg="black", command=window.destroy)
quit_button.grid(row=3, column=2)

# Lancer la boucle principale de tkinter
window.mainloop()
