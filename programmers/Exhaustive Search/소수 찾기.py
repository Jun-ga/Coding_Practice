from itertools import permutations

def prime_number(x): #소수 찾는 함수
    if x <= 1:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    
    
def solution(numbers):
    answer = 0
    num_prime = []      
    number = ','.join(numbers).split(',') #"17" > '1','7'로 변환
    
    for i in range(1,len(numbers)+1): #조합이용해서 가능한 모든 조합들 만듦
        num_prime.append(list(set(map(''.join,permutations(number,i))))) #set은 중복제거를 위해 사용
    num_prime = list(set(map(int,sum(num_prime,[])))) 
    #sum으로 num_prime의 [] 제거
    #sum 전 num_prime = [['7', '1'], ['17', '71']] sum 후 ['7','1','17','71']
    #int로 숫자열로 변경 , '011' -> '11' 기존의 '11'이 있으므로 set으로 중복제거
    
    
    for j in num_prime:
        if prime_number(j) == True : # 소수일때
            answer += 1 
    
    return answer
