
## Preparação do Ambiente

Este README fornece instruções para configurar o ambiente necessário para executar os scripts de alocação de equipe e análise de dados. Seguindo estes passos, você garantirá que todas as dependências estejam instaladas e o ambiente esteja pronto para uso.

### Requisitos

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

- **Python 3.10 ou superior:** Pode ser baixado do [site oficial do Python](https://www.python.org/downloads/).
- **pip:** O gerenciador de pacotes do Python.

### Configuração do Ambiente

#### Programas:

- VS Code
- PyCharm Community Edition

### 1. Criar e Ativar um Ambiente Virtual

Para manter as dependências isoladas, é recomendado usar um ambiente virtual. Execute os seguintes comandos no terminal:

```bash
# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate
```

### 2. Instalar Dependências

Instale as bibliotecas necessárias usando o pip. Crie um arquivo `requirements.txt` com o seguinte conteúdo e instale as dependências:

```txt
pandas==2.0.0
numpy==1.24.0
pulp==2.7.0
matplotlib==3.7.1
scikit-learn==1.3.0
```

**Instale as dependências com o comando:**

```bash
pip install -r requirements.txt
```

### 3. Executar o Script

Após preparar o ambiente e o script, você pode executar o script com o comando:

```bash
git clone [link do repositório]
```

Após o `git clone`, todas as dependências dos arquivos serão baixadas. Na pasta `engineers`, há um arquivo dentro da pasta `src` chamado `extract.py`. Ao executá-lo, ele fará o download do **arquivo.csv**.

### Uso com Jupyter Notebook ou Google Colab

#### Jupyter Notebook

1. **Instalar o Jupyter Notebook**

   Se ainda não tiver o Jupyter Notebook instalado, você pode instalá-lo com o comando:

   ```bash
   pip install notebook
   ```

2. **Iniciar o Jupyter Notebook**

   Inicie o Jupyter Notebook com o comando:

   ```bash
   jupyter notebook
   ```

   Isso abrirá uma nova janela do navegador com o painel do Jupyter Notebook.

3. **Criar um Novo Notebook**

   No painel do Jupyter Notebook, crie um novo notebook e cole o código do script `alocacao_equipe.py` nas células do notebook.

4. **Executar o Notebook**

   Execute as células do notebook para processar os dados e gerar o arquivo CSV.

#### Google Colab

1. **Abrir o Google Colab**

   Acesse o [Google Colab](https://colab.research.google.com/) em seu navegador.

2. **Criar um Novo Notebook**

   Crie um novo notebook clicando em "File" > "New notebook".

3. **Instalar Dependências**

   Execute as seguintes células para instalar as dependências necessárias:

   ```python
   !pip install pandas pulp
   ```

4. **Fazer Upload do Arquivo CSV**

   Faça upload do seu arquivo CSV para o Google Colab com o seguinte código:

   ```python
   from google.colab import files
   uploaded = files.upload()
   ```

   Isso abrirá uma caixa de diálogo para selecionar o arquivo CSV.

5. **Colar e Executar o Código**

   Cole o código do script `alocacao_equipe.py` em uma célula do notebook e execute a célula para processar os dados e gerar o arquivo CSV.
