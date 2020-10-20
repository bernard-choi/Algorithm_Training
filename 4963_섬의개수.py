import sys
sys.setrecursionlimit(1500) ## pypy3가 recursion 갚이가 더 깊음. python3가 아닌 pypy3로 제출해야 통과됨

def dfs(island,x,y):
    if x >= row or x < 0 or y >= col or y < 0:
        return

    if island[x][y] == 0:
        return

    island[x][y] = 0

    dfs(island,x+1,y)
    dfs(island,x-1,y)
    dfs(island,x+1,y+1)
    dfs(island,x+1,y-1)
    dfs(island,x-1,y+1)
    dfs(island,x-1,y-1)
    dfs(island,x,y-1)
    dfs(island,x,y+1)

def do(island,row,col):
    count = 0
    for i in range(row):
        for j in range(col):
            if island[i][j] == 1:
                dfs(island,i,j)
                count += 1

    print(count)

while True:
    col, row = map(int,input().split())
    island = []
    for i in range(row):
        island.append(list(map(int,input().split())))


    if row == 0 and col == 0:
        break

    do(island,row,col)
