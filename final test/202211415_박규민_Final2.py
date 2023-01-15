def problem_2(bracket):
    list_result = []
    if '(' in bracket or ')' in bracket:
        num_1 = bracket.count('(')
        num_2 = bracket.count(')')
        if num_1 == num_2 :
            a = 'True'
        else:
            a = 'False'
        list_result.append(a)

    elif '[' in bracket or ']' in bracket:
        num_3 = bracket.count('[')
        print(num_3)
        num_4 = bracket.count(']')
        if num_3 == num_4 :
            b = 'True'
        else:
            b = 'False'
        list_result.append(b)
    
    elif '{' in bracket or '}' in bracket:
        num_5 = bracket.count('{')
        num_6 = bracket.count('}')
        if num_5 == num_6 :
            c = 'True'
        else:
            c = 'False'
        list_result.append(c)
    

    
    if 'False' in list_result:
        result = 'False'
    else :
        result = 'True'

        result = bool(result)

    return result


