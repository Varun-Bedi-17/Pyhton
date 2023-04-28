from itertools import count


def maze(n,i,j):
    if i == n-1 and j == n-1:
        return 1

    if i >= n or j >= n:
        return 0
    
    return maze(n,i+1,j) + maze(n,i,j+1)

print(maze(3,0,0))

