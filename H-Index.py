def solution(citations):
    for idx, citation in enumerate(citations):

        if idx >= citation:
            return idx

    return len(citations)


test = [3, 0, 6, 1, 5]
solution(test)
