def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y 
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y 

def calc(expression, priority):
    try:
        if '+' in expression or '-' in expression or '*' in expression or '/' in expression:
    
            total = expression
            total = total.replace('+', ' + ')
            total = total.replace('-', ' - ')
            total = total.replace('*', ' * ')
            total = total.replace('/', ' / ')
            total = total.split(' ')
            
            priority_len = len(priority)
            if priority_len == 1:
                count_1 = total.count(priority[0])
                
                for i in range(count_1):
        
                    if priority[0] in total:
                        num_1 = (total.index(priority[0]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[0] == '+':
                            result = add(a,b)
                        elif priority[0] == '-':
                            result = subtract(a,b)
                        elif priority[0] == '*':
                            result = multiply(a,b)
                        elif priority[0] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)
                        

            elif priority_len == 2:
                count_1 = total.count(priority[0])
                count_2 = total.count(priority[1])  

                for i in range(count_1):
        
                    if priority[0] in total:
                        num_1 = (total.index(priority[0]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[0] == '+':
                            result = add(a,b)
                        elif priority[0] == '-':
                            result = subtract(a,b)
                        elif priority[0] == '*':
                            result = multiply(a,b)
                        elif priority[0] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)

                for i in range(count_2):
        
                    if priority[1] in total:
                        num_1 = (total.index(priority[1]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[1] == '+':
                            result = add(a,b)
                        elif priority[1] == '-':
                            result = subtract(a,b)
                        elif priority[1] == '*':
                            result = multiply(a,b)
                        elif priority[1] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)

            elif priority_len == 3:
                count_1 = total.count(priority[0])
                count_2 = total.count(priority[1])
                count_3 = total.count(priority[2])

                for i in range(count_1):
        
                    if priority[0] in total:
                        num_1 = (total.index(priority[0]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[0] == '+':
                            result = add(a,b)
                        elif priority[0] == '-':
                            result = subtract(a,b)
                        elif priority[0] == '*':
                            result = multiply(a,b)
                        elif priority[0] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)


                for i in range(count_2):
        
                    if priority[1] in total:
                        num_1 = (total.index(priority[1]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[1] == '+':
                            result = add(a,b)
                        elif priority[1] == '-':
                            result = subtract(a,b)
                        elif priority[1] == '*':
                            result = multiply(a,b)
                        elif priority[1] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)

                for i in range(count_3):
        
                    if priority[2] in total:
                        num_1 = (total.index(priority[2]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[2] == '+':
                            result = add(a,b)
                        elif priority[2] == '-':
                            result = subtract(a,b)
                        elif priority[2] == '*':
                            result = multiply(a,b)
                        elif priority[2] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)

            elif priority_len == 4:
                count_1 = total.count(priority[0])
                count_2 = total.count(priority[1])
                count_3 = total.count(priority[2])
                count_4 = total.count(priority[3])

                for i in range(count_1):
        
                    if priority[0] in total:
                        num_1 = (total.index(priority[0]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[0] == '+':
                            result = add(a,b)
                        elif priority[0] == '-':
                            result = subtract(a,b)
                        elif priority[0] == '*':
                            result = multiply(a,b)
                        elif priority[0] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)

                for i in range(count_2):
        
                    if priority[1] in total:
                        num_1 = (total.index(priority[1]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[1] == '+':
                            result = add(a,b)
                        elif priority[1] == '-':
                            result = subtract(a,b)
                        elif priority[1] == '*':
                            result = multiply(a,b)
                        elif priority[1] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)

                for i in range(count_3):
        
                    if priority[2] in total:
                        num_1 = (total.index(priority[2]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[2] == '+':
                            result = add(a,b)
                        elif priority[2] == '-':
                            result = subtract(a,b)
                        elif priority[2] == '*':
                            result = multiply(a,b)
                        elif priority[2] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)

                for i in range(count_4):
        
                    if priority[3] in total:
                        num_1 = (total.index(priority[3]))

                        a = (total[num_1 -1])
                        b = (total[num_1 +1])
                        a = float(a)
                        b = float(b)
                
                        if priority[3] == '+':
                            result = add(a,b)
                        elif priority[3] == '-':
                            result = subtract(a,b)
                        elif priority[3] == '*':
                            result = multiply(a,b)
                        elif priority[3] == '/':
                            result = divide(a,b)

                        del total[num_1 -1 : num_1 +2]
                        total.insert(num_1 -1, result)

            result = int(total[0])
        else:
            result = 'None'
    except:
        result ='None'
    return result


