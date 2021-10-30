from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from ttkbootstrap import Style
from functools import partial
import mysql.connector
from datetime import timedelta, date
import Tela_Contatos as tc


banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='My_Firstone')

cursor = banco.cursor()
class Tela:
    def __init__(self):

        self.janela = Tk()
        FuncoesBiblioteca.CriarTema(self, 'superhero')
        self.janela.title('Sistema Bibliotecário')
        self.janela.geometry('500x500+450+150')
        self.janela.iconbitmap('2.ico')

        self.frame0 = Frame(self.janela, width=500, height=500)

        Tela.CriarMenu(self, self.frame0)
        imagem = ImageTk.PhotoImage(Image.open("1.png"))
        imagemL = Label(self.frame0, image=imagem, width=500, height=500)
        imagemL.place(x=0, y=0)

        self.frame0.place(x=0, y=0)
        self.janela.mainloop()

    def TelaCadastro(self, janela, menu=''):
        self.janela.config(menu=menu)
        self.janela.title('Cadastro')

        FuncoesBiblioteca.CriarTema(self, 'superhero')
        fontExample = tkFont.Font(family="Arial", size=11, weight="bold", slant="italic")

        self.frame1 = Frame(janela, width=500, height=500)
        lb_nome = Label(self.frame1, text='NOME: ', font=fontExample)
        ce_nome = Entry(self.frame1, width=38)
        lb_senha = Label(self.frame1, text='SENHA: ', font=fontExample)
        ce_senha = Entry(self.frame1, width=38)
        lb_Confirmarsenha = Label(self.frame1, text='CONFIRME: ', font=fontExample)
        ce_Confirmarsenha = Entry(self.frame1, width=38)
        bt0 = Button(self.frame1, width=10, text='VOLTAR', font=fontExample)
        bt1 = Button(self.frame1, width=12, text='CADASTRAR', font=fontExample)

        bt1['command'] = partial(FuncoesBiblioteca.Cadastrar, self, ce_senha, ce_Confirmarsenha, ce_nome)
        bt0['command'] = partial(Tela.SairCadastro, self, ce_Confirmarsenha, ce_nome, ce_senha, self.frame1,
                                 'Sistema Bibliotecário')

        self.frame1.place(x=0, y=0)
        lb_nome.place(x=80, y=150)
        ce_nome.place(x=145, y=152)
        lb_senha.place(x=73, y=200)
        ce_senha.place(x=145, y=202)
        lb_Confirmarsenha.place(x=50, y=250)
        ce_Confirmarsenha.place(x=145, y=252)
        bt0.place(x=160, y=300)
        bt1.place(x=260, y=300)

    def Login(self, janela, menu=''):
        self.janela.config(menu=menu)
        self.janela.title('Login')
        FuncoesBiblioteca.CriarTema(self, 'superhero')
        fontExample = tkFont.Font(family="Arial", size=11, weight="bold", slant="italic")
        self.frame2 = Frame(janela, width=500, height=500)

        lb_nome = Label(self.frame2, text='NOME: ', font=fontExample)
        self.ce_nome = Entry(self.frame2, width=38)
        lb_senha = Label(self.frame2, text='SENHA: ', font=fontExample)
        ce_senha = Entry(self.frame2, width=38)
        lb_esqueci = Label(self.frame2, text='ESQUECI MINHA SENHA', font=fontExample)
        bt3 = Button(self.frame2, text='Não tem cadastro? Clique aqui', font=fontExample, bg='green')
        bt0 = Button(self.frame2, width=10, text='VOLTAR', font=fontExample)
        bt1 = Button(self.frame2, width=10, text='ENTRAR', font=fontExample)
        bt2 = Button(self.frame2, width=19, text='ALTERAR SENHA', font=fontExample)

        bt1['command'] = partial(FuncoesBiblioteca.Validar, self, self.ce_nome, ce_senha, self.janela)
        bt0['command'] = partial(Tela.VoltarMenu, self, self.frame2, 'Sistema Bibliotecário')
        bt2['command'] = partial(Tela.TelaAlterSenha, self)
        bt3['command'] = partial(Tela.TelaCadastro, self, self.janela)

        self.frame2.place(x=0, y=0)
        lb_nome.place(x=80, y=150)
        self.ce_nome.place(x=145, y=152)
        lb_senha.place(x=73, y=200)
        ce_senha.place(x=145, y=202)
        lb_esqueci.place(x=170, y=300)
        bt0.place(x=160, y=245)
        bt2.place(x=170, y=330)
        bt1.place(x=260, y=245)
        bt3.place(x=142, y=390)

    def TelaAlterSenha(self, menu=''):
        self.janela.config(menu=menu)
        self.janela.title('Alterar Senha')

        FuncoesBiblioteca.CriarTema(self, 'superhero')
        fontExample = tkFont.Font(family="Arial", size=11, weight="bold", slant="italic")

        self.frame11 = Frame(self.janela, width=500, height=500)
        lb_nome = Label(self.frame11, text='NOME: ', font=fontExample)
        ce_nome = Entry(self.frame11, width=38)
        lb_senha = Label(self.frame11, text='SENHA: ', font=fontExample)
        ce_senha = Entry(self.frame11, width=38)
        lb_Confirmarsenha = Label(self.frame11, text='CONFIRME: ', font=fontExample)
        ce_Confirmarsenha = Entry(self.frame11, width=38)
        bt0 = Button(self.frame11, width=10, text='VOLTAR', font=fontExample)
        bt1 = Button(self.frame11, width=12, text='ALTERAR', font=fontExample)

        bt1['command'] = partial(FuncoesBiblioteca.AlterarSenha, self, ce_nome, ce_Confirmarsenha, ce_senha)
        bt0['command'] = partial(Tela.VoltarMenuAlter, self, self.frame11, 'Login')

        self.frame11.place(x=0, y=0)
        lb_nome.place(x=80, y=150)
        ce_nome.place(x=145, y=152)
        lb_senha.place(x=73, y=200)
        ce_senha.place(x=145, y=202)
        lb_Confirmarsenha.place(x=50, y=250)
        ce_Confirmarsenha.place(x=145, y=252)
        bt0.place(x=160, y=300)
        bt1.place(x=260, y=300)

    def Escolha(self, janela):
        self.janela.title('Escolha')
        FuncoesBiblioteca.CriarTema(self, 'superhero')
        fontExample0 = tkFont.Font(family="arial black", size=14, weight="bold", slant="italic")
        fontExample1 = tkFont.Font(family="impact", size=24, weight="bold")
        fontExample = tkFont.Font(family="arial", size=14, weight="bold", slant="italic")
        radio2 = StringVar()

        self.frame4 = Frame(janela, width=500, height=500)

        bt0 = Button(self.frame4, width=10, text='Prosseguir', font=fontExample, fg='black')
        bt1 = Button(self.frame4, width=10, text='Voltar', font=fontExample, fg='black')

        bt0['command'] = partial(FuncoesBiblioteca.Escolher, self, radio2)
        bt1['command'] = partial(Tela.VoltarMenu, self, self.frame4, 'Login')

        lb_nome = Label(self.frame4, text='O QUE DESEJA FAZER?', font=fontExample1, fg='orange')

        FuncoesBiblioteca.CriarTema(self, '').configure('TRadiobutton', font=fontExample0)
        FuncoesBiblioteca.CriarTema(self, '').map('TRadiobutton', foreground=[
            ('disabled', 'info.TRadiobutton'),
            ('selected', 'yellow'),
            ('!selected', 'white')])
        radio = ttk.Radiobutton(self.frame4, text='Alugar', value='r', variable=radio2, style='custom.TRadiobutton')
        radio1 = ttk.Radiobutton(self.frame4, text='Devolver', value='r1', variable=radio2, style='custom.TRadiobutton')
        radio2 = ttk.Radiobutton(self.frame4, text='Prorrogar Aluguel', value='r2', variable=radio2, style='custom.TRadiobutton')

        self.frame4.place(x=0, y=0)
        bt1.place(x=130, y=420)
        bt0.place(x=260, y=420)
        lb_nome.place(x=110, y=50)
        radio.place(x=200, y=200)
        radio1.place(x=200, y=250)
        radio2.place(x=200, y=300)

    def TelaAlugar(self, janela):

        FuncoesBiblioteca.CriarTema(self, 'superhero')
        fontExample = tkFont.Font(family="Arial", size=11, weight="bold", slant="italic")
        self.janela.title('Alugar')

        self.frame3 = Frame(janela, width=500, height=500,  bg='brown')
        bt0 = Button(self.frame3, width=10, text='Alugar', font=fontExample, fg='black')
        bt1 = Button(self.frame3, width=10, text='Voltar', font=fontExample, fg='black')
        bt2 = Button(self.frame3, width=10, text='Pesquisar', font=fontExample, fg='black')
        lb_titulo = Label(self.frame3, text='Título:', font=fontExample, bg='brown')
        ce_titulo = Entry(self.frame3, width=18, fg='black')
        lb_autor = Label(self.frame3, text='Autor:', font=fontExample, bg='brown')
        ce_autor = Entry(self.frame3, width=18, fg='black')
        Tela.TreeviewAlugar(self, self.frame3)

        bt0['command'] = partial(FuncoesBiblioteca.__init__, self)
        bt2['command'] = partial(FuncoesBiblioteca.PesquisarAlugar, self, self.dados, ce_titulo,
                                 ce_autor, self.ce_nome)
        bt1['command'] = partial(Tela.VoltarMenu, self, self.frame3, 'Escolha')

        self.frame3.place(x=0, y=0)
        bt1.place(x=160, y=420)
        bt0.place(x=260, y=420)
        bt2.place(x=205, y=110)
        lb_titulo.place(x=140, y=50)
        ce_titulo.place(x=100, y=80)
        lb_autor.place(x=320, y=50)
        ce_autor.place(x=280, y=80)

    def TelaDevolver(self, janela):
        FuncoesBiblioteca.CriarTema(self, 'superhero')
        fontExample = tkFont.Font(family="Arial", size=11, weight="bold", slant="italic")
        self.janela.title('Devolver')

        self.frame5 = Frame(janela, width=500, height=500)
        bt0 = Button(self.frame5, width=10, text='Devolver', font=fontExample, fg='black')
        bt1 = Button(self.frame5, width=10, text='Voltar', font=fontExample, fg='black')
        bt2 = Button(self.frame5, width=10, text='Pesquisar', font=fontExample, fg='black')
        lb_nome = Label(self.frame5, text='Diga Seu Nome:', font=fontExample)
        ce_nome = Entry(self.frame5, width=18)

        Tela.TreeviewDevolver(self, self.frame5)

        bt0['command'] = partial(FuncoesBiblioteca.Devolver, self)
        bt2['command'] = partial(FuncoesBiblioteca.PesquisarDevolver, self, self.dados, ce_nome)
        bt1['command'] = partial(Tela.VoltarMenu, self, self.frame5, 'Escolha')

        self.frame5.place(x=0, y=0)
        bt1.place(x=160, y=420)
        bt0.place(x=260, y=420)
        bt2.place(x=205, y=110)
        lb_nome.place(x=190, y=50)
        ce_nome.place(x=180, y=80)

    def TelaProrrogar(self, janela):
        FuncoesBiblioteca.CriarTema(self, 'superhero')
        fontExample = tkFont.Font(family="Arial", size=11, weight="bold", slant="italic")
        self.janela.title('Prorrogar')

        self.frame10 = Frame(janela, width=500, height=500, bg='purple')
        bt0 = Button(self.frame10, width=10, text='Prorrogar', font=fontExample, fg='black')
        bt1 = Button(self.frame10, width=10, text='Voltar', font=fontExample, fg='black')
        bt2 = Button(self.frame10, width=10, text='Pesquisar', font=fontExample, fg='black')
        lb_nome = Label(self.frame10, text='Diga Seu Nome:', font=fontExample, bg='purple')
        ce_nome = Entry(self.frame10, width=18)
        Tela.TreeviewProrrogar(self, self.frame10)

        bt0['command'] = partial(FuncoesBiblioteca.AdiarDevolucao, self)
        bt2['command'] = partial(FuncoesBiblioteca.PesquisarProrrogar, self, self.dados, ce_nome)
        bt1['command'] = partial(Tela.VoltarMenu, self, self.frame10, 'Escolha')

        self.frame10.place(x=0, y=0)
        bt1.place(x=160, y=420)
        bt0.place(x=260, y=420)
        bt2.place(x=205, y=110)
        lb_nome.place(x=190, y=50)
        ce_nome.place(x=180, y=80)

    def Treeview(self, frame):
        fontExample = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")
        fontExample1 = tkFont.Font(family="Arial", size=14, weight="bold", slant="italic")
        omni = ttk.Style()
        omni.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                       font=(fontExample))  # Modify the font of the body
        omni.configure("mystyle.Treeview.Heading", font=fontExample1)  # Modify the font of the headings
        omni.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.dados = ttk.Treeview(frame, style="mystyle.Treeview", selectmode='browse', columns=[1, 2], show='headings')
        self.dados.column(1, width=200)
        self.dados.column(2, width=200)
        self.dados.heading(1, text='Código')
        self.dados.heading(2, text='Nome')
        self.dados.bind('<<TreeviewSelect>>')
        self.dados.place(x=50, y=165)

    def TreeviewAlugar(self, frame):
        fontExample = tkFont.Font(family="Arial", size=12, weight="bold", slant="italic")
        omni = ttk.Style()
        omni.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                       font=(fontExample))  # Modify the font of the body
        omni.configure("mystyle.Treeview.Heading", font=fontExample)  # Modify the font of the headings
        omni.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.dados = ttk.Treeview(frame, style="mystyle.Treeview", selectmode='browse',
                                  columns=[1, 2, 3], show='headings')
        self.dados.column(1, width=130)
        self.dados.column(2, width=130)
        self.dados.column(3, width=130)
        self.dados.heading(1, text='Titulo')
        self.dados.heading(2, text='Nome')
        self.dados.heading(3, text='Status')
        self.dados.bind('<<TreeviewSelect>>')
        self.dados.place(x=50, y=165)

    def TreeviewDevolver(self, frame):
        fontExample = tkFont.Font(family="Arial", size=12, weight="bold", slant="italic")
        omni = ttk.Style()
        omni.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                       font=(fontExample))  # Modify the font of the body
        omni.configure("mystyle.Treeview.Heading", font=fontExample)  # Modify the font of the headings
        omni.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.dados = ttk.Treeview(frame, style="mystyle.Treeview", selectmode='browse',
                                  columns=[1, 2, 3], show='headings')
        self.dados.column(1, width=130)
        self.dados.column(2, width=130)
        self.dados.column(3, width=130)
        self.dados.heading(1, text='Titulo')
        self.dados.heading(2, text='Nome')
        self.dados.heading(3, text='Entrega')
        self.dados.bind('<<TreeviewSelect>>')
        self.dados.place(x=50, y=165)

    def TreeviewProrrogar(self, frame):
        fontExample = tkFont.Font(family="Arial", size=12, weight="bold", slant="italic")
        omni = ttk.Style()
        omni.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                       font=(fontExample))  # Modify the font of the body
        omni.configure("mystyle.Treeview.Heading", font=fontExample)  # Modify the font of the headings
        omni.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.dados = ttk.Treeview(frame, style="mystyle.Treeview", selectmode='browse',
                                  columns=[1, 2, 3], show='headings')
        self.dados.column(1, width=130)
        self.dados.column(2, width=130)
        self.dados.column(3, width=130)
        self.dados.heading(1, text='Titulo')
        self.dados.heading(2, text='Nome')
        self.dados.heading(3, text='Entrega')
        self.dados.bind('<<TreeviewSelect>>')
        self.dados.place(x=50, y=165)

    def SairCadastro(self, x, y, z, frame, msg):

        if x.get() != '' or y.get() != '' or z.get() != '':
            MsgBox = messagebox.askquestion('Exit', 'Seus Dados Não Serão Salvos, Deseja sair?', icon='question')
            if MsgBox == 'yes':
                frame.place_forget()
                try:
                    self.frame2.place_forget()
                except:
                    Tela.CriarMenu(self, self.frame0)
                    self.janela.title(msg)

        else:
            frame.place_forget()
            try:
                self.frame2.place_forget()
                Tela.CriarMenu(self, self.frame0)
                self.janela.title(msg)
            except:
                Tela.CriarMenu(self, self.frame0)
                self.janela.title(msg)

    def VoltarMenu(self, frame, msg):
        frame.place_forget()
        Tela.CriarMenu(self, self.frame0)
        self.janela.title(msg)

    def VoltarMenuAlter(self, frame, msg):
        frame.place_forget()
        self.janela.title(msg)

    def CriarMenu(self, frame0):
        menubar = Menu(frame0)
        Menu1 = Menu(menubar, tearoff=0)
        Menu1.add_command(label="Entrar", command=lambda: Tela.Login(self, self.janela))
        Menu1.add_command(label="Cadastrar", command=lambda: Tela.TelaCadastro(self, self.janela))
        Menu1.add_command(label="Contato", command=lambda: tc.Contato(self.janela))
        Menu1.add_separator()
        Menu1.add_command(label="Sair", command=lambda: self.janela.destroy())
        menubar.add_cascade(label="O que você deseja?", menu=Menu1)
        self.janela.config(menu=menubar)


class FuncoesBiblioteca:

    def __init__(self):
        if self.dados1 == 'disponível':
            Date_required = date.today() + timedelta(days=15)
            try:
                itemselect = self.dados.selection()[0]
                valor = self.dados.item(itemselect, 'values')
                valor1 = valor[0]
                valor2 = valor[1]
                comando_SQL = f'INSERT INTO livro_alugado(nome_livro, autor, data_entrega, nome_pessoa) ' \
                              f'VALUES(%s, %s, %s, %s)'
                dados = (valor1, valor2, Date_required, self.ce.get())
                cursor.execute(comando_SQL, dados)
                MsgBox = messagebox.showerror('Success', 'Livro Alugado', icon='info')

                '''UPDATE relatorios SET data = DATE_FORMAT(data,'%Y-01-%d')'''
            except:
                MsgBox = messagebox.showerror('Error', 'Comando Inválido', icon='error')
        else:
            MsgBox = messagebox.showerror('Warning', 'Livro Indisponível', icon='warning')

    def Devolver(self):
        try:
            itemselect = self.dados.selection()[0]
            valor = self.dados.item(itemselect, 'values')
            comando_SQL = f'delete from livro_alugado where nome_livro = "{valor[0]}" limit 1  '
            cursor.execute(comando_SQL)
            banco.commit()
            MsgBox = messagebox.showerror('Success', 'Livro Devolvido', icon='info')

        except:
            MsgBox = messagebox.showerror('Error', 'Comando Inválido', icon='error')

    def AdiarDevolucao(self):
        try:
            '''itemselect = self.dados.selection()[0]
            valor = self.dados.item(itemselect, 'values')
            comando_SQL = f'select data_entrega from livro_alugado where nome_pessoa = "{self.ce.get()}" limit 1  '
            data = cursor.fetchall()
            cursor.execute(comando_SQL)
            banco.commit()
            if datetime.datetime.now() < data:'''
            itemselect = self.dados.selection()[0]
            valor = self.dados.item(itemselect, 'values')
            comando_SQL = f'update livro_alugado set data_entrega = "{date.today() + timedelta(days=16)}" where nome_livro = "{valor[0]}" limit 1'
            cursor.execute(comando_SQL)
            banco.commit()
            MsgBox = messagebox.showerror('Success', 'Entrega Prorrogado', icon='info')

        except:
            MsgBox = messagebox.showerror('Error', 'Comando Inválido', icon='error')

    def CriarTema(self, name):
        self.style = Style(name)
        return self.style

    def Cadastrar(self, senha, conf_senha, nome):
        try:
            if senha.get() != conf_senha.get():
                MsgBox = messagebox.showerror('Error', 'As Senhas São Divergentes', icon='error')
            else:
                comando_SQL = f'INSERT INTO login(senha, usuario) VALUES(%s, %s)'
                dados = (conf_senha.get(), nome.get())
                cursor.execute(comando_SQL, dados)
                banco.commit()
                MsgBox = messagebox.showerror('Error', 'Usuário Cadastrado', icon='error')

        except:
            MsgBox = messagebox.showerror('Error', 'Comando Inválido', icon='warning')

    def Pesquisar(self, frame, ce_titulo, ce_autor):
        try:
            if ce_autor.get() == '':
                comando_SQL = f'select * from livros where nome_livro = "{ce_titulo.get()}" limit 1  '
                cursor.execute(comando_SQL)
                dados = cursor.fetchall()
                banco.commit()
                frame.insert('', 'end', values=(dados[0]))
                ce_titulo.delete([0], [len(ce_titulo.get())])
                ce_autor.delete([0], [len(ce_autor.get())])

            elif ce_titulo.get() == '':
                comando_SQL = f'select * from livros where autor = "{ce_autor.get()}" limit 1  '
                cursor.execute(comando_SQL)
                dados = cursor.fetchall()
                banco.commit()
                frame.insert('', 'end', values=(dados[0]))
                ce_titulo.delete([0], [len(ce_titulo.get())])
                ce_autor.delete([0], [len(ce_autor.get())])

            elif ce_titulo.get() != '' and ce_autor.get() != '':
                comando_SQL = f'select * from livros where autor = "{ce_autor.get()}" limit 1  '
                cursor.execute(comando_SQL)
                dados = cursor.fetchall()
                banco.commit()
                frame.insert('', 'end', values=(dados[0]))
                ce_titulo.delete([0], [len(ce_titulo.get())])
                ce_autor.delete([0], [len(ce_autor.get())])

        except:
            MsgBox = messagebox.showerror('Error', 'Livro Não Consta Em Nosso Acervo', icon='error')
            ce_titulo.insert([0], '')
            ce_autor.insert([0], ' ')

    def PesquisarAlugar(self, frame, ce_titulo, ce_autor, ce_nome):
        self.ce = ce_nome
        try:
            comando_SQL = f'select autor from livro_alugado where nome_livro = "{ce_titulo.get()}" limit 1  '
            cursor.execute(comando_SQL)
            self.dados1 = cursor.fetchall()
            banco.commit()

            if len(self.dados1) == 0:
                self.dados1 = 'disponível'

            elif self.dados1[0][0] != '':
                self.dados1 = 'indisponível'

        except:
            pass

        try:
            if ce_autor.get() == '':
                comando_SQL = f'select * from livros where nome_livro = "{ce_titulo.get()}" limit 1  '
                cursor.execute(comando_SQL)
                dados = cursor.fetchall()
                frame.insert('', 'end', values=(dados[0][0], dados[0][1], self.dados1))
                ce_titulo.delete([0], [len(ce_titulo.get())])
                ce_autor.delete([0], [len(ce_autor.get())])

            elif ce_titulo.get() == '':
                comando_SQL = f'select * from livros where autor = "{ce_autor.get()}" limit 1  '
                cursor.execute(comando_SQL)
                dados = cursor.fetchall()
                banco.commit()
                frame.insert('', 'end', values=(dados[0][0], dados[0][1], self.dados1))
                ce_titulo.delete([0], [len(ce_titulo.get())])
                ce_autor.delete([0], [len(ce_autor.get())])

            elif ce_titulo.get() != '' and ce_autor.get() != '':
                comando_SQL = f'select * from livros where autor = "{ce_autor.get()}" limit 1  '
                cursor.execute(comando_SQL)
                dados = cursor.fetchall()
                banco.commit()
                frame.insert('', 'end', values=(dados[0][0], dados[0][1], self.dados1))
                ce_titulo.delete([0], [len(ce_titulo.get())])
                ce_autor.delete([0], [len(ce_autor.get())])

        except:
            MsgBox = messagebox.showerror('Error', 'Livro Não Consta Em Nosso Acervo', icon='error')
            ce_titulo.insert([0], '')
            ce_autor.insert([0], ' ')

    def PesquisarDevolver(self, frame, ce_nome):
        try:
            comando_SQL = f'select * from livro_alugado where nome_pessoa = "{ce_nome.get()}" limit 1  '
            cursor.execute(comando_SQL)
            dados = cursor.fetchall()
            print(dados)
            frame.insert('', 'end', values=(dados[0][0], dados[0][1], dados[0][2]))

        except:
            MsgBox = messagebox.showerror('Error', 'Livro Não Consta Em Nosso Acervo', icon='error')

    def PesquisarProrrogar(self, frame, ce_nome):
        try:
            comando_SQL = f'select * from livro_alugado where nome_pessoa = "{ce_nome.get()}" limit 1  '
            cursor.execute(comando_SQL)
            dados = cursor.fetchall()
            frame.insert('', 'end', values=(dados[0][0], dados[0][1], dados[0][2]))

        except:
            MsgBox = messagebox.showerror('Error', 'Comando Inválido', icon='error')

    def Validar(self, ce_nome, ce_senha, janela):

        comando_SQL = f'select * from login where usuario = "{ce_nome.get()}" limit 1  '
        cursor.execute(comando_SQL)
        dados = cursor.fetchall()
        banco.commit()
        print(dados)
        comando_SQL = f'select * from login where senha = "{ce_senha.get()}" limit 1  '
        cursor.execute(comando_SQL)
        dados1 = cursor.fetchall()
        print(dados1)
        banco.commit()
        if len(dados) == 0 or len(dados1) == 0:
            MsgBox = messagebox.showerror('Error', 'Usuário ou senha Inválidos', icon='error')


        else:
            Tela.Escolha(self, janela)

    def AlterarSenha(self, ce_nome, ce_confirm, ce_senha):

        comando_SQL = f'select * from login where usuario = "{ce_nome.get()}" limit 1  '
        cursor.execute(comando_SQL)
        dados = cursor.fetchall()
        banco.commit()
        if len(dados) == 0:
            MsgBox = messagebox.showerror('Error', 'Usuário Inexistente', icon='error')
        else:
            if ce_senha.get() != ce_confirm.get():
                MsgBox = messagebox.showerror('Error', 'As Senhas São Divergentes', icon='error')
            else:
                comando_SQL = f'update login set senha = "{ce_confirm.get()}" where usuario = "{ce_nome.get()}" limit 1'
                cursor.execute(comando_SQL)
                banco.commit()
                MsgBox = messagebox.showerror('Success', 'Senha Alterada', icon='info')

    def Escolher(self, var):

        if var.get() == 'r':
            Tela.TelaAlugar(self, self.janela)

        elif var.get() == 'r1':
            Tela.TelaDevolver(self, self.janela)

        elif var.get() == 'r2':
            Tela.TelaProrrogar(self, self.janela)
        else:
            MsgBox = messagebox.showerror('Error', 'Marque Um dos Campos Para Continuar', icon='info')


tela = Tela()