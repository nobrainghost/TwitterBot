import requests

# List of URLs to fetch data from
urls = [
    "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks/Absa%20Bank%20Kenya%20Plc",
    "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks/Safaricom",
    # Add more URLs here as needed
]

# Common headers for all requests
headers = {
    "X-RapidAPI-Key": "be623b818cmsh7d25d2e33a15fccp15ee38jsne2bef3c5c029",
    "X-RapidAPI-Host": "nairobi-stock-exchange-nse.p.rapidapi.com"
}

# Open tweets.txt file in append mode
with open('tweets.txt', 'a') as f:
    # Loop through each URL
    for url in urls:
        # Fetch data from the URL
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            if data:
                item = data[0]
                stock_name = item.get('name')
                volume = item.get('volume')
                price = item.get('price')
                change = item.get('change')

                # Format the tweet-like string
                tweet = f"Company: {stock_name}\nStock Name: {stock_name}\nVolume: {volume}\nPrice: {price}\nChange: {change}\n\n"

                # Write the tweet to tweets.txt file
                f.write(tweet)
                f.write('\n')
                print("Data updated for:", stock_name)
            else:
                print("No data found in response:", url)
        else:
            print("Failed to fetch data from:", url)
