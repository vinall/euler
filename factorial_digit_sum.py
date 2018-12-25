
def factorial(num):
    if num <= 2:
        return num
    return num * factorial(num-1)

if __name__ == "__main__":
    d = [int(i) for i in str(factorial(100))]
    print(d)
    print("sum = ", sum(d))
