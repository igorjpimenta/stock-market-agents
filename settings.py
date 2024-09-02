from decouple import Config, RepositoryEnv
from pathlib import Path
from pydantic.v1 import SecretStr


BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

DOTENV_PATH = str(BASE_DIR / '.env')
config = Config(RepositoryEnv(DOTENV_PATH))

OPENAI_API_KEY = SecretStr(str(config('OPENAI_API_KEY')))
