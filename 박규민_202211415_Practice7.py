# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민
def mat2edge(mat):
    f = open(mat, 'r')
    data = f.readlines()
    f.close()

    second = data[0]
    second = second.replace('\n', '')
    second_alpabet = second.split(',')
    del second_alpabet[0]
    # print(second_alpabet)
    cnt = len(second_alpabet)

    row1 = []
    row2 = []
    row3 = []
    row4 = []

    for i in range(cnt):
        i = second_alpabet[0]
        row1.append(i)
    for i in range(cnt):
        i = second_alpabet[1]
        row2.append(i)
    for i in range(cnt):
        i = second_alpabet[2]
        row3.append(i)
    for i in range(cnt):
        i = second_alpabet[3]
        row4.append(i)    

    num_1 = data[1]
    num_1 = num_1.replace('a', '')
    num_2 = data[2]
    num_2 = num_2.replace('b', '')
    num_3 = data[3]
    num_3 = num_3.replace('c', '')
    num_4 = data[4]
    num_4 = num_4.replace('d', '')

    num = num_1 + num_2 + num_3 + num_4
    num = num.replace('\n', '')
    num = num.split(',')
    del num[0]
    # print(num)

    row = row1 + row2 + row3 + row4
    # print(row)

    col = second_alpabet + second_alpabet + second_alpabet + second_alpabet
    # print(col)

    count_of_zero = num.count('0')

    for i in range(count_of_zero):
        if '0' in num:
            id = (num.index('0'))
            
            del num[id]
            del row[id]

            del col[id]

    result = [(x, y, z) for x, y, z in zip(row, col, num)]

    return result

print(mat2edge('w7_matrix.csv'))