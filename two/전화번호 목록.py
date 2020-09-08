def solution(phone_book):
    phone_book = list(map(str, sorted(phone_book)))

    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            # if(phone_book[i] == str(j)[:len(phone_book[i])]):
            if(str(j).startswith(phone_book[i])):
                return False
    return True

# 새로 배운 점
'''
1. startswith()
'''
