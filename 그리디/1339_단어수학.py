n = int(input())
input_list = []
for i in range(n):
    input_list.append(list(map(str,input())))

input_list2 = [] ## 자릿수 정보를 담기 위한 리스트. [[5, 'A'],[1, 'B'],[2, 'C'],[4, 'C'],[3, 'D'], [2, 'E'],[1, 'F'],[3, 'G']]

for i in range(len(input_list)):
    for index,j in enumerate(input_list[i]):
        input_list2.append([len(input_list[i])-index,j])

input_list2.sort(key = lambda x: x[1])

alph_list = list(set([y for x in input_list for y in x])) ## ['A', 'B', 'C', 'D', 'E', 'F', 'G'] input으로 받은 단어들의 unique값

cal_list = []
for i in alph_list:
    init = 0
    for j in input_list2:
        if j[1] == i:
            init += 10**(j[0]-1)
    cal_list.append(init) ## 가중치 계산

cal_list.sort(reverse=True) # 역순 ex) [10000, 1010, 100, 100, 10, 1, 1]

check_num = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # 가중치와 곱할 예정

print(sum([cal_list[x] * check_num[x] for x in range(len(cal_list))]))
