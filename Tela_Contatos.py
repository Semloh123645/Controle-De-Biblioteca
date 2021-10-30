from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image


def Contato(janela):

    janela.title('Tela de contatos')

    fontExample = tkFont.Font(family="Arial", size=11, weight="bold", slant="italic")

    imagem = ImageTk.PhotoImage(Image.open("logo comunicação.png"))
    imagemL = Label(janela, image=imagem, width=500, height=500)
    imagemL.place(x=0, y=0)
    # lb_contatos = Label(janela, width=15, font=fontExample, fg='black'
    # , text='Em Caso de Dúvida, Entrar em contato com os Desenvolvedores')

    # lb_contato1()

    # lb_contatos.place(x=100, y=250)

    janela.geometry('500x500+450+150')
    janela.mainloop()

