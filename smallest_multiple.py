
def smallest_multiple():
    rg = [i for i in range(1,21)]
    for i in range(2,20):
        value = rg[i-1]
        for j in range(i,20):
            if rg[j] % value == 0:
                rg[j] = rg[j]/value
    result = 1
    print(rg)
    for i in rg:
        result = result*i
    print("Result = ",result)

if __name__ == "__main__":
    smallest_multiple()
