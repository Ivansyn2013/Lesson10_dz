def my_list(x, y):
    res_list = []
    if type(x) == list:
        res1 = map(my_list, x, y)

        for el in res1:
            res_list.append(el)
        return res_list
    else:
        return x + y

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        for el in self.list:
            print(*IterMatList(el))
        return ''
        #return f'{[IterMatList(el) for el in self.list]}' как это реализовать?
    def __add__(self, other):
        return Matrix(my_list(self.list, other.list))





class IterMatList:
    def __init__(self, start):
        self.st = start
        self.i = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.st):
            self.i +=1
            return self.st[self.i-1]
        else:
            raise StopIteration




mc_list1 = [[31,22],[37,43],[51,86]]
mc_list2 = [[3,5,32],[2,4,6],[-1,64,-8]]
mc_list3 = [[3,5,8,3],[8,3,7,1]]

mc1 = Matrix(mc_list1)
mc2 = Matrix(mc_list2)
mc3 = Matrix(mc_list3)

print(mc1)
print(mc2)
print(mc3)
print(mc1+mc2)