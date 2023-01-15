def problem_5(sentence):
    a= sentence
    a = a.lower()
    a = a.replace(' ', '')

    list_a = list(a)

    if list_a[-1] == '?' or list_a[-1] == '.' or list_a[-1] == '!' or list_a[-1] == '~':
        shape = list_a[-1]

    else:
        shape = ''

    a = a.replace('?', '')
    a = a.replace('.', '')
    a = a.replace('!', '')
    a = a.replace('~', '')
    a = a + shape

    if '@' or '#' or '$' or '^' or '&' or '*' in a:
        a = a.replace('@', 'alpha')
        a = a.replace('#', 'beta')
        a = a.replace('$', 'gamma')
        a = a.replace('^', 'delta')
        a = a.replace('&', 'epsilon')
        a = a.replace('*', 'eta')

    list_b = list(a)

    if list_b[-1] == '?' or list_b[-1] == '.' or list_b[-1] == '!' or list_b[-1] == '~':
        a = a
    else:
        a = a + '.'

    if list_b[0].islower() == True:
        a = a.capitalize()
    
    result = a
    return result