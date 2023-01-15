# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

#전체 리스트 로드
import csv

f = open('week3.csv','r')
rdr = csv.reader(f)

for line in rdr:
    print(line)

f.close() 

print()
print()

# 전체 평균 구하기
f = open('week3.csv','r')
rdr = f.readlines()[1:]

grade = []
for line in rdr:
    total = line.split(',')
    num = float(total[-1])
    grade.append(num)

avg = sum(grade) / len(grade)

print('전체 평균: ', round(avg,3))

#남,여 평균
f = open('week3.csv', 'r')
rdr = f.readlines()[1:]

female = []
male = []
for line in rdr:
    total = line.split(',')
    if 'F' in total[2]:
        num_1 = float(total[-1])
        female.append(num_1)

    else:
        num_2 = float(total[-1])
        male.append(num_2)

avg = sum(female) / len(female)
print('여자 평균: ', round(avg, 3))

avg = sum(male) / len(male)
print('남자 평균: ', round(avg, 3))


#16학번 평균
f = open('week3.csv', 'r')
rdr = f.readlines()[1:]

num_16 = []
for line in rdr:
    total = line.split(',')
    if '2016' in total[0]:
        num = float(total[-1])
        num_16.append(num)

avg = sum(num_16) / len(num_16)

print('16학번 평균: ', round(avg, 3))


#17학번 평균
f = open('week3.csv', 'r')
rdr = f.readlines()[1:]

num_17 = []
for line in rdr:
    total = line.split(',')
    if '2017' in total[0]:
        num = float(total[-1])
        num_17.append(num)

avg = sum(num_17) / len(num_17)

print('17학번 평균: ', round(avg, 3))


#18학번 평균
f = open('week3.csv', 'r')
rdr = f.readlines()[1:]

num_18 = []
for line in rdr:
    total = line.split(',')
    if '2018' in total[0]:
        num = float(total[-1])
        num_18.append(num)

avg = sum(num_18) / len(num_18)

print('18학번 평균: ', round(avg, 3))


#19학번 평균
f = open('week3.csv', 'r')
rdr = f.readlines()[1:]

num_19 = []
for line in rdr:
    total = line.split(',')
    if '2019' in total[0]:
        num = float(total[-1])
        num_19.append(num)

avg = sum(num_19) / len(num_19)

print('19학번 평균: ', round(avg, 3))

f.close() 
