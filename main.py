import requests
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime, timedelta


from message import send_message

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY= os.getenv('STOCK_API_KEY')
NEWS_API_KEY= os.getenv('NEWS_API_KEY')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def yesterdays_fluctuation_percentage_in_stock(stock_name: str):
    today=datetime.now().date()- timedelta(days=1)
    yesterday = today - timedelta(days=1)
    previous_to_yesterday= yesterday  - timedelta(days=1)
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?'
    parameters={
        'apikey': STOCK_API_KEY,
        'function': 'TIME_SERIES_DAILY',
        'symbol': stock_name
    }
    response = requests.get(url, params=parameters)
    response.raise_for_status()

    data = response.json()['Time Series (Daily)']

    end_price=float(data[str(yesterday)]['4. close'])
    starting_price=float(data[str(previous_to_yesterday)]['1. open'])
    difference= end_price-starting_price
    percentage_decline=difference*100/starting_price
    return percentage_decline

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news_for_company(company_name: str, number_of_headlines:int=3):
    parameters={
        'apiKey': NEWS_API_KEY,
        'q': company_name,
        'from': datetime.now() - timedelta(days=3),
        'sortBy': 'relevancy',
        'page_size': number_of_headlines,
        'page': 1
    }
    response=requests.get('https://newsapi.org/v2/everything', params=parameters)
    response.raise_for_status()
    data = response.json()
    if data['totalResults']==0:
        return 'No breaking news'
    size=min(number_of_headlines, len(data['articles']))

    result = '\n\n'.join([f"{i}. Title: {article['title']} |Date_Published:{article['publishedAt']}  |:\nBrief: {article['content']} \n Refer: {article['url']}" for i, article in enumerate(data['articles'][:size])])

    return result

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_alert_for_stock(stock_name: str, company_name: str, alert_percentage_change: float=3):
    percentage_fluctuate= yesterdays_fluctuation_percentage_in_stock(stock_name)

    if abs(percentage_fluctuate)<alert_percentage_change:
        return 'no alert since alert_percentage: ' + str(alert_percentage_change)
    
    if percentage_fluctuate>0:
        message_fluctuation = f'{stock_name}: \u25B2 {percentage_fluctuate:.2f}%'
    else:
        message_fluctuation = f'{stock_name}: \u25BC {percentage_fluctuate:.2f}%'
 

    news=get_news_for_company(company_name=company_name)
    message_content=message_fluctuation+'\n'+news
    return send_message(mssg_body=message_content)

print(send_alert_for_stock(STOCK, COMPANY_NAME))
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

