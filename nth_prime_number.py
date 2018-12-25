
import math

def isprime(num):
    i = 2 

    while i <= int(math.sqrt(num)):
        if num % i == 0:
            return False
        i += 1
    return True

def nth_prime(nth):
    all_prime = 0
    i =2 
    while True:
        if isprime(i):
            all_prime += 1
            print("i = ",i," all_prime = ",all_prime)
            if all_prime == nth:
                break
        i += 1
    return i


    return all_prime
if __name__ == "__main__":
    print("nth prime is = ", nth_prime(10001))
