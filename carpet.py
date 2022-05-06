def solution(brown, yellow):
    ab = brown + yellow

    for b in range(1, ab + 1):
        if (ab/b) % 1 == 0:
            a = int(ab / b)

            if a >= b:
                if (a-2)*(b-2) == yellow:
                    return [a, b]


br =  24
yel = 24

print(solution(br, yel))
