from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acesse as variáveis de ambiente carregadas
api_key = os.getenv("API_KEY")

# password.py
API_KEY = api_key