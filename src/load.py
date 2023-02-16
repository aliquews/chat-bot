import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


OPENAI_API = os.environ.get("OPENAI")
TELEGRAM_API = os.environ.get("TELEGRAM")

print(type(OPENAI_API))