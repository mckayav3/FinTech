top_traders_per_month = {}
top_traders_per_month["January"] = "Susan"
top_traders_per_month["February"] = "Samuel"
#print (top_traders_per_month)

top_traders_per_month["February"] = "Harold"
#print(top_traders_per_month)
# Delete the key:value pair for February
del top_traders_per_month["February"]
print (top_traders_per_month)