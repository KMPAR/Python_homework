# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y 
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y 
   

def calc(total):
    total = total.replace('+', ' + ')
    total = total.replace('-', ' - ')
    total = total.replace('*', ' * ')
    total = total.replace('/', ' / ')
    total = total.split(' ')
    print(total)

    count_1 = total.count('/')
    count_2 = total.count('*')
    count_3 = total.count('+')
    count_4 = total.count('-')

    for i in range(count_1):
   
        if '/' in total:
            num_1 = (total.index('/'))
    
            print(num_1)

            a = (total[num_1 -1])
            b = (total[num_1 +1])
            a = float(a)
            b = float(b)
    
    
            result = divide(a,b)
            print(result)
    
            del total[num_1 -1 : num_1 +2]
            total.insert(num_1 -1, result)
            print(total)

    for i in range(count_2):
   
        if '*' in total:
            num_1 = (total.index('*'))
    
            print(num_1)

            a = (total[num_1 -1])
            b = (total[num_1 +1])
            a = float(a)
            b = float(b)
    
    
            result = multiply(a,b)
            print(result)
    
            del total[num_1 -1 : num_1 +2]
        total.insert(num_1 -1, result)
        print(total)    

    for i in range(count_3):
   
        if '+' in total:
            num_1 = (total.index('+'))
    
            # print(num_1)

            a = (total[num_1 -1])
            b = (total[num_1 +1])
            a = float(a)
            b = float(b)
    
    
            result = add(a,b)
            # print(result)
    
            del total[num_1 -1 : num_1 +2]
            total.insert(num_1 -1, result)
            # print(total)
    
    for i in range(count_4):
   
        if '-' in total:
            num_1 = (total.index('-'))
        
            # print(num_1)

            a = (total[num_1 -1])
            b = (total[num_1 +1])
            a = float(a)
            b = float(b)
    
    
            result = subtract(a,b)
            # print(result)
    
            del total[num_1 -1 : num_1 +2]
            total.insert(num_1 -1, result)
            # print(total)

    result = float(total[0])
    return result

exp = calc("19.731*5.0*14.31-17+9.57")
print(exp)