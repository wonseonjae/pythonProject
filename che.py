import math

def numberCheck(num):

    if num == 0 or num == 1:
        return False

    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
    return True

print(numberCheck(5))