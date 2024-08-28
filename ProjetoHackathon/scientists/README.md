 - ***Preparação do Ambiente***

Este README fornece instruções para configurar o ambiente necessário para executar os scripts de alocação de equipe e análise de dados. Seguindo estes passos, você garantirá que todas as dependências estejam instaladas e o ambiente esteja pronto para uso.

Requisitos
Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

Python 3.10 ou superior: Pode ser baixado do site oficial do Python.
pip: O gerenciador de pacotes do Python.
Configuração do Ambiente

- Programas: 
VS code 
pycharme comunity 


1. Criar e Ativar um Ambiente Virtual
Para manter as dependências isoladas, é recomendado usar um ambiente virtual. Execute os seguintes comandos no terminal:

bash
Copiar código
# Criar um ambiente virtual
python -m venv venv


# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate

2. Instalar Dependências
Instale as bibliotecas necessárias usando o pip. Crie um arquivo requirements.txt com o seguinte conteúdo e instale as dependências:

```requirements.txt```
```pandas==2.0.0```
```numpy==1.24.0```
```pulp==2.7.0```
```matplotlib==3.7.1```
```scikit-learn==1.3.0```


- ***Instale as dependências com o comando:***

bash
Copiar código
pip install -r requirements.txt


3. Executar o Script
Após preparar o ambiente e o script, você pode executar o script com o comando:

bash
Copiar código
git clone `` link do repositorio`` 

apos o git clone vai baixar todas as dependencias dos arquivos na pasta enginers 
tem um arquuivo dentro da pasta src chamnado extract.py que assim executado ele vai baixar o **arquivo.csv** .


 - ***Uso com Jupyter Notebook ou Google Colab***
  
Se você preferir usar Jupyter Notebook ou Google Colab, siga estas instruções:

Jupyter Notebook
Instalar o Jupyter Notebook

Se ainda não tiver o Jupyter Notebook instalado, você pode instalá-lo com o comando:

bash
Copiar código
pip install notebook
Iniciar o Jupyter Notebook

Inicie o Jupyter Notebook com o comando:

bash
Copiar código
jupyter notebook
Isso abrirá uma nova janela do navegador com o painel do Jupyter Notebook.

Criar um Novo Notebook

No painel do Jupyter Notebook, crie um novo notebook e cole o código do script alocacao_equipe.py nas células do notebook.

Executar o Notebook

Execute as células do notebook para processar os dados e gerar o arquivo CSV.

Google Colab
Abrir o Google Colab

Acesse Google Colab em seu navegador.

Criar um Novo Notebook

Crie um novo notebook clicando em "File" > "New notebook".

Instalar Dependências

Execute as seguintes células para instalar as dependências necessárias:

python
Copiar código
!pip install pandas pulp
Fazer Upload do Arquivo CSV

Faça upload do seu arquivo CSV para o Google Colab com o seguinte código:

python
Copiar código
from google.colab import files
uploaded = files.upload()
Isso abrirá uma caixa de diálogo para selecionar o arquivo CSV.

Colar e Executar o Código

**Cole o código do script alocacao_equipe.py em uma célula do notebook e execute a célula para processar os dados e gerar o arquivo CSV.**