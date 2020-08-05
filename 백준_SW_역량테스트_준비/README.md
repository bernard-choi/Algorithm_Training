## BFS

#### 2718_미로탐색

![](https://user-images.githubusercontent.com/36406676/89364836-5b548080-d70e-11ea-8371-e051a1ece7e5.png)

```python
a,b = map(int,input().split())
dist = [[0]*b for _ in range(a)] ## 똑같은 크기의 matrix를 복사.
matrix = []
for i in range(a):
    matrix.append(list(map(int,input())))

dx = [1,-1,0,0] ## 이동방향 down, up, right, left 4가지
dy = [0,0,1,-1]

def bfs(x,y):
    answer = 0
    visited = []   ## 이전에 방문한 칸을 memo
    queue = []     ## queue를 활용. 다음 방문 가능한 칸을 insert
    dist[0][0] = 1 ## dist에 해당 거리들을 표시 0->1->2...
    queue.append([x,y])
    visited.append([x,y])
    while queue:
        point = queue.pop(0)
        for i in range(4):
            nx,ny = point[0]+ dx[i],point[1] + dy[i]

            if (0<= nx < a) and (0 <= ny < b) and (matrix[nx][ny] != 0): ## 칸을 벗어나거나 장애물이 있는 칸은 제외
                if ([nx,ny] not in visited): ## 방문한 적이 있는 칸 제외
                    queue.append([nx,ny]) ## 방문 가능한 칸을 queue에 insert
                    visited.append([nx,ny]) ## 방문했다고 표시
                    dist[nx][ny] = dist[point[0]][point[1]] + 1 ## dist에 움직인 거리 표시

    print(dist[a-1][b-1])


bfs(0,0)
```
