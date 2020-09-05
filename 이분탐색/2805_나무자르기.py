a,b = map(int,input().split())
input_list = list(map(int,input().split()))

input_list.sort()

def binary_search(data,start,end,M):
    answer = 0
    while start <= end: ## start랑 end가 같아지면
        mid = (start+end)//2

        tree_get = sum([x-mid for x in data if x-mid >= 0])



        if tree_get >= M:
            answer = mid
            start = mid + 1

        else:
            end = mid - 1

    return answer


result = binary_search(input_list,0,input_list[-1],b)
print(result)
