scores = input("Entry scores: ").split(" ")
numofmember =0
for i in scores:
    scores[numofmember]=int(i)
    numofmember+=1

x=scores[0]

for score in scores:
    
    if(score>=x):
        x=score

print(f"Max score = {x}")