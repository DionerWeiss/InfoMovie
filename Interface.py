
from tkinter import *
from Filme import *
from PIL import Image, ImageTk

class Application:
    def __init__(self, master=None):
        #primeiro container
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer["padx"] = 30
        self.primeiroContainer.pack()

        #segundo container
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        #label do nome
        self.nomeLabel = Label(self.primeiroContainer, text="Filme ou serie: ", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        #Entry do nome
        self.nomeEntry = Entry(self.primeiroContainer)
        self.nomeEntry["width"] = 30
        self.nomeEntry["font"]  = self.fontePadrao
        self.nomeEntry.insert(0, "Avengers")
        self.nomeEntry.pack(side=LEFT)

        #Btn pesquisar
        self.labelPesquisar = Button(self.segundoContainer, command=self.pesquisarFilme)
        self.labelPesquisar["text"] = "Pesquisar"
        self.labelPesquisar["font"] = ("Calibri", "12")
        self.labelPesquisar["width"] = 12
        self.labelPesquisar.pack()

    def pesquisarFilme(self):
        #pega o valor de nomeEntry e armazena na variavel filme
        filme = self.nomeEntry.get()

        #desempacota os pacotes do inicio
        self.desempacota_inicio()

        #cria um novo objeto Movie()
        m = Movie()
        #resultados recebe o retorno do metodo pesquisar
        resultados = m.pesquisar(filme)

        #criacao de labelMovies dentro do primeiro container
        self.labelMovies = Label(self.primeiroContainer)
        self.labelMovies['padx'] = 100
        self.labelMovies.pack()

        if (resultados != "Filme nao encontrado"):
            #percorre o dicionario resultados e cria um botao personalizado, com o nome e id do filme
            for a in resultados:
                self.criar_botao(a['title'], self.labelMovies, a['id'])
        #se o filme nao foi encontrado mostra a mensagem
        else:
            labelErro = Label(self.labelMovies, text="Filme nao encontrado")
            labelErro.pack()

        #botao voltar
        self.voltar = Button(self.segundoContainer, command=self.voltarInicio)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Calibri", "12")
        self.voltar["width"] = 12
        self.voltar.pack()


    #cria um botao, recebe o nome do botao, o label pai e o id do filme, para chamar o metodo mostra_detalhes()
    def criar_botao(self, nomeBtn, label, id):
        nomeBtn = Button(label, text = nomeBtn, command=lambda : self.motra_detalhes(id))
        nomeBtn['width'] = 40
        nomeBtn['pady'] = 5
        nomeBtn.pack()

    #voltar ao Inicio
    def voltarInicio(self):
        self.nomeLabel.pack(side=LEFT)
        self.nomeEntry.pack(side=LEFT)
        self.labelPesquisar.pack()
        self.voltar.pack_forget()
        self.labelMovies.pack_forget()

    #voltar para pesquisa
    def voltarPesquisa(self):
        self.labelMovies.pack()
        self.voltar['command'] = lambda : self.voltarInicio()
        self.voltar.pack()
        self.labelInfo.pack_forget()

    #desempacota os pacotes iniciais
    def desempacota_inicio(self):
        self.nomeEntry.pack_forget()
        self.nomeLabel.pack_forget()
        self.labelPesquisar.pack_forget()


    def motra_detalhes(self, id):
        #desempacota os pacotes do frame anterior, da pesquisabtnDetails
        self.desempacotar_pesquisa()
        #uso de try e except para evitar erros
        font = ("Arial", "12")
        try:

            #cria um novo obejto Movie()
            mo = Movie()
            #chama a funcao detalhes, que preenche os dados do filme
            mo.detalhes(id)
            root.title(mo.nome)
            #criacao do label das informacoes do filme
            self.labelInfo = Label(self.primeiroContainer)
            self.labelInfo.pack()

            #label local para armazenar a imagem
            labelImagem = Label(self.labelInfo)

            #abre a imagem
            photo = Image.open(r"jj.jpg")
            #redimenciona a imagem para o tamanho 200x300
            photo = photo.resize((200, 300), Image.ANTIALIAS)

            #link da imagen no label, necessario para a imagem aparecer
            labelImagem.image = ImageTk.PhotoImage(photo)
            #campo 'image' do label recebe o link da imagem salva
            labelImagem['image'] = labelImagem.image

            #criacao do label, dentro de labelInfo, onde sera exibido os dados
            labelData = Label(self.labelInfo, anchor=S)

            #criacao dos labels para cada dado
            labelNome = Message(labelData, text="Name: {}".format(mo.nome), width=430,font=font, pady=5)
            label_original_title = Message(labelData, text="Original Title: {}".format(mo.original_title), font=font, width=430, pady=5)
            label_release_date = Message(labelData, text="Release Date: {}".format(mo.data_lancamento), font=font,  width=430, pady=5)
            label_genres = Message(labelData, text="Genres: {}".format(mo.genres[1:]), font=font, width=430, pady=5)
            label_companies = Message(labelData, text="Production Companies: {}".format(mo.production_companies[:-2]), font=font, width=430, pady=5)

            #botao voltar recebe o comando para voltar para a pesquisa
            self.voltar['command'] = self.voltarPesquisa

            #empacota os pacotes
            labelImagem.pack(side=LEFT)
            labelNome.pack(anchor=W)
            label_original_title.pack(anchor=W)
            label_release_date.pack(anchor=W)
            label_genres.pack(anchor=W)
            label_companies.pack(anchor=W)
            labelData.pack()
        #except, caso algum link possua erro
        except:
            self.labelInfo = Label(self.primeiroContainer, text="Filme nao encontrado")
            self.labelInfo['width'] = 30
            self.labelInfo['font'] = ("Calibri", "25")
            self.labelInfo.pack()
            self.voltar['command'] = self.voltarPesquisa

    #desempacota os labels da pesquisa
    def desempacotar_pesquisa(self):
        self.labelMovies.pack_forget()
        self.labelPesquisar.pack_forget()


root = Tk()
Application(root)
root.title("Pesquisar")
root.mainloop()
