print('Задание №1')


class Matrix:
    """ Класс матрица """
    @staticmethod
    def check_list(lst):
        ln = [len(el) for el in lst]
        return True if len(set(ln)) <= 1 else False

    def __init__(self, elements_list):
        if not Matrix.check_list(elements_list):
            raise Exception('Переданный список невозможно преобразовать в матрицу')
        self.__matrix = elements_list

    def __str__(self):
        matrix_str = ''
        for line in self.__matrix:
            for el in line:
                matrix_str = matrix_str + '\t' + str(el)
            matrix_str = matrix_str + '\n'
        return matrix_str

    def __add__(self, other):
        if type(other) is not Matrix:
            raise Exception('Недопустимый тип слагаемого')
        res_mat = []
        for line1, line2 in zip(self.__matrix, other.__matrix):
            new_line = [a + b for a, b in zip(line1, line2)]
            res_mat.append(new_line)
        return Matrix(res_mat)


test_list = [[1, 2, 3], [4, 5, 6], [1, 4, 6], [6, 4, 8]]
test_list2 = [[8, 6, 4], [9, 0, 3], [1, 6, 3], [7, 5, 0]]
c = Matrix(test_list)
print(c)
d = Matrix(test_list2)
print(d)
c = c + d
print('Сумма матриц:\n', c)
