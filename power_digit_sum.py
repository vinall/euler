def multiply(begin_num,multiplier):
    remainder = 0
    result = ""
    i = len(begin_num)-1
    while i >= 0:
        temp = (int(begin_num[i])-int ('0'))*multiplier + remainder
        remainder = int(temp/10)
        result = str(int(temp%10)) + result
        i-=1
    if remainder != 0:
        result = str(remainder) + result
    return result

def power(e):
    result = "0"
    multiplier = 2
    begin_num = "1"
    print ([i for i in range(0,e)])
    for i in range(0,e):
        begin_num = multiply(begin_num,multiplier)
        #begin_num = result
    return begin_num

if __name__ == "__main__":
    res = [int(i) for i in power(1000)]
    print(sum(res))
    #print(multiply("9999",2))
