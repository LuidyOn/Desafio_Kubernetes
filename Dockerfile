# Imagem oficial e enxuta do Python
FROM python:3.12-slim

WORKDIR /app

# Instala apenas as dependências necessárias
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia somente o código da aplicação
COPY app/app.py .

# Porta em que o Flask escuta
EXPOSE 5000

# Inicia a aplicação (AMBIENTE e APP_SECRET são injetados em tempo de execução)
CMD ["python", "app.py"]
