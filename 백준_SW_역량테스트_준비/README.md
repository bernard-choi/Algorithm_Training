## Template 정리

#### BFS - 미로탐색

![](https://user-images.githubusercontent.com/36406676/89364836-5b548080-d70e-11ea-8371-e051a1ece7e5.png)

```python

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

```

#### DFS - 퇴사

![](https://user-images.githubusercontent.com/36406676/89367946-44fdf300-d715-11ea-8e3f-1d795763b36d.png)


```python

def do(cost_sum,index): ## 재귀로 구현

    if index >= len(time): ## 퇴사날 넘어가면 끝
        return


    if index + time[index] <= len(time):
        answer_list.append(cost_sum + cost[index])


    do(cost_sum + cost[index], index + time[index])  ## 상담하는 경우 cost랑 time추가
    do(cost_sum, index+1) ## 상담 안하고 넘어가는 경우


```

#### 백트래킹 - N과M(1)

![](https://user-images.githubusercontent.com/36406676/89366216-6a88fd80-d711-11ea-9d35-5c1c31d6830d.png)

```python
answer_list = [0] * b
check = [False] * (a+1) ## 체크라는 리스트를 만들어서 사용여부 확인

def go(n,m,index):
    if index == m: ## 길이 M 도달하면 출력
        for i in range(m):
            print(answer_list[i], end = ' ')
        print()
        return

    for i in range(1,n+1):
        if check[i] == True: ## 중복이 없으므로 해당 배열 check가 True면 다음으로 넘어감
            continue

        check[i] = True
        answer_list[index] = i
        go(n,m,index+1) ## 다음 인덱스로 넘어감
        check[i] = False ## 백트래킹

```
