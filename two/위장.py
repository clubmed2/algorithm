def solution(clothes):
    clothes_dict = {}
    answer = 1

    for i in clothes:
        if (i[1] in clothes_dict.keys()):
            clothes_dict[i[1]] += 1
        else:
            clothes_dict[i[1]] = 1  # 아무 것도 입지 않는 경우를 추가한 상태로 카운트
            clothes_dict[i[1]] += 1
    for i in clothes_dict.keys():
        answer *= clothes_dict[i]
    answer -= 1  # 아무 것도 입지 않는 경우는 없다.
    return answer


# 새로 배운 점
'''
1. 없음
'''
