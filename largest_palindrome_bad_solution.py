
def ispalindrome(num):
    i = 0
    j = len(str(num))-1
    snum = str(num)
    while i<j:
        if snum[i] != snum[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def some_function():
    max_num = -1
    for i in range(999,99,-1):
        for j in range(999,i,-1):
            num = i*j
            if ispalindrome(num) and max_num < num: 
                max_num = num
    print("max_num = " , max_num)
if __name__ == "__main__":
    some_function()
