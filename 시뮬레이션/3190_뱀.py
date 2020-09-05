from collections import deque

N = int(input())
K = int(input())
K_mat = []
for i in range(K):
    K_mat.append(list(map(int,input().split())))
L = int(input())
L_mat = []
for i in range(L):
    L_mat.append(list(input().split()))

dx = [0,0,-1,1] # right, left, up, down
dy = [1,-1,0,0]

start = [0,0]
dir_init = 'right'

K_mat = [[x[0]-1,x[1]-1] for x in K_mat]
visited = [[False]*N for _ in range(N)]

for index in K_mat:
    visited[index[0]][index[1]] = True # 사과 한번 먹으면 끝

def next_point(x,y,direction):
    if direction == 'right':
        return x + dx[0], y + dy[0], 'right'
    elif direction == 'left':
        return x + dx[1], y + dy[1], 'left'
    elif direction == 'up':
        return x + dx[2], y + dy[2], 'up'
    elif direction == 'down':
        return x + dx[3], y + dy[3], 'down'



queue1 = deque()
queue2 = deque()
queue1.append(start)
queue2.append('right')

answer = 0

while queue1:
    if L_mat and int(L_mat[0][0]) == answer:
        if queue2[-1] == 'right' and L_mat[0][1] == 'D': # down
            queue2[-1] = 'down'
        elif queue2[-1] == 'right' and L_mat[0][1] == 'L': # up
            queue2[-1] = 'up'
        elif queue2[-1] == 'left' and L_mat[0][1] == 'D': # up
            queue2[-1] = 'up'
        elif queue2[-1] == 'left' and L_mat[0][1] == 'L': # down
            queue2[-1] = 'down'
        elif queue2[-1] == 'up' and L_mat[0][1] == 'D': # right
            queue2[-1] = 'right'
        elif queue2[-1] == 'up' and L_mat[0][1] == 'L': # left
            queue2[-1] = 'left'
        elif queue2[-1] == 'down' and L_mat[0][1] == 'D': # left
            queue2[-1] = 'left'
        elif queue2[-1] == 'down' and L_mat[0][1] == 'L': # right
            queue2[-1] = 'right'

        L_mat.pop(0)



    new_x, new_y, direction = next_point(queue1[-1][0],queue1[-1][1],queue2[-1])
    answer += 1


    if ([new_x,new_y] in queue1) or (new_x < 0) or (new_x >= N) or (new_y < 0) or (new_y >= N):
        break

    queue1.append([new_x, new_y])
    queue2.append(direction)

    if visited[new_x][new_y] == False:
        queue1.popleft()
        queue2.popleft()

    else:
        visited[new_x][new_y] = False

print(answer)
