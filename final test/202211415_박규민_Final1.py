def problem_1(a, n):

    def ten_num(n):
        b = n // 10
        return b

    def one_num(n):
        b = n % 10
        return b

    for i in range(n):
        a = a + ten_num(a) + one_num(a)

    result = a

    return result
