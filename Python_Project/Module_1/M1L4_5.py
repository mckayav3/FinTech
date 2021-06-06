# Create a variable that identifies currency
issue_currency = "USD"

# Create a variable that identifies price
price = 30.0

# If the currency is USD, print the price. (Don't forget the colon.)
if issue_currency == "USD":
    print("The currency is $", price)

# If the currency is Euro, display the following statement.
elif issue_currency == "EUR":
    print("The currency is €", price)

# If the currency is anything other than USD or Euro, display the following.
else:
    print("The currency is not in USD or EUR.")
