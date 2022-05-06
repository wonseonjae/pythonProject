def solution(phone_book):
   phone_book.sort()
   answer = True
   for i in range(len(phone_book)):
       if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
           answer = False
           break
   return answer



phnum = ["119", "97979797", "1199999999"]

print(solution(phnum))
