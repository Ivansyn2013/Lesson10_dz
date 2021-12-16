class Cells:
    def __init__(self, numb):
        str_numb = str(numb)
        if str_numb.isdigit():
            self.numb = numb
        else:
            raise Exception('Введите целое число')

    def __add__(self, other):
        return f'Суммая ячеик:{self.numb + other.numb}' \
 \
    def __sub__(self, other):
        return f'{self.numb - other.numb}' if (self.numb - other.numb) > 0 else f'Ошибка. Получилось отрицательно число'

    def __mul__(self, other):
        _cell3 = Cells(self.numb * other.numb)
        return f'Результат умножения {_cell3.numb}'

    def __floordiv__(self, other):
        _cell3 = Cells(self.numb // other.numb)
        return f'Результат деления {_cell3.numb}'

    def __truediv__(self, other):
        pass

    def make_order(self, val):
        result = ['*' * val] * (self.numb // val)
        if self.numb % val:
            result.append('*' * (self.numb % val))
        return '\n'.join(result)


cell1 = Cells(56)
cell2 = Cells(15)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)
print(cell1.make_order(20))
