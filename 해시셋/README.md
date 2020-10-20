## Hash

Python은 Dictionary라는 형태로 해시 자료구조를 제공.
Dictionary는 'dict'클래스로 구현되어있음

#### 언제사용?

빠른 접근 탐색이 필요할 때. 딕셔너리는 함수 대부분의 시간 복잡도가 O(1)로 아주 빠른 자료구조.
집계할 떄. 특히 Collections모듈의 Counter클래스는 이때 아주 유용하게 쓰임.

#### Get

```Python
# get 메소드를 이용해 원소 가져오기
# 딕셔너리에 해당 key가 없을때 Key Error를 내는 대신 특정한 값을 가져온다.

my_dict = {'김철수': 300, 'Anna': 180}
my_dict.get("홍길동", 0) # 0
```

#### Items

```Python
## key value 쌍을 extract - Items사용
my_dict = {'김철수': 300, 'Anna': 180}
my_dict.items() # dict_items([('김철수', 300, 'Anna': 180)])
```
#### Counter

```Python
import collections
my_list = ["박수진", "박수진", "홍길동", "김철수", "김철수"]
my_counter = collections.Counter(my_list)

my_counter # Counter({'김철수': 2, '박수진': 2, '홍길동': 1})
```


#### 완주하지 못한 선수
``` Python
## 프로그래머스 - 완주하지 못한 선수

def solution(participant,completion):
    d = {}
    for x in participant:
        d[x] = d.get(x,0) + 1

    for x in completion:
        d[x] -= 1

    dnf = [k for k, v in d.items() if v > 0] ## key를 담는다.
    answer = dnf[0]

    return answer

```

#### 나머지 한점

```python
from collections import Counter
def solution(v):
    counter1 = Counter([x[0] for x in v]) # X, Y 좌표로 뽑힌 값의 개수
    counter2 = Counter([x[1] for x in v])
    x = counter1.most_common()[-1][0] # 개수가 적은 값을 추출
    y = counter2.most_common()[-1][0]
    answer = [x, y] # , 뒤에 띄어쓰기 했습니다.

    return answer
```

## Set

Python은 set이라는 형태로 집합 자료구조를 제공.

#### 언제사용?

다루는 데이터의 삽입/삭세/서치가 자주 일어날때. 리스트의 원소 탐색 시간복잡도는 O(N), 반면 집합은 O(1)이 소요됨.


#### add

```python
my_set = set()
my_set.add(3)
my_set.add("데미")

my_set # {3,'데미'}
```

#### remove

```python
my_set = set([1,2,3,4,5])
my_set.remove(1)

my_set # {2,3,4,5}
```

#### 집합

```python
# 합집합: | 를 사용
set1 = set([1,2,3,4,5])
set2 = set([4,5,6,7,8])

set1 | set2 # {1, 2, 3, 4, 5, 6, 7, 8}

# 차집합: - 를 사용

set1 = set([1,2,3,4,5])
set2 = set([4,5,6,7,8])

set1 - set2 # {1, 2, 3}

# 교집합: & 를 사용

set1 = set([1,2,3,4,5])
set2 = set([4,5,6,7,8])

set1 & set2 # {4, 5}
```
#### 운송트럭

```python
from collections import Counter
def solution(board, nums):
    answer = 0
    bingo_coordinates = set(nums)
    N = len(board)

    bingo_col = [0 for _ in range(N)]
    bingo_row = [0 for _ in range(N)]
    bingo_cross1 = 0
    bingo_cross2 = 0

    for row in range(N):
        for col in range(N):
            if board[row][col] in bingo_coordinates: # 검색 시 O(1)의 시간복잡도
                bingo_col[col] += 1
                bingo_row[row] += 1

                if row == col:
                    bingo_cross1 += 1

                if row + col == N-1:
                    bingo_cross2 += 1

    col_answer = Counter(bingo_col)[N]
    row_answer = Counter(bingo_row)[N]

    answer += col_answer
    answer += row_answer
    answer += bingo_cross1 == N
    answer += bingo_cross2 == N


    return answer

```
