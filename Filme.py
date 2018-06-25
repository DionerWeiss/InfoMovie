import urllib
import requests

class Movie():
    def __init__(self):
        #api_key, necessario para usar a api
        self.__api_key = "2aa83a7e309150394c61729525230237"
        self.nome = ""
        self.original_title = ""
        self.data_lancamento = ""
        #link da url principal
        self.__url = "https://api.themoviedb.org/3"
        #link da imagem
        self.__imagem_url = "https://image.tmdb.org/t/p/w500"
        self.production_companies = ""
        self.genres = ""

    def pesquisar(self, filme):
        self.__url = self.__url+"/search/movie?api_key={}&query={}".format(self.__api_key, filme)
        #self.__url = "https://api.themoviedb.org/3/movie/550?api_key=2aa83a7e309150394c61729525230237"
        link = requests.get(self.__url).json()
        try:
            if(link != None) or (link != ""):
                return link['results']
            else:
                return "Filme nao encontrado"
        except:
            return "Filme nao encontrado"

    def detalhes(self, id):
        url_details = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(str(id), self.__api_key)
        filme = requests.get(url_details).json()
        self.nome = filme['title']
        self.original_title = filme['original_title']
        self.data_lancamento = filme['release_date']
        for b in filme['production_companies']:
            self.production_companies = self.production_companies + b['name'] +"; "
        for a in filme['genres']:
            self.genres = self.genres + "; " + a['name']
            #self.genres.append(a['name'])
        self.baixar_imagem(filme['poster_path'])

    def baixar_imagem(self, link):
        image_url = self.__imagem_url +link
        urllib.request.urlretrieve(image_url, "jj.jpg")


