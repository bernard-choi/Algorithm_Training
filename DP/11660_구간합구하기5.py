n = int(input())
input_list = list(map(int,input().split()))
d = [1] * n
d[0]=1

for i in range(1,n): ## 기준은 i
#     print(i)
    max_value = 1
    for j in range(0,i):
#         print(j)
        if input_list[j] < input_list[i]:
            temp = d[j] + 1
            if temp > max_value:
                max_value = temp

    d[i] = max_value

print(max(d))
