import  os
def sum_numbers(line,sums):
    remainder = 0 
    temp = ""
    idx = len(line)-1
    jdx = len(sums)-1
    while idx  >=0 or jdx >=0:
        aux = (int(line[idx]) - int('0') if idx>=0 else 0) + ( int(sums[jdx]) - int('0') if jdx >= 0  else 0 ) + remainder
        remainder = int((aux )/10)
        actual = (aux) % 10
        temp = str(actual) + temp
        idx -= 1
        jdx -= 1
    if remainder != 0:
        temp = str(remainder) + temp 
    """if remainder != 0:
        while idx>=0 and remainder != 0:
           aux = (int(line[idx]) - int('0')) + remainder
           remainder = (aux)/10
           actual = a%10
           temp = str(actual) + temp
           idx-=1"""
    print(line,"+",sums," Result:= ",temp)
    return temp


def large_sum():
    path = os.getcwd() + "/" + "large_number.txt"
    sums = "0"
    with open(path,"r") as f:
        for line in f:
            sums = sum_numbers(line[:-1],sums)
    print("Final sum = " , sums)
if __name__ == "__main__":
    large_sum()
