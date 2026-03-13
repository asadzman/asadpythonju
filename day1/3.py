from itertools import compress
data=range(1,21)
even=[]
odd=[]
for p in data:
    if p%2==0:
        even.append(1)
        odd.append(0)
    else:
        even.append(0)
        odd.append(1)
eve=list(compress(data,even))
odd=list(compress(data,odd))
print("even numbers:",eve)
print("odd numbers:",odd)