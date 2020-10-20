from collections import deque
def solution(max_weight, specs, names):
    my_dict = {}
    for spec in specs:
        my_dict[spec[0]] = int(spec[1])

    queue = deque(names)
    answer = 1

    init = 0
    while queue:

        if init == max_weight:
            answer += 1
            init = 0

        name = queue.popleft()
        init += my_dict[name]

        if init > max_weight:
            answer += 1
            init = my_dict[name]

    return answer
