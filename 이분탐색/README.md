1. **Template**
```python
def binary_search(data,start,end,target):
  while start <= end:
    mid = (start + end) // 2

    if data[mid] == target:
      return mid

    elif data[mid] < target:
      start = mid + 1

    else:
      end = mid - 1

  return None

if result == None:
  print("탐색 실패")
else:
  print('탐색 성공: 인덱스 ', result)

# 리스트 [1,3,5,7,9] 에서 값이 7인 원소 탐색하기
data = [1,3,5,7,9]
result = binary_search(data, 0, len(data) - 1, 7)

```


2. **이진분류 모듈 bisect** 를 sorted된 리스트에 적용

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
