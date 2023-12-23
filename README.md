# web-scraping-python
API para scraping de dados do SimilarWeb e armazená-los em um banco de dados MongoDB

## Como rodar o projeto?
#### E necessario ter o mangodb instalado, faça a instalação dele e modifique as linhas de configuração de conexão no projeto, no arquivo api_fast.py
para as configurações do seu banco de dados.

#### Configurações para conexão com o MongoDB
client = MongoClient('localhost', 27017) 

db = client['MyDatabaseSimularWeb']  

colecao = db['SimularWebInfo']

### Criar e Ativar o Ambiente Virtual (venv)
No Windows:
#### Criar o ambiente virtual
python -m venv meu_ambiente
#### Ativa o ambiente virtual
meu_ambiente\Scripts\activate

No macOS e Linux:
#### Cria um ambiente virtual chamado 'meu_ambiente'
python3 -m venv meu_ambiente

#### Ativa o ambiente virtual
source meu_ambiente/bin/activate

### Instalar Requisitos (Requirements)
*Certifique-se de estar no ambiente virtual antes de prosseguir*

#### Instala os requisitos do arquivo requirements.txt
pip install -r requirements.txt

### Rodar um Projeto FastAPI
Supondo que você tenha um arquivo chamado main.py que contém o projeto FastAPI, você pode executá-lo assim:

uvicorn api_fast:app --reload
