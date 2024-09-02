from crewai import Task
from agents import stock_price_analyst, news_analyst, stock_writter_analyst
from datetime import datetime


date = datetime.now().strftime('%Y-%m-%d')

get_stock_price = Task(
    description='Analyse the stock {ticker} price history and create a trend \
        analyses of up, down and sideways',
    expected_output="Specify the current trend stock price - up down or \
        sideways. Eg.: stock='AAPL, price UP",
    agent=stock_price_analyst
)

get_news = Task(
    description=f'Take the stock and always include BTC to it (if not \
        requested). \
        Use the search tool to search each individually.\
        The current date is {date}.\
        Compose the results into a helpful report.',
    expected_output="A summary of the overall market and one sentence summary \
        for each requested asset.\
        Include a fear/gree score for each asset based on the news.\
        Use the following format:\
        <STOCK ASSET>\
        <SUMMARY BASED ON NEWS>\
        <TREND PREDICTION>\
        <FEAR/GREED SCORE>",
    agent=news_analyst
)

write_analyses = Task(
    description='Use the stock price trend and the stock news report to \
        create an analyses and write the newsletter about the {ticker} \
        company that is brief and highlights the most important points.\
        Focus on the stock price trend, news and fear/greed score.\
        What are the near future considerations?\
        Include de previous analyses of the stock trend and news summary.',
    expected_output="An eloquent 3 paragraphs newsletter formated as markdown \
        in an easy readable manner.\
        It should contain:\
        - 3 bullets executive summary\
        - Introduction - set the overall picture and spike up the interest\
        - Main part provides the meat of the analyses including the news \
        summary and fear/greed scores\
        - summary - key facts and concrete future trends prediction - up,\
        down and sideways",
    agent=stock_writter_analyst,
    context=[get_stock_price, get_news]
)
