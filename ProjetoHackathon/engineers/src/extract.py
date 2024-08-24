import os
import gdown

def baixar_arquivos_google_drive(url_pasta, diretorio_local):
    '''Baixa todos os arquivos de uma pasta do Google Drive para o diretório local especificado.'''
    os.makedirs(diretorio_local, exist_ok=True)
    try:
        gdown.download_folder(url_pasta, output=diretorio_local, quiet=False, use_cookies=False)
    except Exception as e:
        print(f'Erro ao baixar arquivos: {e}')
        return False
    return True

def listar_arquivos_csv(diretorio):
    '''Lista todos os arquivos CSV no diretório especificado e os retorna como uma lista de caminhos completos.'''
    try:
        arquivos_csv = [os.path.join(diretorio, arquivo) for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]
        return arquivos_csv
    except FileNotFoundError:
        print(f'O diretório \'{diretorio}\' não foi encontrado.')
        return []
    except PermissionError:
        print(f'Permissão negada ao acessar o diretório \'{diretorio}\'.')
        return []

def main():
    url_pasta = 'https://drive.google.com/drive/folders/1TkyHYcJ0U_dWYeoxaBY_di-WgLNlA5mF'
    diretorio_local = './ProjetoHackathon/engineers/data'
    
    if baixar_arquivos_google_drive(url_pasta, diretorio_local):
        arquivos_csv = listar_arquivos_csv(diretorio_local)
        print('Arquivos CSV encontrados:', arquivos_csv)
    else:
        print('Falha no download dos arquivos.')

if __name__ == '__main__':
    main()