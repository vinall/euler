import math
def largest_prime_factor(num):
    n1 = int(math.sqrt(num))
    max_prime = -1
    for i in range(3,int(math.sqrt(num))):
        while num % i == 0:
            max_prime = i
            num /= i;
            print("n = " , num , " mid = " , num )
    return max_prime


if __name__ == "__main__":
    print("largest prime factor = " , largest_prime_factor(600851475143))
