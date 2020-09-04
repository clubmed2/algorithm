def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1

    # 현재 문자와 다음 문자가 같은지를 비교할 때 2중 반복문을 쓰는 대신 리스트 원소를 하나씩 당기고 마지막에 공백을 추가하여 한 번의 반복문으로 검사한다.
    # [a,a,b,b,a,c,c,c]
    # [a,b,b,a,c,c,c,'']
    for a, b in zip(words, words[1:] + ['']):
        # 같을때는 카운트만 해주고
        if a == b:
            cur_cnt += 1
        # 같지 않았을 때 현재 글자와 지금까지의 카운트를 묶어 res리스트에 넣는다.
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    # 길이를 잰다.
    sum = 0
    for word, cnt in res:
        if cnt > 1:
            sum += (len(word) + (len(str(cnt))))
        else:
            sum += len(word)
    return sum


def solution(text):
    answer = []
    text_len = len(text)

    if(text_len == 1):
        return 1
    for tok_len in list(range(1, int(text_len/2) + 1)):
        answer.append(compress(text, tok_len))
    return min(answer)


# 새로 배운 점
'''
1. min(string, key=len)
2. 현재 문자와 다음 문자가 같은지를 비교할 때 2중 반복문을 쓰는 대신 리스트 원소를 하나씩 당기고 마지막에 공백을 추가하여 한 번의 반복문으로 검사한다.
'''
