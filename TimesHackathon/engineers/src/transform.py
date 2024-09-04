import pandas as pd
import warnings

"""Ignorar avisos referentes ao formato de data"""
warnings.filterwarnings(
    "ignore",
    message=(
        "Could not infer format, so each element will be parsed individually, "
        "falling back to `dateutil`"
    )
)

def formatar_telefone(numero_telefone):
    """Formata números de telefone para o formato +XXXXXXXXXXXXXXX.

    Adiciona o código do país +55 se não estiver presente e remove caracteres
    não numéricos, exceto "+".
    """
    numero_telefone = ''.join(caractere for caractere in numero_telefone
                               if caractere.isdigit() or caractere == '+')
    if numero_telefone.startswith('+'):
        numero_formatado = numero_telefone
    else:
        numero_formatado = '+55' + numero_telefone
    numero_formatado = ''.join(caractere for caractere in numero_formatado
                               if caractere.isdigit())
    return f"+{numero_formatado}"

def formatar_frameworks(lista_frameworks):
    """Formata a lista de frameworks e bibliotecas.

    Converte cada item para o formato de título e remove espaços extras, 
    mantendo a ordem original. Se o item começar com um ponto seguido de um
    espaço, o ponto é unido com a próxima letra.
    """
    if isinstance(lista_frameworks, str) and len(lista_frameworks) > 2:
        lista_formatada = []
        for framework in lista_frameworks.split(','):
            framework = framework.strip().title()
            if framework.startswith('. '):
                lista_formatada.append('.' + framework[2:])
            else:
                lista_formatada.append(framework)
        return ', '.join(lista_formatada)
    return ''

def transformar_dados():
    """Retorna um dataframe com as colunas formatadas.

    As colunas do dataframe são:
    ['timestamp', 'nome_completo', 'whatsapp_numero', 'interesse_voluntario',
     'nivel_experiencia', 'areas_interesse', 'linguagens_ferramentas',
     'frameworks_bibliotecas', 'disponibilidade_horario', 'preferencias_colaboracao',
     'liderar_projetos']
    """
    caminho_arquivo = './Data/voluntarioscomunidade.csv' 
    
    try:
        dataframe_voluntarios = pd.read_csv(caminho_arquivo, sep=',')
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
    except pd.errors.ParserError:
        print("Erro: Ocorreu um erro ao analisar o arquivo.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    
    dataframe_voluntarios.rename(
        columns={
            'Carimbo de data/hora': 'timestamp',
            'Nome Completo:': 'nome_completo',
            'WhatsApp (Número) ': 'whatsapp_numero',
            'Interesse em Projetos Voluntários:': 'interesse_voluntario',
            '  Nível de Experiência  ': 'nivel_experiencia',
            'Área(s) de Interesse:': 'areas_interesse',
            'Suas Principais Linguagens/Ferramentas:': 'linguagens_ferramentas',
            'Seus Frameworks/Bibliotecas (Exemplo: Angular, React, Laravel...)': 'frameworks_bibliotecas',
            'Disponibilidade de Horário:': 'disponibilidade_horario',
            'Preferências de Colaboração: (Trabalhar em equipe na área de TI é essencial para o sucesso de projetos. A colaboração permite a combinação de diversas habilidades e experiências, promove a troca de conhecimentos, estimula a criatividade e acelera o processo de aprendizado.)': 'preferencias_colaboracao',
            'Gostaria de Liderar Projetos?': 'liderar_projetos'
        },
        inplace=True
    )
    
    dataframe_voluntarios['timestamp'] = pd.to_datetime(dataframe_voluntarios['timestamp'], errors='coerce')
    dataframe_voluntarios['timestamp'] = dataframe_voluntarios['timestamp'].dt.strftime('%d/%m/%Y - %H:%M:%S')
    dataframe_voluntarios['nome_completo'] = dataframe_voluntarios['nome_completo'].str.title()
    dataframe_voluntarios['whatsapp_numero'] = dataframe_voluntarios['whatsapp_numero'].apply(formatar_telefone)
    dataframe_voluntarios['frameworks_bibliotecas'] = dataframe_voluntarios['frameworks_bibliotecas'].apply(formatar_frameworks)
    
    return dataframe_voluntarios
