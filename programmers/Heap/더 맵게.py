#ver 2
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #리스트를 최소힙으로 변환
    while scoville[0] < K : #최소값이 K보다 크거나 같을때까지 반복
        if len(scoville) == 1 : return -1 #모든 음식 K 이상으로 불가능시 -1 리턴
        if scoville[0] >= K: break #test 16 오류 이유; 처음부터 모든 음식 K 이상일때 0 리턴  
            
        heapq.heappush(scoville,heapq.heappop(scoville)+ heapq.heappop(scoville) * 2) #연산
        answer += 1 #카운트
                  
    return answer

'''
#ver1
#정확도 test 16 미통 호율성 O
#고찰
#모든 음식이 K보다 클때 따로 작성해줘야함

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while 1 :
        if scoville[0] < K :
            heapq.heappush(scoville,heapq.heappop(scoville)+ heapq.heappop(scoville) * 2)
            answer += 1
            if len(scoville) == 1 :
                return -1
        else : break
                  
    return answer
'''
