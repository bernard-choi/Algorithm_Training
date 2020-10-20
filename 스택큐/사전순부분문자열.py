def solution(s):
    stack = []
    for string in s:
        while stack and stack[-1] < string:
            stack.pop()

        stack.append(string)

    answer = ''.join(stack)

    return answer

if __name__ == '__main__':
  s = 'xyb'
  print(solution(s)) # yb
