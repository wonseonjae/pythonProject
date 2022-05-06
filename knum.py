def solution(array, commands):
   answer = []
   for i in range(len(commands)):
       arr_list = array[commands[i][0]-1:commands[i][1]]
       arr_list.sort()
       answer.append(arr_list[commands[i][2]-1])
   return answer

arr = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr, com))
