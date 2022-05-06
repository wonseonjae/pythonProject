

def solution(numbers):
   numbers = list(map(str, numbers))
   numbers.sort(key=lambda x : x*3, reverse=True)
   return str(int(''.join(numbers)))

num = [6,10,2]
print(solution(num))


