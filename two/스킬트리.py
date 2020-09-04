def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        temp = list(skill)
        for j in i:
            # 선행 스킬 목록에 있으면서
            if(j in temp):
                # 선행스킬을 배우지 않았다면 break
                if(j != temp.pop(0)):
                    break
        # 선행스킬을 순서대로 배워서 break에 걸리지 않았을 때
        else:
            answer += 1
    return answer


# 새로 배운 점
'''
1. for-else의 else는 for문이 중간에 break을 만난 적이 없을 때 수행된다. 반복문에서 flag를 사용했을 때 대체하여 사용할 수 있다.
'''
