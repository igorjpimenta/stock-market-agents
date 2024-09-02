from langchain_openai import ChatOpenAI
from settings import OPENAI_API_KEY


gpt_3_5_turbo = ChatOpenAI(
    model='gpt-3.5-turbo',
    api_key=OPENAI_API_KEY
)
