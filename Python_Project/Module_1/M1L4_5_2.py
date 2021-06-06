issue_currency = "USD"
price = 30.0

# Check if price is not negative (greater than equal to 0)
if price >= 0:
    # If price is not negative and currency is `USD` (Dollar).
    if issue_currency == "USD":
        print("The currency is $", price)
    # If price is not negative and currency is `EUR` (Euro).
    elif issue_currency == "EUR":
        print("The currency is €", price)
    # If anything other than the above.
    else:
        print("The currency is not in USD or EUR.")
else:
    # If price is negative.
    print("Error, the price listed is a negative number")