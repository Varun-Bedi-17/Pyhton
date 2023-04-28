def issafe(arr, x, y, n):
    if x<n and y<n and arr[x][y] == 1:
        return True
    return False

def solve(arr, x, y, n, sol):
    if x==n-1 and y==n-1:
        sol[x][y]=1
        return True
    if x<0 or y<0:
        return False
    if issafe(arr, x, y, n):
        sol[x][y]=1
        return solve(arr,x,y+1,n,sol)
    y = y-1
    if issafe(arr,x+1,y,n):
        return solve(arr,x+1,y,n,sol)
    sol[x][y] = 0
    y = y-1
    return solve(arr,x+1,y,n,sol)

# maze = [[1,0,1,0,1], [1,1,1,1,1], [0,1,0,1,0], [1,0,0,1,1], [1,1,1,0,1]]
# soln = [[0 for i in range(5)] for j in range(5)]

maze2 = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
sol2 = [[0 for i in range(4)] for j in range(4)]

# maze3 = [[1, 0, 0, 0],[1, 0, 0, 0],[1, 1, 0, 0],[0, 1, 1, 1]] 
# sol3 = [[0 for i in range(4)] for j in range(4)]

if solve(maze2, 0, 0, 4, sol2):
    for i in range(4):
        for j in range(4):
            print(sol2[i][j], end=" ")
        print("")
else:
    print("Solution not exist")