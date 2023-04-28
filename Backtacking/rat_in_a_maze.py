def issafe(maze, x, y, n):
    if x < n and y < n and maze[x][y] == 1:
        return True
    return False


def solve(maze, x, y, n, soln):
    if x == n-1 and y == n-1:
        soln[x][y] = 1
        return True
    if issafe(maze, x, y, n):
        soln[x][y]=1
        if solve(maze, x+1, y, n, soln):
            return True
        if solve(maze, x, y+1, n, soln):
            return True
        soln[x][y]=0     # Backtack
        return False
    return False

maze = [[1,0,1,0,1], [1,1,1,1,1], [0,1,0,1,0], [1,0,0,1,1], [1,1,1,0,1]]
soln = [[0 for i in range(5)] for j in range(5)]
# maze2 = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
# sol2 = [[0 for i in range(4)] for j in range(4)]

if solve(maze, 0, 0, 5, soln):
    for i in range(5):
        for j in range(5):
            print(soln[i][j], end=" ")
        print("")
else:
    print("Solution not exist")

