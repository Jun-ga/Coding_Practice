def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = [] #다리

    for i in range(bridge_length - 1): #다리길이
        bridge.append(0)
    
    bridge.append(truck_weights[0]) #트럭하나 다리에 미리 올려두고 시작
    truck_weights.pop(0)
    
    while bridge:
        answer += 1 #연산 한번 돌때마다 시간은 흐름
        bridge.pop(0) #초가 지날때 마다 0이든 트럭이든 건너야함 
        if len(truck_weights) != 0 : #다리에 올라가지 못한 트럭이 존재할때
            if sum(bridge) + truck_weights[0] <= weight: #다리 위의 총합과 다음차례 올라올 트럭이 하중보다 작으면 다음 차례 올라올 수 있음
                bridge.append(truck_weights[0]) 
                truck_weights.pop(0)

            else: #못 올라온다면 트럭대신 자리수 채워줌
                bridge.append(0)
		else: pass #트럭이 모두 다리를 건넜거나 다리 위에 있다면 pass, bridge.pop(0) 반복으로 다리 위에 있는 트럭들 내려주기 

    return answer
   
#비고
#제일 먼저 들어오는 트럭을 따로 안빼고 돌렸을때는 (아래 코드같이) 테스트 5번 항목 타임에러뜸
#while 안에 하나의 연산을 줄인 것만으로 타임에러 통과
'''
answer = 0
bridge = []

for i in range(bridge_length):
	bridge.append(0)
'''
    
    
