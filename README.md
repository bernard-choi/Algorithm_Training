# Algorithm_Training


알고리즘 개인공부(Python)

# Contents

#### 온라인 강의

- [백준 SW 역량테스트 준비](https://github.com/yunsikus/Algorithm_Training/tree/master/%EB%B0%B1%EC%A4%80_SW_%EC%97%AD%EB%9F%89%ED%85%8C%EC%8A%A4%ED%8A%B8_%EC%A4%80%EB%B9%84)

- [프로그래머스 파이썬을 무기로 코딩테스트 광탈을 면하자!](https://github.com/yunsikus/Algorithm_Training/tree/master/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4_%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84_%EB%AC%B4%EA%B8%B0%EB%A1%9C_%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8_%EA%B4%91%ED%83%88%EC%9D%84_%EB%A9%B4%ED%95%98%EC%9E%90)

- [프로그래머스 K사 코딩테스트 기출문제 Best 7](https://github.com/yunsikus/Algorithm_Training/tree/master/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4_K%EC%82%AC_%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8_%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C_Best7)

- [프로그래머스 온라인 스터디](https://github.com/yunsikus/Algorithm_Training/tree/master/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4_%EC%98%A8%EB%9D%BC%EC%9D%B8_%EC%8A%A4%ED%84%B0%EB%94%94)

#### 오프라인 스터디

- [백준 오프라인 스터디](https://github.com/yunsikus/Algorithm_Training/tree/master/%EB%B0%B1%EC%A4%80_%EC%98%A4%ED%94%84%EB%9D%BC%EC%9D%B8_%EC%8A%A4%ED%84%B0%EB%94%94)

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
3. **String 출력** - format을 쓰는게 깔끔

ex) [4796_캠핑](https://www.acmicpc.net/problem/4796)

```python
  for i in range(len(matrix)-1):
    answer = do(matrix[i])
    print("Case {}: {}".format(i+1,answer)) ## format

```

#### Pythonic 문제풀이

1. **sort 함수** - key, reverse를 활용

ex) [프로그래머스_가장 큰 수](https://programmers.co.kr/learn/courses/30/lessons/42746)
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

2. **2차원 리스트 90도 회전**

ex) [프로그래머스_자물쇠와 열쇠](https://programmers.co.kr/learn/courses/10336/lessons/64196)

```python
def rotate_a_matrix_by_90_degree(a):
  n = len(a) # 행 길이 계산
  m = len(a[0]) # 열 길이 계산

  result = [[0] * n for _ in range(m)] ## 결과 리스트
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]

  return result
```
3. **List comprehension**으로 복잡한 if문을 간략화함

ex) [프로그래머스_문자열압축](https://programmers.co.kr/learn/courses/10336/lessons/64194)

```python
def solutions(s):
    answer = len(s)
    for i in range(1,(len(s)//2)+1):
        new_s = ''
        count = 1
        prev = s[:i]
        for j in range(1,len(s)//i+1):
            if prev == s[i*j:i*j+i]:
                count += 1
            else:  
                new_s += str(count) + prev if count >= 2 else prev
                ## count가 2이상인 경우만 new_s에 추가.
                ## count가 1이면 숫자 빼고 string만 추가.
                count = 1   
                prev = s[i*j:i*j+i]

        new_s += str(count) + prev if count >= 2 else prev
        answer = min(answer,len(new_s))
```
4. **이진분류 함수 bisect** 를 sorted된 리스트에 적용

ex) [프로그래머스_문자열압축](https://programmers.co.kr/learn/courses/10336/lessons/64194)

```python
## bisect_left(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 위치를 반환
## bisect_right(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽일할 가장 오른쪽 위치를 반환

from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a,x)) ## index 2
print(bisect_right(a,x)) ## index 4
```
```python
## 특정 범위의 데이터 개수 구하기
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4)) ## 4가 몇개 있는지
print(count_by_range(a,-1,3)) ## -1과 3 사이의 숫자가 몇개 있는지
```

```python
## x보자 작은 데이터 중에서 가장 큰 값의 인덱스를 반환
def index_of_less_than_x(a,x):
    i = bisect_left(a,x)
    if i:
        return i-1
    return None

answer = index_of_less_than_x(a,3)
print(answer) ## index 1
```
```python
# x보다 큰 데이터 중에서, 가장 작은 값의 인덱스를 반환
def index_of_greater_than_x(a,x):
    i = bisect_right(a,x)
    if i:
        return i
    return None

answer = index_of_greater_than_x(a,3)
print(answer) ## index 6
```

```python
# x보다 크거나 같은 데이터 중에서, 가장 작은 값의 인덱스를 반환
def index_of_greater_equal_than_x(a,x):
    i = bisect_left(a,x)
    if i!= len(a):
        return i

    return None

answer = index_of_greater_than_x(a,3)
print(answer) ## index 6
  ```



#### 알고리즘

- 이진분류
