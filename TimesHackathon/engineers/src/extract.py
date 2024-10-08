import requests 
import io

def retornar_arquivo():
    url_arquivo = 'https://drive.google.com/uc?id=1JLpuGMPkhqYBCvC07k53lh0wtSz2UYGH&export=download'
    response = requests.get(url_arquivo)

    try:
        conteudo = io.StringIO(response.text)
        return conteudo
    except:
        return None
    
if __name__ == '__main__':
    retornar_arquivo()