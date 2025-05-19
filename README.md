# TwitterBot

TwitterBot is a simple, automated Python bot for posting tweets with real-time stock market and forex updates. It leverages the popular [Tweepy](https://www.tweepy.org/) library and obtains financial data from public APIs, posting the latest information about selected companies and currency exchange rates directly to your Twitter account.

## Features

- **Automated Stock Updates:** Fetches live stock data for selected companies (primarily from the Nairobi Stock Exchange).
- **Automated Forex Updates:** Fetches and posts current currency exchange rates (including USD, EUR, JPY, and BTC to KES).
- **Batch Tweeting:** Gathers data, formats tweet content, and posts in batches to avoid spamming.
- **Easy Customization:** Add or remove companies to track using the `target_stocks.txt` file.
- **Deployment Ready:** Includes a `Procfile` for easy deployment on platforms like Heroku.

## Requirements

- Python 3.x
- [Tweepy](https://www.tweepy.org/)
- [requests](https://docs.python-requests.org/en/master/)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/nobrainghost/TwitterBot.git
    cd TwitterBot
    ```

2. **Set up Twitter API credentials:**
    - Obtain your credentials from the [Twitter Developer Portal](https://developer.twitter.com/).
    - Update the following variables in `Bot.py` and/or `ratesapi.py`:
      ```python
      consumer_key = "YOUR_CONSUMER_KEY"
      consumer_secret = "YOUR_CONSUMER_SECRET"
      access_token = "YOUR_ACCESS_TOKEN"
      access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
      ```

3. **Customize Tracked Companies:**
    - Add or remove company names in `target_stocks.txt` to control which stocks are tracked.

4. **Run the Bot:**

    - To post stock updates:
      ```bash
      python Bot.py
      ```

    - To post forex updates:
      ```bash
      python ratesapi.py
      ```

## File Structure

- `Bot.py` - Main bot script: fetches stock data and posts tweets.
- `ratesapi.py` - Fetches forex rates and posts related tweets.
- `target_stocks.txt` - List of company names to track.
- `tweets.txt` - Temporary file for storing generated tweets before posting.
- `forex_rates.txt` - Temporary file for storing forex tweets.
- `requirements.txt` - Python dependencies.
- `Procfile` - For deployment on Heroku or similar platforms.

## Example Usage

**Stock Update Tweet Example:**
```
Company: Safaricom
Stock Name: Safaricom
Volume: 1200000
Price: 22.50
Change: +0.20
```

**Forex Rate Tweet Example:**
```
Forex Rates 2025-05-19, 12:23:45
1 USD = 150.25 KES
1 EUR = 162.10 KES
1 JP YEN = 1.10 KES
1 BTC = 65000 USD
```

## Notes

- **API Keys:** The API keys in the code are placeholders. Use your own credentials.
- **Posting Interval:** The bot can be configured to wait between posts (see `time.sleep()` in the code).
- **Extensibility:** You can add more sources or change the format as needed.

## License

This project is open source and available under the MIT License.

---

*Feel free to contribute or open an issue for suggestions or bug reports!*
