# web-scraping-python
API para scraping de dados do SimilarWeb e armazená-los em um banco de dados MongoDB

## Como rodar o projeto?

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
