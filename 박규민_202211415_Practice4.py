# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

def addall(num_list):
    result = sum(num_list)
    return result


def bigger(a, b):
    a = int(a) or float(a)
    b = int(b) or float(b)
    if a > b :
        result = a
    else :
        result = b
    return result


def rep(string, char):
    if char in string:
        res = string.replace(char, '')
        return res


def sigma(n):
    if n != 0:
        return n + sigma(n-1)
    else:
        return 0


def facto(n):
    if n != 0:
        return n * facto(n-1)
    else:
        return 1