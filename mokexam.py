def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    results = {1:0, 2:0, 3:0}
    for i in range(len(answers)):
        if student1[i % len(student1)] == answers[i]:
            results[1] += 1
        if student2[i % len(student1)] == answers[i]:
            results[2] += 1
        if student3[i % len(student1)] == answers[i]:
            results[3] += 1
    answer = []
    highscore = max(results.values())
    for i in range(1,4):
        if results[i] == highscore:
            answer.append(i)
    return answer

test = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(solution(test))
