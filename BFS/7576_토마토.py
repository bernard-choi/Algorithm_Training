from collections import deque

#a, b = map(int,input().split())
#matrix = []
#for i in range(b):
#    matrix.append(list(map(int,input().split())))


def solution(a,b,matrix):
    queue = deque()
    visited = [[False] * a for _ in range(b)]
    copy_mat = [[0] * a for _ in range(b)]
    start_point = []

    for i in range(b):
        for j in range(a):
            if matrix[i][j] == 1:
                start_point.append([i,j,0])
                visited[i][j] = True

            if matrix[i][j] == -1:
                visited[i][j] = True

    queue = deque(start_point)
    while queue:
        x, y, value = queue.popleft()
        DELTAS = [[0,1],[0,-1],[1,0],[-1,0]]
        for dx, dy in DELTAS:
            next_x = x + dx
            next_y = y + dy
            if (0 <= next_x < b) and (0 <= next_y < a) and not visited[next_x][next_y]:
                queue.append([next_x, next_y, value + 1])
                copy_mat[next_x][next_y] = value + 1
                visited[next_x][next_y] = True

    if sum(map(sum,visited)) != a*b:
        return(-1)
    else:
        return(max(map(max,copy_mat)))

if __name__ == '__main__':
    a = 6
    b = 4
    matrix = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,1]]
    print(solution(a,b,matrix)) ## 8
