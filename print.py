from collections import deque


def solution(priorities, location):
    answer = 0

    myDeque = deque([(v, i) for i, v in enumerate(priorities)])

    print(myDeque)

    idx = 0
    while myDeque:
        idx += 1

        firstData = myDeque.popleft()

        if myDeque and max(myDeque)[0] > firstData[0]:
            print(myDeque)
            myDeque.append(firstData)
            print(myDeque)
        else:
            answer += 1

            if location == firstData[1]:
                break

    return answer

pri = [2, 1, 3, 2]
loc = 2
print(solution(pri, loc))
