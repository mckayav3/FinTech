principle = 103208.56
interest_rates = [.103,.067,.099,.10]
total_interest = 0.0
for rate in interest_rates:
    interest = rate*principle
    total_interest= total_interest+interest
    print (f"your interest will be: ${interest: .2f}" )
print(f"The total interest is: ${total_interest: .2f}")