from collections import Counter
def solution(v):
    counter1 = Counter([x[0] for x in v]) # X, Y 좌표로 뽑힌 값의 개수
    counter2 = Counter([x[1] for x in v])
    x = counter1.most_common()[-1][0] # 개수가 적은 값을 추출
    y = counter2.most_common()[-1][0]
    answer = [x, y] # , 뒤에 띄어쓰기 했습니다.

    return answer

if __name__ == '__main__':
    v = [[1, 4], [3, 4], [3, 10]]
    print(solution(v)) # [1, 10]
