from itertools import combinations
from copy import deepcopy
from collections import deque

N,M = map(int,input().split())
mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))

homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            homes.append([i,j])
        elif mat[i][j] == 2:
            chickens.append([i,j])

chicken_list = list(combinations(chickens,M))


candidates = []

for chickens in chicken_list: ## ([1,2],[2,2],[4,4])
    chicken_dist = []
    for home in homes:
        chicken_dist.append(min([abs(chicken[0]-home[0]) + abs(chicken[1]-home[1]) for chicken in chickens]))

    candidates.append(sum(chicken_dist))

print(min(candidates))
