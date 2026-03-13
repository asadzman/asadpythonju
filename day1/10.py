import time
INT_MAX=100000

a=int(input("enter the value a: "))
q=int(input("enter the value q: "))


start=int(time.time())
term = a
while term<INT_MAX:
    term=term*q

print("loop ends!")
end=int(time.time())

execution_time=end-start
print(f"execution time : {execution_time}")
