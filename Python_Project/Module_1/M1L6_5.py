table_data = [
    ["Ticker", "Open", "Close"],
    ["AAPL", 363.25, 363.4],
    ["AMZN", 2756.0, 2757.99],
    ["GOOG", 1409.1, 1408.2]
]

amazon_data = table_data[2]
amazon_opening_price=amazon_data[1]
google_data= table_data[3]

amazon_opening_price= table_data[2][1]
apple_closing_price= table_data[1][2]


print(amazon_data)
print (amazon_opening_price)
print(google_data)
print(apple_closing_price)
print ("Closing price for Apple",apple_closing_price)
print("-----------------------------------------------")
for row in table_data:
    ticker = row [0],[2]
    print(ticker)
print("-----------------------------------------------")
for item in table_data:
    ticker = item["Ticker"]
    print(ticker)