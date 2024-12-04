import  requests
from newsapi import NewsApiClient
from twilio.rest import Client



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_API = "0TAZ2PFWNTK92YIF"
NEWS_API_KEY ='c283fa7106144d89923d23bdd5d4d9ea'
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
daily = "TIME_SERIES_DAILY"
account_sid ="ACfdea6e443f848569cffb5c2b401dd55d"
auth_token = "faf5e2dd505913a03fd246280ca958c1"



#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params ={
    "function": "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" :MY_API
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(response.json())
data = response.json()["Time Series {Daily"]
print(data)
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = float(yesterday_closing_price) - float( day_before_yesterday_closing_price)
up_down =None
if diff >0:
    up_down ="🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((diff/float(yesterday_closing_price))*100)
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 3:
    print("Get News")


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 1:
    news_params ={
        "apiKey": NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    new_response =requests.get(NEWS_ENDPOINT, params = news_params)
    articles = new_response.json()["articles"]
    print(articles)


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles =[f"{STOCK_NAME}:{up_down}{diff_percent}%\nHeadline: {articles['title']}. \nBriel:{articles['description']}" for articles in three_articles]

#TODO 9. - Send each article as a separate message via Twilio.

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+18447192354",
            to="+19409770736",
        )


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

