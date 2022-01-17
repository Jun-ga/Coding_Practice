#ver1
#정확도 O 호율성 X
def solution(prices):
    answer = []
    while len(prices) > 0:
        if prices[0] <= min(prices):
            answer.append(len(prices)-1)
            #prices.pop(0)
            
        else:
            for i in range(1,len(prices)):
                if prices[0] > prices[i]:
                    answer.append(i)
                    break
        prices.pop(0)
            
    return answer
  
  
  
#고찰
#deque사용, if/else문 줄이기

#ver2
#정확도O, 효율성 O
from collections import deque #효율성 높이기 위해 deque 사용

def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices) > 0:
        count = 0 #떨어진 기간
        temp = prices.popleft() #주식가격
        for i in prices:
            count += 1 #탐색
            if temp > i : break #기준 주식가격이 더 높다면 빠져나옴
        answer.append(count) 
    return answer
  
