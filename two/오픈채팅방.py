def solution(record):
    a = []
    current_nick = {}

    for i in record:
        i = i.split()
        if(i[0] == "Enter"):
            a.append({
                "id": i[1],
                "chat": "님이 들어왔습니다.",
            })
            current_nick[i[1]] = i[2]
        elif(i[0] == "Leave"):
            a.append({
                "id": i[1],
                "chat": "님이 나갔습니다.",
            })
        elif(i[0] == "Change"):
            current_nick[i[1]] = i[2]

    return [current_nick[i["id"]]+i["chat"] for i in a]


# 새로 배운 점
'''
1. 없음
'''
