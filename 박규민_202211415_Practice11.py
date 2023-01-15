# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

def matmul (mat1, mat2):
    try : 
        answer = [len(mat2[0])*[0] for i in range(len(mat1))]
        for i in range(len(answer)):
            for j in range(len(answer[i])):
                for k in range (len(mat1[i])):
                    answer[i][j] += mat1[i][k] * mat2[k][j]
    except IndexError : 
        answer = 'MatrixValueError'
    except Exception as e :
        answer = e 
    return answer


x = matmul([[3,2],[1,4]],[[1,3],[4,2]])
print(x)
x = matmul(0, 3)

x = matmul([[3,2,5],[1,4,3]],[[1,3],[4,2]])

