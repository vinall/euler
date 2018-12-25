

def sum_even_number_in_fibonacci(num):
    first = 1
    second = 1
    sum = 0
    #for i in range(2,num):
    while sum < num:
        next_num = first + second
        first = second
        second = next_num
        if next_num % 2 == 0:
            sum = sum + next_num
        print ("sum = " , sum)
    return sum
if __name__ == "__main__":
    print("sum of all even number in fibonacci " , sum_even_number_in_fibonacci(4000000))
