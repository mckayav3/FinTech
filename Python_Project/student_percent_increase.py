# Percent Increase Bonus Activity
# Formulas
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100
# Create float variable for original_price
original_price=71.50
# Create float variable for current_price
current_price=100.00
# Calculate difference between current_price and original_price
difference = current_price - original_price #28.5
# Calculate percent_increase
percent_increase = difference /original_price * 100
# Print original_price
print(f"Apple's original stock price was ${original_price}")
# Print current_price
print(f"Apples current stock price is ${current_price}")
# Print percent_increase
print (f"Apple's increase in price by: {percent_increase:.2f} %")
