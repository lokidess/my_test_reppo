# a = {"name": "Loki", "age": 29}
# b = a.copy()
# a["name"] = 'Tor'
#
# print(b)
# print(a)


# a = ['qwe', 'qasd', 123]
#
# b = dict.fromkeys(a)
# print(b)


# a = {"name": "Loki", "age": 29}
#
# print(a.items())

# a = {"name": "Loki", "age": 29}
# print(a.keys())

# a = {"name": "Loki", "age": 29}
#
# print(a.pop('last_name', None))
# print(a)

# a = {"name": "Loki", "age": 29}
# print(a.setdefault(
#     'last_name',
#     'name'
# ))

# a = {"name": "Loki", "age": 29}
# b = {"last_name": 'God', 'age': 999}
#
# a['some_new_key'] = 78
# a.update(b)
# print(a)

# a = {"name": "Loki", "age": 29}
# print(a.values())

# a = {"name": "Loki", "age": 29}
# print(a.get('last_name', 0))

# a = [1, 2, 3, 4, 5, 6]
#
# print(1 in a)
#
# a = {"name": "Loki", "age": 29}
# print('Loki' in a.values())


# print(1 > 0 and 0 < 1)

# print(2 < 1 or 0 < 1)

# False != False in [False]
#
# (False != False) in [False]
#
# False != (False in [False])

# value = input('Enter a number: ')
#
# splited_value = value.split('.')
#
# if value.isdigit():
#     print("Yeah! It's a number!")
# elif len(splited_value) == 2 \
#     and splited_value[0].isdigit() \
#     and splited_value[1].isdigit():
#     print("Yeah! It's a float")
# else:
#     print('Seams like a string')

# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         continue
#     elif i == 4:
#         break
#     i += 1

# i = 0
# a = ['qwe', 'asd', 'zxc']
#
# while i < len(a):
#     print(a[i])
#     i += 1

# a = ['qwe', 'asd', 'zxc']
#
# for item in a:
#     print(item)
#     if item == 'zxc':
#         break
# else:
#     print('All values was processed')

# a = {"name": "Loki", "age": 29}

# for _, value in a.items():
#     print(f'Val: {value}')

# a = ['qwe', 'asd', 'zxc']
# print(list(enumerate(a)))
#
# for num, value in enumerate(a):
#     print(f'{num}, {value}')

# a = ['qwe', 'asd', 'zxc']
# iter_a = iter(a)
# print(iter_a)
# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))

for odd in (x for x in range(2, 100) if x % 2 == 0):
    print(odd)

