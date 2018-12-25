
def factorial(num):
    if num == 2:
        return 2
    return num*factorial(num-1)
def function(m,n):
    up = factorial(m+n)
    down1 = factorial(m)
    down2 = factorial(n)
    return up/(down1*down2)



if __name__ == "__main__":
    print(function(20,20))
