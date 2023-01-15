# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

import numpy as np
import matplotlib.pyplot as plt

def vecprod(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    result = np.dot(a, b)
    return result

# x = vecprod([1,2,3,4], [1,2,3,4])
# print(x)


def show_scatter(vec1, vec2):
    plt.scatter(vec1, vec2)
    result = plt.show()
    return result

# x = show_scatter([1,2,3,4], [1,2,3,4])
# print(x)
