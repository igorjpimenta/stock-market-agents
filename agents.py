from crewai import Agent
from models import gpt_3_5_turbo
from tools import stock_prices_fetching_tool, news_searching_tool

stock_price_analyst = Agent(
    role='Senior Stock Price Analyst',
    goal='Find the {ticker} stock price and analyses trends',
    backstory="You're a highly experienced in analysing the price of an \
        specific stock and make predictions about its future price.",
    verbose=True,
    llm=gpt_3_5_turbo,
    max_iter=5,
    memory=True,
    allow_delegation=False,
    tools=[stock_prices_fetching_tool]
)

news_analyst = Agent(
    role='Stock News Analyst',
    goal='Create a short summary of the market news related to the stock \
        {ticker} company.\
        Specify the current trend - up down or sideways eith the news context.\
        For each requested stock asset, specify a number between 0 and 100, \
        where 0 is extreme fear and 100 is extreme greed',
    backstory="You're a highly experienced in analysing the market trend \
        and news and have tracked assets for more then 10 years.\
        You're also master level analyst in the traditional markets and have \
        deep understanding of human psychology.\
        You understand news, their titles and information, but you look at a \
        health dose of skeptcism. You consider also the source of the news \
        articles.",
    verbose=True,
    llm=gpt_3_5_turbo,
    max_iter=10,
    memory=True,
    allow_delegation=False,
    tools=[news_searching_tool]
)

stock_writter_analyst = Agent(
    role='Senior Stock Analyst Writter',
    goal='Analyse the trends price and news and write a insightful compeling \
        and informative 3 paragraph long newsletter based on the stock report \
        and price trend.',
    backstory="You're a widely accepted as best stock analyst in the market.\
        You understand complex concepts andd create compeling stories and \
        narratives that resonate with wider audiences.\
        You understand macro factors and combine multiple theories - eg.: \
        cycle theory and fundamental analyses.\
        You're able to hold multiple opinions when analysing anything.",
    verbose=True,
    llm=gpt_3_5_turbo,
    max_iter=15,
    memory=True,
    allow_delegation=True
)
