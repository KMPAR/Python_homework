class problem_3:
    def __init__(self, mat1, mat2):
        self.mat1 = mat1
        self.mat2 = mat2

    def mat_mul(self):
        result = [len(self.mat2[0])*[0] for i in range(len(self.mat1))]
        for i in range(len(result)):
            for j in range(len(result[i])):
                for k in range (len(self.mat1[i])):
                    result[i][j] += self.mat1[i][k] * self.mat2[k][j]
        
        return result





# 참고 : https://jeonzzang.tistory.com/23
# 참고 : https://hodunamu.com/python-행렬의-곱셈/