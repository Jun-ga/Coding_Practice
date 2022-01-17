def solution(clothes):
    answer = 0
    clo_hash = {}
    
    for clothe in clothes:
        if clothe[1] not in clo_hash.keys():
            clo_hash[clothe[1]] = 1
        else:
            clo_hash[clothe[1]] += 1
    
    answer = 1    
    for option, num in clo_hash.items():
        answer *= (num+1)
    return answer-1
