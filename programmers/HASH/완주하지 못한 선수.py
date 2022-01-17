def solution(participant, completion):
    answer = ''

    ds ={}
    
    for i in participant :
        if i in ds.keys():
            ds[i] += 1
        else :
            ds[i] = 1
            
    for j in completion :
        if j in ds.keys():
            ds[j] -= 1
        else :
            pass           
    for k in ds.keys():
        if ds[k] != 0 :
            answer = k


    return answer
