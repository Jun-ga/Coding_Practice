def solution(brown, yellow):
    answer = []
    num =[]
    
    #갈색+노랑색 합의 약수들이 나올 수 있는 h,w
    #갈색은 2보다는 커야함
    #갈색이 제일 밖이므로 노란색의 길이는 -2씩 한 것
    #갈색 h, w에 각각 -2 한 것을 곱했을때 나오는 값이 총 노란색수 
    #총 노란색 = (h-2)*(w-2)
    
    total = brown + yellow
    
    for w in range(3,total+1):
        if total%w == 0:
            h = total//w
            if h < w : break
            num.append([h,w])
            
    for b in num:
        if (b[0]-2)*(b[1]-2) == yellow:
            answer.append(b)
            answer = sum(answer,[])

    return answer
