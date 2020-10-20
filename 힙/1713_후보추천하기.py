a = int(input())
b = int(input())
input_list = list(map(int,input().split()))

hubo = dict()

for index,i in enumerate(input_list):

    if len(hubo) == a:

        if i not in hubo.keys():

            min_v = min([v for k,v in hubo.items()]) ## 가장 작은 value값을 찾는다.

            del_hubo = [k for k,v in hubo.items() if v == min_v] ## 가장 작은 value값에 해당하는 item을 찾는다.

            hubo.pop(del_hubo[0],None) ## 가장 오래된 key를 삭제



    hubo[i] = hubo.get(i,0) + 1

answer = [k for k,v in hubo.items()]
answer.sort()

for i in answer:
    print(i,end = ' ')
        
