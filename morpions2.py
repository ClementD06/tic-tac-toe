import subprocess
from tkinter import *
import tkinter   
import webbrowser


def open_log_close_previous():
    window.destroy()
    subprocess.run(["python", "morpions_last.py"])
    

#Creer une premiere fenetre

window = Tk()

#paramètres de la fenetre

window.title("Jeu du morpion")
window.geometry("1280x720")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#41B77F')

#creer la frame

frame = Frame(window, bg='#41B77F')

#Ajouter un premier texte

label_title = Label(frame, text = "Tic Tac Toe", font = ("Arial", 40),bg = '#41B77F', fg = 'White')
label_title.pack()

#Ajouter un second texte

label_subtitle = Label(frame, text = "Bienvenue sur le jeu du Morpion ", font = ("Arial", 25),bg = '#41B77F', fg = 'White')
label_subtitle.pack()

frame.pack(expand=YES)

#Ajouter un bouton

yt_button = Button(frame, text= "Lancer une partie", font = ("Arial", 25),bg = 'white', fg = '#41B77F', command=open_log_close_previous)
yt_button.pack(pady=25, fill=X)


#Afficher la fenetre

window.mainloop()
