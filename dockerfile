# Usar uma imagem oficial do Python como base
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto para o diretório de trabalho
COPY . .

# Expor a porta em que o FastAPI vai rodar
EXPOSE 8000

# Comando para rodar a aplicação usando o Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
