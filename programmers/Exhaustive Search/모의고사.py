def solution(answers):
    per_answer = [] #삼인방 맞은 개수
    answer = []
    term = 0 #맞은 개수 
    person = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]] #답안
    person_num = [5,8,10] #반복되는 답안
    
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == person[i][j%person_num[i]]: # j%person_num[i]는 삼인방 반복되는 답안처리
                term += 1 #term에 정답일시 넣음
        per_answer.append(term) #한 사람끝나면 저장
        term = 0 #새롭게 시작 전 맞은 개수 리셋
    
    for i, num in enumerate(per_answer): 
        if num == max(per_answer): #제일 많이 맞은 사람
            answer.append(i+1) #제일 많이 맞은 사람의 인덱스 출력 0부터 시작하므로 +1
    
    return answer
