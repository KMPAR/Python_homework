# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

class Person(object):
    def __init__(self, name, age, job):
        
        self.name = name
        self.age = str(age)
        self.job = job

    def get_status(self):
        return print('이름 : ' + self.name + ', 나이 : ' + self.age + ', 직업 : ' + self.job)



class Student(Person):
    def __init__(self, name, age, job, major, std_num, grade, GPA, my_prof):
        super().__init__(name, age, job)
        self.major = major
        self.std_num = std_num
        self.grade = str(grade)
        self.GPA = str(GPA)
        self.my_prof = my_prof



    def set_prof(self, my_prod):
        self.my_prof = my_prod

    
# a = Student('홍길동', 20, '학생', '산업공학', '202211415', 2, 3.5, '김종화')
# print(a.my_prof)

# a.set_prof('윤장혁')
# print(a.my_prof)

# a.get_status()

