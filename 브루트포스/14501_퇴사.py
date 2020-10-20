a = int(input())
time = []
cost = []
for i in range(a):
    a,b = map(int,input().split())
    time.append(a)
    cost.append(b)

answer_list = []

def do(cost_sum,index):

    if index >= len(time) :
        return


    if index + time[index] <= len(time):
        answer_list.append(cost_sum + cost[index])


    do(cost_sum + cost[index], index + time[index])
    do(cost_sum, index+1)

do(0,0)

if len(answer_list)==0:
    print(0)
else:
    print(max(answer_list)) 
