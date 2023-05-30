# Stock News Alert

This Python script fetches stock price data from the Alpha Vantage API and uses Twilio to send news alerts to your phone number when the stock price of a specified company increases or decreases by more than 1%. It utilizes the News API to retrieve relevant news articles related to the specified company.

## Prerequisites

Before running this script, ensure you have the following:

- Python 3.x installed
- `requests` library installed (`pip install requests`)
- `twilio` library installed (`pip install twilio`)

## Setup

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before running the script, you need to provide your own API keys and phone numbers in the `config.py` file.

```python
STOCK_NAME = "TSLA"  # The stock symbol you want to monitor (e.g., TSLA for Tesla)
COMPANY_NAME = "Tesla Inc"  # The name of the company you want to monitor
STOCK_API_KEY = "YOUR_OWN_API_KEY_FROM_ALPHAVANTAGE"  # Your API key from Alpha Vantage
NEWS_API_KEY = "YOUR_OWN_API_KEY_FROM_NEWSAPI"  # Your API key from News API
TWILIO_SID = "YOUR_TWILIO_ACCOUNT_SID"  # Your Twilio account SID
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"  # Your Twilio auth token
VIRTUAL_TWILIO_NUMBER = "YOUR_VIRTUAL_TWILIO_NUMBER"  # Your virtual Twilio number
VERIFIED_NUMBER = "YOUR_OWN_PHONE_NUMBER_VERIFIED_WITH_TWILIO"  # Your own phone number verified with Twilio
```

Replace the placeholder values with your actual API keys and phone numbers.

## Usage

Run the following command to execute the script:

```
python stock_news_alert.py
```

The script performs the following steps:

1. Retrieves the closing stock prices for the past two days using the Alpha Vantage API.
2. Calculates the percentage difference between yesterday's closing price and the day before yesterday's closing price.
3. If the difference is greater than 1%, it retrieves the first three news articles related to the specified company from the News API.
4. Formats the articles' headlines and descriptions.
5. Sends each article as a separate message to your phone number using Twilio.

You will receive news alerts on your phone whenever the stock price of the specified company changes significantly.

## Use Case: Monitoring Stock News

This script is useful for individuals who want to stay updated with the stock market and receive news alerts regarding specific companies. Here's an example use case scenario:

John is an investor who closely follows the stock market and wants to monitor the stock price of Tesla Inc. He wants to receive news alerts on his phone whenever the stock price of Tesla increases or decreases significantly. Instead of manually checking the stock price and news articles, John decides to automate this process using the Stock News Alert script.

By configuring the script with his API keys, phone number, and desired stock symbol (TSLA) and company name (Tesla Inc), John can run the script and receive timely alerts whenever there is a notable change in Tesla's stock price. The script retrieves the closing prices for the past two days and calculates the percentage difference. If the difference exceeds 1%, it fetches the first three news articles related to Tesla from the News API. John receives separate messages with the article titles and descriptions on his phone via Twilio.

With this automated system in place, John can stay informed about Tesla's stock price movements and receive relevant news articles without the need for

 manual monitoring. This enables him to make well-informed investment decisions and take appropriate actions based on the latest information.

## Customization

Feel free to customize the script as per your requirements. You can modify the stock symbol, company name, or the threshold percentage for triggering news alerts by editing the configuration in the `config.py` file.

You can also modify the number of news articles to fetch or customize the message format sent via Twilio by modifying the script accordingly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
