# Algorithm_Training


알고리즘 개인공부(Python)

# Contents

#### 온라인 강의

- [백준 SW 역량테스트 준비](https://code.plus/course/32)

- [프로그래머스 파이썬을 무기로 코딩테스트 광탈을 면하자!](https://programmers.co.kr/learn/courses/9877)

- [프로그래머스 K사 코딩테스트 기출문제 Best 7](https://programmers.co.kr/learn/courses/10336)

- [프로그래머스 온라인 스터디](https://programmers.co.kr/learn/courses/10585)

#### 오프라인 스터디

- [백준 오프라인 스터디](https://www.acmicpc.net/)

----

## 디버깅 및 코딩 팁


#### 입출력

1. **입력 개수가 주어지지 않을때**- try except 처리로 해결
ex) [1793_타일링](https://www.acmicpc.net/problem/1793)
```Python
while True:
    try:
        n = int(input())
        print(d[n])
    except:
        break
```

2. **출력형식이 잘못되었습니다**. - 불필요한 공백 출력시 눈에 띄지는 않지만 에러가 출력됨.
ex) [17276_배열돌리기](https://www.acmicpc.net/problem/17276)
```python
for i in range(a):
    for j in range(a):
        print(matrix[i][j], end = ' ')
    if i != a-1:
        print() ## print(' ') 로 해서 "출력형식이 잘못되었슫니다" 계속 뜸
```

#### Pythonic 문제풀이

1. **sorted함수** - key, reverse를 활용

ex) [가장 큰 수](https://programmers.co.kr/learn/courses/30/lessons/42746)
```python
def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x: (x*4)[:4],reverse=True) ## 리스트 값을 4번 반복한후 4번째 자리까지 가장 큰수를 추출
    if numbers[0] == '0':
        answer = 0
    else:
        answer =  ''.join(numbers)
    return answer
```
