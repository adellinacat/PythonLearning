import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        num = ''
        for i in range(len(self.matrix)):
            num = num + '\t'.join(map(str, self.matrix[i])) + '\n'
        return num

    def __add__(self, new):
        if len(self.matrix) != len(new.matrix):
            return None
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for el in range(len(self.matrix[i])):
                result[i][el] = self.matrix[i][el] + new.matrix[i][el]
        return Matrix(result)


list_1 = [[1, 2], [3, 4], [5, 6]]
list_2 = [[10, 20], [30, 40], [50, 60]]
num1 = Matrix(list_1)
num = Matrix(list_2)
print(num1)
summary = num1 + num
print('summary')
print(summary)
print(type(summary))