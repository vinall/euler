
import math
def sum_prime_numbers(num):
    prime_number = [ True for i in range(1,num+1)]
    num_sq = int(math.sqrt(num))
    for p in range(2,num_sq):
        if prime_number[p]:
            i = p*p
            while i < num:
                prime_number[i] = False
                i = i + p
    sum = 0
    print("-------------------")
    for j in range(2,num):
        if prime_number[j]:
            sum+=j
    return sum

if __name__ == "__main__":
    print("sum of prime = ",sum_prime_numbers(2000000))
