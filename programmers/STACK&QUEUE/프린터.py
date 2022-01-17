def solution(priorities, location):
    answer = 0
    
    while len(priorities) > 0:
        if priorities[0] >= max(priorities): #중요도가 제일 큰 것이 첫번째라면
            priorities.pop(0) #인쇄 
            answer += 1 #개수 세기
            if location == 0: break #요청한 문서가 첫번째있을 경우 이미 인쇄 끝났으므로 break
                
        else :
            term = priorities.pop(0) 
            priorities.append(term) #대기목록의 제일 뒤로 보냄
            
        location -= 1 #자리가 한자리씩 땡겨졌으므로
        
		#location = 0 이고, 이때 중요도가 제일 큰 게 아니라면 요청 문서는 대기 문서 맨 뒤로 보내야함 
		#else문에 의해 location은 -1가 됨
        if location < 0 : 
            location = len(priorities) - 1 #요청 문서가 맨 뒤로 보내짐 예) 5개 문서 if 전 location = -1 if 후 loction = 4
            
    return answer
