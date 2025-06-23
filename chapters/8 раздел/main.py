from itertools import zip_longest

id = [1, 2, 3, 4, 5]

print(list(enumerate(id)))  # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

for i, el in enumerate(id):  # можно добавить аргумент start
    if not isinstance(el, int):
        break
    print(f"{i}: {el}")

print(enumerate(id))  # <enumerate object at 0x74e169d0df80>

i = 0

while i < 10:
    print(i)
    i += 1
else:
    print(1234)

names = ["Антон", "Ann", "John"]
cars = ["Honda", "BMV", "Ford"]

for name, car in zip(names, cars):
    print(f"{name}: {car}")
else:
    print(3456457)


# zip

names = ["Антон", "Ann", "John"]
cars = ["Honda", "BMV", "Ford"]

for name, car in zip(names, cars):
    print(f"{name}: {car}")

record = zip(names, cars)

print(record)  # HashCode
print(list(record))  # [('Антон', 'Honda'), ('Ann', 'BMV'), ('John', 'Ford')]

id = [1, 2, 3, 4, 5]
names = ["Антон", "Ann", "John"]
cars = ["Honda", "BMV", "Ford"]
record = zip(id, names, cars)

print(list(record))  # [(1, 'Антон', 'Honda'), (2, 'Ann', 'BMV'), (3, 'John', 'Ford')]


cars = ["Honda", "BMV"]
record = zip(
    id, names, cars
)  # зависит от самого короткого, но посмотрите на строку 60 и импортируте from itertools import zip_longest

print(list(record))  # [(1, 'Антон', 'Honda'), (2, 'Ann', 'BMV')]

record = zip_longest(id, names, cars)
print(
    list(record)
)  # [(1, 'Антон', 'Honda'), (2, 'Ann', 'BMV'), (3, 'John', None), (4, None, None), (5, None, None)]

record = zip_longest(id, names, cars, fillvalue="Нет")
print(
    list(record)
)  # [(1, 'Антон', 'Honda'), (2, 'Ann', 'BMV'), (3, 'John', 'Нет'), (4, 'Нет', 'Нет'), (5, 'Нет', 'Нет')]


# разархивировать -- оставить только кортежи
id = [1, 2, 3, 4, 5]
names = ["Антон", "Ann", "John", "Joseph", "Lisa"]
cars = ["Honda", "BMV", "Ford"]
record = zip(id, names, cars)
el, name, car = zip(*record)
print(el)
print(name)
print(car)

"""
(1, 2, 3)
('Антон', 'Ann', 'John')
('Honda', 'BMV', 'Ford')
"""


id = [1, 2, 3, 4, 5]
names = ["Антон", "Ann", "John", "Joseph", "Lisa"]
leader_dict = {i: name for i, name in zip(id, names)}
print(leader_dict)  # {1: 'Антон', 2: 'Ann', 3: 'John', 4: 'Joseph', 5: 'Lisa'}

leader_dict = dict(zip(id, names))
print(leader_dict)  # {1: 'Антон', 2: 'Ann', 3: 'John', 4: 'Joseph', 5: 'Lisa'}

# update
other_id = [6, 7]
other_names = ["George", "Lesya"]
leader_dict.update(zip(other_id, other_names))
print(
    leader_dict
)  # {1: 'Антон', 2: 'Ann', 3: 'John', 4: 'Joseph', 5: 'Lisa', 6: 'George', 7: 'Lesya'}


# transponing matrix
matrix = [[1, 2, 3], [1, 2, 3]]
transponing = [list(i) for i in zip(*matrix)]
print(transponing)  # [[1, 1], [2, 2], [3, 3]]
