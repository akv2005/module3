print('1---------------------')
def test_1(nn=1, *types, names_="Имя, ", **dict):
    print("Type:", type(dict))
    print(nn,names_, "Фамилия:", *dict.values())
    print(types)

test_1(2, 3, 4, names='Иван', fam = 'Сидоров')

print('2---------------------')
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print('Факториалал', factorial(6))