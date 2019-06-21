
# # Defination
# def add():
#     print("Something cool")
#
# # Object
# print(type(add))
#
# # Calling
# add()


# def is_even(my_number):
#     if my_number % 2 == 0:
#         return True
#     return False
#
#
# my_num = int(input("Enter number pls: "))
# if is_even(my_num):
#     print('Even')
# else:
#     print('Odd')


# def sum(a, b, c=None):
#     if c:
#         return a + b * c
#     return a + b
#
#
# print(sum(2, 2, 2))


# def trick(a=[]):
#     a = a.copy()
#     a.append(1)
#     print(a)
#
#
# trick()  # [1]
# trick()  # [1, 1]
# trick()  # [1, 1, 1]

# def get_all_even(num_lst):
#     return [x for x in num_lst if x % 2 == 0]
#
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# print(get_all_even(numbers))

# def callback():
#     print("I'm Callback!")
#
#
# def sum(a, b, c=None, callback=None):
#     result = a + b
#     if c:
#         result = a + b * c
#     if callback:
#         callback()
#     return result
#
#
# some = sum(1, 2, 3, callback)
# print(some)

# def sum(a, b, c=None, callback=None):
#     result = a + b
#     if c:
#         result = a + b * c
#     if callback:
#         callback()
#     return result
#
#
# print(sum(1, 3, callback=print))


# def get_all_even(a, b, c):
#     print(a, b, c, sep='|')
#
#
# get_all_even(**{'a': 1, 'b': 2, 'c': 3})


# a = ["sd", "wqeqwe", "asd", "qweewq", 'dss']
#
#
# def get_len(string):
#     return len(string)
#
#
# sorted(a, key=lambda x: len(x))
# sorted(a, key=get_len)

# my_lambda = lambda a, b: a + b
#
# def my_func(a, b):
#     sum = a + b
#     dev = a - b
#     return sum, dev
#
#
# print(my_func(3, 7))
# a, b = my_func(2, 7)
# print(a, b, sep='|')
#
# def endless(start=0):
#     count = start
#     while True:
#         yield count
#         count += 1
#
#
# for num in endless():
#     print(num)
#     if num == 100:
#         break

# some = endless()
# print(next(some))
# print(next(some))
# print(next(some))
# print(next(some))

# def add():
#     pass
#
#
# def save(data):
#     pass
#
#
# def delete(id):
#     pass
#
#
# if 1 < 0:
#     pass
#
# for x in range(10):
#     pass

# TODO EVIL!!!
# try:
#     1 / 0
# except:
#     pass


def some():
    a = 999
    print(a)


a = 10
