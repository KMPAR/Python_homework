# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민
import csv

def get_high(fn):
    data = []
    data1 = []
    data2 = []
        
    with open(fn,'r',encoding='utf-8') as file:
        csv_data = csv.reader(file)

        for row in csv_data:
            group = row[4].strip()
            if group == '사립':
                data.append(row)

        for row in data:
            group1 = row[2].strip()
            if group1 == '고등학교':
                data1.append(row)
        
        for row in data1:
            data2.append(row[1])

    data2.sort()
    result = data2

    with open('week12_박규민.csv', 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file, delimiter=' ', quotechar =' ', quoting=csv.QUOTE_ALL)
        for row in data2:
            writer.writerow([row])
        return result

print(get_high('w12_school.csv'))