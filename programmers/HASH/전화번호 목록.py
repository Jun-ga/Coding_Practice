#ver1  
#정확도 O, 효율성 X

def solution(phone_book):
    answer = True  
    temp = []
    for i in range(len(phone_book)):
        temp.clear()
        for a in range(len(phone_book)):
            temp.append(phone_book[a])
        temp.remove(temp[i])
        for j in range(len(phone_book)-1):
            if phone_book[i] == temp[j][0:len(phone_book[i])]:
                answer = False
        return answer 

#ver2
#정확도 O, 효율성 O
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                answer = False

    return answer


