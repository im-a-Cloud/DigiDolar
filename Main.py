import requests
from PIL import Image
from io import BytesIO
import webbrowser
from googlesearch import search

#função que baixa as imagens na máquina em um arquivo
def baixar_imagem_digimon(url, nome_arquivo):
    # Faz a requisição GET para o URL fornecido
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Abre um arquivo em modo de escrita binária e escreve o conteúdo da imagem
        with open(nome_arquivo, 'wb') as file:
            file.write(response.content)
        print(f'Imagem baixada com sucesso como {nome_arquivo}')
    else:
        print(f'Falha ao baixar imagem. Código de status: {response.status_code}')
#baixa a imagem temporariamente
def baixar_imagem(url):
    # Faz a requisição GET para o URL fornecido
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        print(f'Falha ao baixar imagem. Código de status: {response.status_code}')
        return None

#função para exibir a imagem do digimon(não funciona como eu quero)
def mostrar_imagem_digimon(imagem_bytes):
    if imagem_bytes:
        # Abre a imagem usando Pillow
        img = Image.open(imagem_bytes)
        # Exibe a imagem
        img.show()
    else:
        print("Nenhuma imagem para exibir.")

UrlDolar = "https://economia.awesomeapi.com.br/json/last/USD-BRL" 
#metodo get da api para pegar o valor atual do Dolar Americano em Reais do Brasil

resposta = requests.get(UrlDolar)

if resposta.status_code == 200: #se a requisição deu certo
    dados_dolar = resposta.json() #pega todo os dados do .json

    valor_dolar = round(float(dados_dolar['USDBRL']['bid']),2) #pega o campo do json com o valor do dolar e arredonda para 2 casas decimais
    valor_dolar_em_string = str(valor_dolar).replace(".","") #remove o ponto pois é uma string

    urlDigimon = f"https://digi-api.com/api/v1/digimon/{valor_dolar_em_string}"
    #metodo get para pegar o digimon com o id na 'digidex' relacionado

    print(f'URL da API Digimon: {urlDigimon}')
    print(f'O valor do dólar é: {valor_dolar}')
    print(f'O número que representa o digimom é: {valor_dolar_em_string}')
    #um debug simples

    resposta_digimon = requests.get(urlDigimon)
    #pega os dados do digimon

    if resposta_digimon.status_code == 200:
        dados_digimon = resposta_digimon.json()
        nome_digimon = dados_digimon['name'] #nome do digimon
        link_digimon = dados_digimon['images'][0]['href'] #link da sua imagem na wiki de digimon
        #nome_arquivo = 'digimon_valor_dolar.png'
        #baixar_imagem_digimon(link_digimon, nome_arquivo)
        print(nome_digimon)
        print(link_digimon)
    print(valor_dolar)
    imagem_digimon = baixar_imagem(link_digimon)
    #mostrar_imagem_digimon(imagem_digimon)
    webbrowser.open(link_digimon) #abre o navegador com a imagem do digimon
else:
    print(f'Erro na requisição: {resposta.status_code}')