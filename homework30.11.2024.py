def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(2, 'вторая строка')
print_params(c=False)
print_params(b=25)
list_ = [1,2,3]
print_params(*list_)
values_list = [10, True, 'очередная строка']
values_dict = {'a': 1234, 'b':  'опять строка?', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 'последняя строка']
print_params(*values_list_2, 42)