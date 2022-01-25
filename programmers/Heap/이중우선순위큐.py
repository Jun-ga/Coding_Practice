'''
import heapq
def solution(operations):
    answer = []
    heap_min = []
    heap_max = []
    oper = []
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(heap_min,int(i[1:]))
            heapq.heappush(heap_max,(-1 * int(i[1:]),int(i[1:])))
        else:
            oper.append(int(i[1:]))
            
    print(heap_min)
    print(heap_max)
    print(oper)
            
            
    for j in oper:
        if len(heap_min) == 0 : break
        elif j == -1:
            term_min = heapq.heappop(heap_min)
            heap_max.remove((-1 * term_min,term_min))
            print('min_min삭제',heap_min)
            print('min_max삭제',heap_max)

        else:
            term_max = heapq.heappop(heap_max)[1]
            heap_min.remove(term_max)
            print('max_min삭제',heap_min)
            print('max_max삭제',heap_max)
            
    print(heap_min)
    
    if heap_min :
        answer.append(heapq.heappop(heap_max)[1])
        answer.append(heapq.heappop(heap_min))
    else :
        answer.append(0)
        answer.append(0)
            
    return answer

'''
import heapq
def solution(operations):
    answer = []
    heap_min = [] #최소 힙
    heap_max = [] #최대 힙
    
    while(operations): #연산이 남아있을때까지 동작
        term_oper = operations.pop(0) #차례대로 연산을 oper_term 저장
        term = int(term_oper[2:]) #연산 중 숫자만 따로 D -11 일경우 term = -11
        if term_oper[:1] == 'I': #D -11일 경우 per_term[:1] = D 이 경우 else로 감.
            heapq.heappush(heap_min,term) #최소힙만들기
            heapq.heappush(heap_max,(-1 * term,term)) #최대힙 만들기, 안에 구조는 튜플구조 (예시) heap_max = [(-10,10),(12,-12)] 
        else:
            if len(heap_min) == 0 : pass #heap이 빈경우
            elif term == -1: #최솟값 제거일때
                term_min = heapq.heappop(heap_min) #최소힙에서 pop실행 이때 변수 저장해서 아래 최대힙도 pop 해야함 이유)최소힙과 최대힙은 안의 구성원이 동일해야함
                heap_max.remove((-1 * term_min,term_min)) #최대힙은 튜플로 되어있으므로 그 형식에 맞춰서 제거
                           
            else: #최댓값 제거일때
                term_max = heapq.heappop(heap_max)[1]
                heap_min.remove(term_max)
    
    if heap_min :
        answer.append(heapq.heappop(heap_max)[1])
        answer.append(heapq.heappop(heap_min))
    else :
        answer.append(0)
        answer.append(0)
            
    return answer
