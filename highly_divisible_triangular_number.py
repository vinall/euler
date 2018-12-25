
def highly_divisible_triangular_number():
    idx = 73920
    while True:
        range_of_number = sum(range(1,idx+1))
        count = 2
        j = 2
        while j*j < range_of_number:
            if range_of_number % j == 0:
                count += 1
            if count == 500:
                return range_of_number
            range_of_number /= j
            j+=1
        idx+=1

if __name__ == "__main__":
    print("number we are looking for is = ", highly_divisible_triangular_number())
