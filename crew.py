from crewai import Crew, Process
from models import gpt_3_5_turbo
from agents import stock_price_analyst, news_analyst, stock_writter_analyst
from tasks import get_stock_price, get_news, write_analyses


crew = Crew(
    agents=[stock_price_analyst, news_analyst, stock_writter_analyst],
    tasks=[get_stock_price, get_news, write_analyses],
    verbose=True,
    full_output=True,
    process=Process.hierarchical,
    share_crew=False,
    manager_llm=gpt_3_5_turbo,
    max_iter=15
)
