
def longest_chain():
    max_count = 0
    max_number = 0
    existing_values = {1:1}
    for num in range(1000000,500000,-1):
        count = 0
        aux = num
        while num!=1:
            if num in existing_values:
                count+=existing_values[num]
                break
            if num % 2 == 1:
                num = 3*num+1
            else:
                num = num/2
            count+=1
        existing_values[aux]=count
        if max_count < count:
            max_count = count
            max_number = aux
    return max_count,max_number

if __name__ == "__main__":
    print(longest_chain())
