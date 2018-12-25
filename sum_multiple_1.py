
def sum_of_multiple(num):
    sum = 0
    for i in range(1,1000):
        if i%3 == 0 or i%5 ==0:
            sum = sum + i
    return sum

if __name__ == "__main__":
    sum = sum_of_multiple(1000)
    print("sum of all multiples below 1000 = " , sum)
