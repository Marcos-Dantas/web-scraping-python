from fastapi import FastAPI, HTTPException, Request
from pymongo import MongoClient
from web_scraping import make_scraping, all_fields_required_on_response

app = FastAPI()

# Configurações para conexão com o MongoDB
client = MongoClient('localhost', 27017) 
db = client['MyDatabaseSimularWeb']  
colecao = db['SimularWebInfo']

async def validate_response(json_response):
    if json_response == '404' :
        return False

    if not (all_fields_required_on_response.issubset(json_response.keys())):
        return False

    return True

@app.post('/salve_info/', status_code=201)
async def save_information(request: Request):
    '''
        POST /salve_info: Este endpoint deve receber uma URL de um site, 
        realizar o scraping dos dados no SimilarWeb e salvar as informações no MongoDB.
    '''
    # Acessando o corpo da solicitação diretamente
    request = await request.json()
    url = request.get("url")

    json_response = await make_scraping(url)
    
    if await validate_response(json_response):
        # Converter o JSON em um documento
        if not colecao.find_one({'website': url}):
            response = colecao.insert_one(json_response)
        else:
            colecao.replace_one(
                {'website': url},  # Filtro para encontrar o documento a ser substituído
                json_response,  # Novo documento que substituirá o existente
            )
            response = colecao.find_one({'website': url})
        
        # Verificar se o documento foi inserido ou atualizado com sucesso
       
        new_id = str(response['_id'])
        
        # Retorna o ID gerado junto com os dados inseridos e o status code 201 (Created)
        return {"id": new_id}

    else:
        raise HTTPException(status_code=404, detail="Ocorreu um erro nesta rota.")

@app.post('/get_info/')
async def get_information(request: Request):
    '''
        POST /get_info: Este endpoint deve receber uma URL, buscar as 
        informações do site no banco de dados e retorná-las. Se as informações 
        ainda não estiverem disponíveis, deve retornar um código de erro.
    '''
    # Acessando o corpo da solicitação diretamente
    request = await request.json()
    url = request.get("url")
    
    response = colecao.find_one({'website': url})

    # Retornando o dicionário como JSON
    if response:
        response['_id'] = str(response['_id'])
        return response
    else:
        raise HTTPException(status_code=404, detail="Ocorreu um erro nesta rota.")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
