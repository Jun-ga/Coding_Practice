![구조](file:///C:/Users/gek75/Downloads/IMG_0300.jpg)
def solution(jobs):
    answer = 0
    time_term = 0
    term = []
    
    jobs = sorted(jobs, key=lambda x: x[1]) 
    
    while jobs:
        for i in range(len(jobs)):
            if time_term >= jobs[i][0]: #예외 1 처리
                time_term += jobs[i][1]
                term.append(time_term - jobs[i][0])
                jobs.pop(i)
                break
            if i == len(jobs) - 1: # 예외 2처리
                time_term += 1
                
    answer = sum(term) // len(term)

    return answer
