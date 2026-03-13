# 1. Get the target number of primes from the user
target_count = int(input("Enter number of primes you want to generate: "))

# primes = []
primes: list[int] = []
candidate = 2

while len(primes) < target_count:
    is_prime = True

    for p in primes:
        if candidate % p == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(candidate)

    candidate += 1

# print(f"The first {target_count} primes are: \n{primes}")
for i in primes:
    print(i)
