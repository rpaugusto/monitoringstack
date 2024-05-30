from flask import Flask
import requests
from bs4 import BeautifulSoup
import json
import re

app = Flask(__name__)

# Função para mapear o valor da imagem para o número correspondente
def map_image_value(image_src):
    if 'bola_verde_P' in image_src:
        return 1
    elif 'bola_amarelo_P' in image_src:
        return 2
    elif 'bola_vermelho_P' in image_src:
        return 3
    else:
        return None

# Função para extrair os dados da tabela e gerar um JSON
def extract_table_data(table):
    # Lista para armazenar as chaves
    keys = []
    # Lista para armazenar os objetos JSON
    data = []

    # Iterando sobre as linhas da tabela
    for row in table.find_all('tr'):
        # Se for a primeira linha, extrair as chaves
        if not keys:
            keys = [cell.get_text(strip=True) for cell in row.find_all('th')]
        else:
            # Para as linhas subsequentes, criar um objeto JSON com base nas chaves
            row_data = {}
            # O primeiro elemento em cada linha é o nome da série
            row_data[keys[0]] = row.find('td').get_text(strip=True)
            # As demais colunas contêm imagens, mapeamos seus valores
            for i, cell in enumerate(row.find_all('td')[1:], start=1):
                # Verificando se a célula contém uma tag <img>
                img_tag = cell.find('img')
                if img_tag:
                    # Se contém, obtemos o valor do atributo 'src'
                    image_src = img_tag.get('src')
                    row_data[keys[i]] = map_image_value(image_src)
                else:
                    # Se não contém, atribuímos None
                    row_data[keys[i]] = None
            data.append(row_data)

    return data

@app.route('/')
def index():
    return "endpoint Python"


@app.route('/sefaz')
def sefaz():
    # Fazendo uma solicitação GET para a página
    url = 'https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=P2c98tUpxrI='
    response = requests.get(url)

    # Verificando se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Analisando o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrando a tabela pelo ID
        table = soup.find(id='ctl00_ContentPlaceHolder1_gdvDisponibilidade2')
        
        # Verificando se a tabela foi encontrada
        if table:
            # Extraindo os dados da tabela
            table_data = extract_table_data(table)
            
            ## Convertendo os dados para JSON
            #json_data = json.dumps(table_data, indent=4)

            # Decodificar o JSON e corrigir os caracteres escapados
            cleaned_json = json.dumps(table_data, ensure_ascii=False).encode('utf-8').decode('unicode-escape')

            return cleaned_json
        else:
            return "Tabela não encontrada."
    else:
        return "Falha ao obter a página."

if __name__ == '__main__':
    app.run()