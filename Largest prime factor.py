num = 600851475143
largest_prime_factor = 1
i = 2

while i <= num:
    if num % i == 0:
        largest_prime_factor = i
        num = num / i
    else:
        i += 1

print(largest_prime_factor)
