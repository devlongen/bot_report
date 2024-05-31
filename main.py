# Importação das bibliotecas necessárias
import pandas as pd            # Biblioteca para manipulação de dados em dataframes
import openpyxl                # Biblioteca para trabalhar com arquivos Excel
import psycopg2                # Biblioteca para conectar e manipular bancos de dados PostgreSQL
from datetime import datetime  # Biblioteca para trabalhar com datas e horas
import os                      # Biblioteca para interagir com o sistema operacional
import glob                    # Biblioteca para buscar arquivos com padrões especificados
from googleapiclient.discovery import build   # Biblioteca para interagir com APIs do Google
from google.oauth2.service_account import Credentials   # Biblioteca para autenticação com contas de serviço do Google
from googleapiclient.http import MediaFileUpload  # Biblioteca para fazer upload de arquivos para o Google Drive

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    # Aqui deveriam estar os parâmetros de conexão, como dbname, user, password, host, port
)

cur = conn.cursor()  # Criação de um cursor para executar comandos SQL
print("Conexão concluída")

# Consulta SQL (deve ser especificada a query desejada)
query = """
    -- A consulta SQL deve ser inserida aqui
"""

cur.execute(query)  # Execução da consulta SQL
resultado_base = cur.fetchall()  # Recuperação dos resultados da consulta
print("Query executada e encaminhada")

cur.close()  # Fechamento do cursor
conn.close()  # Fechamento da conexão com o banco de dados
print("Conexão do banco fechada e cursor também")

# Conversão dos resultados da consulta para um DataFrame do pandas
df = pd.DataFrame(resultado_base, columns=['nome', 'id_contrato', 'id_fatura', 'valor'])
print("Arquivo em formato para encaminhar no drive")

# Obtenção da data atual para nomear o arquivo
data_atual = datetime.now()

# Salvamento do DataFrame em um arquivo Excel
df.to_excel(f'bot/backup_base/BOT REPORT (0{data_atual.day}.0{data_atual.month}.{data_atual.year}).xlsx', engine='openpyxl', header=True, index=False)
print("Colocada a data exata do arquivo e transformando para excel.")

# Autenticação com o Google Drive usando a conta de serviço
credentials = Credentials.from_service_account_file(r'/home/usuario/Área de trabalho/iaf_report/base_de_cobranca/projetos-pessoais-420412-e977e871ee92.json')
drive = build('drive', 'v3', credentials=credentials)
print("Credencial aceita")

# Identificação do último arquivo modificado na pasta atual
file_path = glob.glob("*")  # Busca por todos os arquivos na pasta atual
ultimo_arquivo = max(file_path, key=os.path.getatime)  # Seleção do arquivo mais recentemente acessado/modificado
print("Pegando ultimo arquivo")

# Preparação para upload do arquivo ao Google Drive
file_name = os.path.basename(ultimo_arquivo)  # Obtenção do nome do arquivo
folder_id = ''  # ID da pasta do Google Drive onde o arquivo será armazenado (deve ser especificado)
file_metadata = {'name': file_name, 'id': folder_id}  # Metadados do arquivo para o Google Drive
media = MediaFileUpload(ultimo_arquivo, resumable=True)  # Preparação do arquivo para upload

# Upload do arquivo para o Google Drive
file_drive = drive.files().create(body=file_metadata, media_body=media, fields='1fTLQ-v_NUPnXsXjZeTGs5RA0O7UCQZkH').execute()
print("Verificar se subiu pra produção")

# Concessão de permissão de leitura para qualquer pessoa
drive.permissions().create(fileId=file_drive['id'], body={'type': 'anyone', 'role': 'reader'}).execute()

# Créditos para Iago Longen Mendonça, desenvolvedor desse bot
print("Créditos para Iago Longen Mendonça, desenvolvedor desse bot")