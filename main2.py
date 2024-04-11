def print_params(a=10, b='Hi', c=True):
    print(a, b, c)


print('Функция с параметрами по умолчанию:')

print_params()
print_params(4, '  good by  ', False)
print_params(b=25)
print_params(c=[1, 2, 3])

print('Распаковка параметров:')

values_list = ['Hello', True, 44]

print_params(values_list)

print('Распаковка + отдельные параметры:')

values_dict = {'a': 10, 'b': 20, 'c': 30}
print_params(values_dict)
print_params(*values_dict)
print_params(**values_dict)

print()

values_list_2 = [33, 'bye bye']
print_params(*values_list_2, 42)
print('______________')


print('***************')
def func_with_params(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(a, b, *c)

func_with_params(33, 6)
func_with_params(4)
func_with_params(5)
func_with_params(6)
