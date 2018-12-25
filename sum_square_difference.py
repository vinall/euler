
def sum_square_difference(num):
    sq_sum = num*(num+1)*(2*num+1)
    sq_sum = sq_sum/6
    lin_sum = (num*(num+1))/2
    print("square num = " , sq_sum , " natural sum = ", lin_sum)
    print("difference = ",sq_sum - (lin_sum*lin_sum))

if __name__ == "__main__":
    sum_square_difference(100)
