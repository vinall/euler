
result = 0
def prepare_result(m,n):
    result = []
    for i in range(0,m):
        new_row = []
        for j in range(0,n):
            new_row.append(0)
        result.append(new_row)
    return result

def lattice_path(i,j,row,col,count):
    global result
    if i==row and j==col:
        result += 1
    if i > row or j > col:
        return 0 

    if i <= row:
        lattice_path(i+1,j,row,col,result) 
    if j <= col:
        lattice_path(i,j+1,row,col,result)

def another_solution(m,n,result):
    print("m: " , m , " n: " ,n)
    if m == 0 or n == 0:
        return 1

    if result[m-1][n-1] != 0:
        print("result[m][n] = " ,result[m][n])
        return result[m-1][n-1]

    result[m-1][n-1] = another_solution(m - 1,n,result) + another_solution(m,n-1,result)
    print(result[m-1][n-1])
    return result[m-1][n-1]


if __name__ == "__main__":
    #lattice_path(0,0,3,3,0)
    xx = prepare_result(3,3)
    another_solution(3,3,xx)
    lattice_path(0,0,3,3,result)
    print(result)
    print(xx)
