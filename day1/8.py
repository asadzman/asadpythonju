data=range(1,51)
check=lambda x:x%5==0
d=[]
for i in data:
    if check(i):
        d.append(i)
print("multiples are:",d)