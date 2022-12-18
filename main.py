import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "IQ0QK8LMIE3PYFQ3"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "0e0b833dc89742fa9ca1c1fea775035d"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5%  between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
                "function":"TIME_SERIES_DAILY_ADJUSTED",
                "symbol":STOCK_NAME,
                "from": 2022-12-17,
                "apikey":"IQ0QK8LMIE3PYFQ3"
}
news_parameters = {
                "q":"tesla",
                "apiKey":NEWS_API_KEY
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
time_series_data = stock_data["Time Series (Daily)"]

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
closing_stock_price_data = [time_series_data[date]["4. close"] for(date, value) in time_series_data.items()]
yesterday_closing_stock_price_data = float(closing_stock_price_data[0])


#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_stock_price_data = float(closing_stock_price_data[1])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
closing_stock_price_data_difference = round(abs(yesterday_closing_stock_price_data - day_before_yesterday_closing_stock_price_data),2)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_price_difference = round((closing_stock_price_data_difference/day_before_yesterday_closing_stock_price_data) * 100,4)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_price_difference >= 5:
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    articles_data = news_data["articles"][:3]
    print(articles_data)
    change_difference = round((yesterday_closing_stock_price_data - day_before_yesterday_closing_stock_price_data),2)
    if change_difference > 0:
        change_symbol = f"🔺{percentage_price_difference}"
    else:
        change_symbol = f"🔻{percentage_price_difference}"
    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    article_list = [
                    {
                    STOCK_NAME: change_symbol,"headline": val["title"],"Brief": val["description"]} for val in articles_data
                    ]
    print(article_list)
else:
    print("boom boom")
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 



#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

