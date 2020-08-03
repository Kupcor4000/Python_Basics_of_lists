import time

quote = "There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all"
quote2 =["All","art","is","quite","useless"]
sentence = quote.split()
sentence2 = " ".join(quote2)

for word in sentence:
    print(word)
    time.sleep(0.1)
print("\n"+sentence2)