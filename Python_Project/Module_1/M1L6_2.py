"""words= ["cool!","awesome!","why am I shouting"]

for word in words:
    print(word.upper())
"""

words=["cool!","awesome!","why am I shouting?"]
for word in words:
    print ("Orig Word:", word)
    print ("Uppercase Word:", word.upper())
print ("Titlecase Word:", word.title())
print("I'm outside of the loop, so I only print conce after all the words have been selected!")
