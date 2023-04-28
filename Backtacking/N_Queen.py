def issafe(arr, x, y, n):
    for i in range(x):
        if arr[i][y] == 1:
            return False
    
    row = x
    col = y
    while row>=0 and col>=0:
        if arr[row][col]==1:
            return False
        row-=1
        col-=1

    row = x
    col = y
    while x>=0 and y<n:
        if arr[row][col]==1:
            return False
        x-=1
        y+=1

    return True

def Nqueen(arr, row, n):
    if row >=n:
        return True

    for col in range(n):
        if issafe(arr,row,col,n):
            arr[row][col] = 1
            if Nqueen(arr,row+1,n):
                return True
        
            arr[row][col] = 0
    
    return False


board = [[0 for i in range(5)] for j in range(5)]
if Nqueen(board,0,5):
    for i in range(5):
        for j in range(5):
            print(board[i][j], end=" ")
        print("")

else:
    print("Not Found")