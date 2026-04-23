def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

is_prime_number = int(input("Enter a number to check if it's prime: "))
if is_prime(is_prime_number):
    print(f"{is_prime_number} is a prime number.")
else:
    print(f"{is_prime_number} is not a prime number.")