from transform import main
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

def get_engine():
    return create_engine(DATABASE_URL)

def insert_db():
    """Função para inserir dados no banco"""
    df = main()
    engine = get_engine()
    try:
        with engine.begin() as connection:
            df.to_sql(name='respostas_formulario', con=connection, if_exists='replace')
        print('Dados inseridos')
    except Exception as error:
        print(f'Ocorreu um erro ao inserir os dados: {error}')

def queries():
    """Função que faz consulta no banco. Não necessária para o load, mas montei para visualização"""
    engine = get_engine()
    query = 'SELECT * FROM respostas_formulario'
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))
            for row in result:
                print(row)
    except Exception as error:
        print(f'Ocorreu um erro ao executar a consulta: {error}')

if __name__ == '__main__':
    queries()
