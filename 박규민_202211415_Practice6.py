2# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민
# 참고 웹사이트 : https://pydole.tistory.com/entry/Python-2%EA%B0%9C%EC%9D%98-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EC%9A%94%EC%86%8C%EB%93%A4%EC%9D%84-%ED%95%A9%EC%B3%90%EC%84%9C-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%ED%83%80%EC%9E%85%EC%9C%BC%EB%A1%9C-%EB%B3%80%ED%99%98

def word_counter(fname):
    f = open(fname, 'r')
    lyric = f.readlines()
    f.close()

    content = ''
    for line in lyric:
    # line = line.strip()
        line = line.replace(',', '')
        line = line.replace('.', '')
        line = line.replace('-', '')
        line = line.replace("'", '')
        line = line.replace("\n", ' ')
        line = line.replace("\n\n", ' ')
        line = line.replace("          ", '')
    
        content = content + line

    content_1 = content.split(' ')
    content_lower = []
    for i in content_1:
        content_lower.append(i.lower())

    word = set(content_lower)
    word_list = list(word)
    del word_list[0]
    # print(len(word_list))

    list_i = []
    list_cnt = []

    for i in word_list:
        cnt = content_lower.count(i)
        list_i.append(i)
        list_cnt.append(cnt)

    result = { a:b for a,b in zip(list_i, list_cnt)}
    
    return result

print(word_counter('w6_snow_white.txt'))