def solution(str1, str2):
    str1a = []
    str2a = []
    gyo = []
    hap = []

    for i in range(len(str1)):
        if(len(str1[i:i+2]) == 2 and str1[i].isalpha() and str1[i+1].isalpha()):
            str1a.append(str1[i:i+2].lower())
    for i in range(len(str2)):
        if(len(str2[i:i+2]) == 2 and str2[i].isalpha() and str2[i+1].isalpha()):
            str2a.append(str2[i:i+2].lower())
    if (str1a == [] and str2a == []):
        return 1*65536
    if(len(str1a) < len(str2a)):
        str1a, str2a = str2a, str1a
    for i in str1a:
        if(i in str2a):
            gyo.append(i)
            hap.append(i)
            str2a.remove(i)
        else:
            hap.append(i)
    hap += str2a
    return int((len(gyo)/len(hap))*65536)


# 새로 배운 점
'''
1. 중복을 포함한 교/합집합 구하는 방법
'''
