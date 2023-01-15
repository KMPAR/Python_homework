# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

import json

def get_count(input):
    with open (input, 'r', encoding='utf-8') as f:
        json_str = f.read()
        json_data = json.loads(json_str)

    children = json_data['data']['children']

    title_name = []

    for v in children:
        title1 = v['data']['title']
        title_lower1 = title1.lower()
        if 'python' in title_lower1:
            title_name.append(title_lower1)


    for v in children:
        try:
            title2 = v['data']['media']['oembed']['title']
            title_lower2 = title2.lower()
            title_name.append(title_lower2)

        except :
            continue


    result = len(title_name)
    return result

print(get_count('w15_python.json'))

