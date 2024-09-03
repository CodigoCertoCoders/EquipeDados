import pandas as pd
import warnings

warnings.filterwarnings("ignore", 
                        message="Could not infer format, so each element will be parsed individually, "
                        "falling back to `dateutil`")

def formatar_telefone(numero):
    """Formata números de telefone para o formato +XXXXXXXXXXXXXXX.
    Adiciona o código do país +55 se não estiver presente e remove caracteres não numéricos, exceto "+".
    """
    numero = ''.join(c for c in numero if c.isdigit() or c == '+')
    if numero.startswith('+'):
        numero_formatado = numero
    else:
        numero_formatado = '+55' + numero
    numero_formatado = ''.join(c for c in numero_formatado if c.isdigit())
    return f"+{numero_formatado}"

def formatar_frameworks(frameworks):
    """Formata a lista de frameworks e bibliotecas.
    Converte cada item para o formato de título e remove espaços extras, mantendo a ordem original.
    Se o item começar com um ponto seguido de um espaço, o ponto é unido com a próxima letra.
    """
    if isinstance(frameworks, str) and len(frameworks) > 2:
        frameworks_list = [f.strip().title() for f in frameworks.split(',')]
        formatted_list = []
        for f in frameworks_list:
            if f.startswith('. '):
                formatted_list.append('.' + f[2:])
            else:
                formatted_list.append(f)
        return ', '.join(formatted_list)
    else:
        return ''
    
def main():
    """ Retorna um dataframe com as keys: ['timestamp', 'nome_completo', 'whatsapp_numero', 'interesse_voluntario',
       'nivel_experiencia', 'areas_interesse', 'linguagens_ferramentas',
       'frameworks_bibliotecas', 'disponibilidade_horario',
       'preferencias_colaboracao', 'liderar_projetos']"""

    diretorio_local = '../data/Código Certo Coders.csv'
    try:
        df_planilha_hackaton = pd.read_csv(diretorio_local, sep=',')
    except FileNotFoundError:
        print(f"Erro: O arquivo {diretorio_local} não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
    except pd.errors.ParserError:
        print("Erro: Ocorreu um erro ao analisar o arquivo.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    df_planilha_hackaton.rename(columns={
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
    }, inplace=True)
    df_planilha_hackaton['timestamp'] = pd.to_datetime(df_planilha_hackaton['timestamp'], errors='coerce')
    df_planilha_hackaton['timestamp'] = df_planilha_hackaton['timestamp'].dt.strftime('%d/%m/%Y - %H:%M:%S')
    df_planilha_hackaton['nome_completo'] = df_planilha_hackaton['nome_completo'].str.title()
    df_planilha_hackaton['whatsapp_numero'] = df_planilha_hackaton['whatsapp_numero'].apply(formatar_telefone)
    df_planilha_hackaton['frameworks_bibliotecas'] = df_planilha_hackaton['frameworks_bibliotecas'].apply(formatar_frameworks)
    return df_planilha_hackaton
    

if __name__ == '__main__':
    main()