def solution(clothes):
    clothestypemap = {}

    for clothe, clothestype in clothes:
        print(clothe)
        print(clothestype)
        clothestypemap[clothestype] = clothestypemap.get(clothestype, 0) + 1
    answer = 1
    for clothestype in clothestypemap:
        answer *= (clothestypemap[clothestype]+1)
    return answer - 1



clo = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clo))
