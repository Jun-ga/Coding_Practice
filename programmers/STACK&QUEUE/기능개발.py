def solution(progresses, speeds):
    import math
    answer = []
    time = []
    count = 0
    #배포에 걸리는 시간을 time에 저장
    #입출력 예2) time = [5,10,1,1,20,1] 
    for p , s in zip(progresses, speeds):
        time.append(math.ceil((100-p) / s))
        
    #비교군을 term에 저장 ex) term = 5    
    term = time[0]
   
    while len(time) > 0: #time의 길이가 0일때지까지 반복
        if term >= time[0] :#비교군이랑 같거나 작으면 배포가 가능
            time.pop(0) #배포한 것을 빼내고
            count += 1 #개수 카운트
            
        else :
            answer.append(count) #배포된 부분 업데이트
            count = 0 #개수 초기화
            term = time[0] #비교군 재설정
            
    answer.append(count)
    
    return answer

#입출력 2 경우 while 타임라인
#1회    
#5 >= 5 term = 5
#time = [10,1,1,20,1] <- pop(0) = 5
#count = 1
#2회
#5 >= 10 (x) -> else로 이동
#count 업로드 후 초기화
#비교군 term = 10으로 업데이트
#반복
