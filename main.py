def solution(participant, completion):
   dic = {}
   tmp = 0
   for p in participant:
       dic[hash(p)] = p
       tmp += int(hash(p))
   for c in completion:
       tmp -= int(hash(c))
   return dic[tmp]

part = ["leo", "kiki", "eden"]
comp = ["eden", "kiki"]

print(solution(part, comp))
