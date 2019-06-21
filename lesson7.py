# import datetime
#
# from my_lib.utils import no_numbers
# from my_lib.func import no_numbers as no_numbers_func
# # import utils
# # from utils import * TODO: EVIL!!!
# # import my_lib
#
#
# def some():
#     pass
#
#
# if __name__ == "__main__":
#     # text = input('Enter text: ')
#     # print(no_numbers(text))
#     # no_numbers_func(text)
#     my_date = '17-06-2019'
#     # import pdb
#     # pdb.set_trace()
#     dt = datetime.datetime.strptime(
#         my_date, "%d-%m-%Y"
#     )
#     dt_str = dt.strftime("%d-%B-%y %H:%M")
#     print(dt_str)
#     some = [
#     {
#         'name': 'loki',
#         'cars': ['super', 'not super', 'average'],
#         'cat': {
#             'name': 'Tor',
#             'age': 10,
#             'toys': [
#                 'loki jacket', 'loki mouse',
#                 'loki legs'
#             ]
#         }
#     },
#         {
#             'name': 'loki',
#             'cars': ['super', 'not super', 'average'],
#             'cat': {
#                 'name': 'Tor',
#                 'age': 10,
#                 'toys': [
#                     'loki jacket', 'loki mouse',
#                     'loki legs'
#                 ]
#             }
#         },
#         {
#             'name': 'loki',
#             'cars': ['super', 'not super', 'average'],
#             'cat': {
#                 'name': 'Tor',
#                 'age': 10,
#                 'toys': [
#                     'loki jacket', 'loki mouse',
#                     'loki legs'
#                 ]
#             }
#         },
#         {
#             'name': 'loki',
#             'cars': ['super', 'not super', 'average'],
#             'cat': {
#                 'name': 'Tor',
#                 'age': 10,
#                 'toys': [
#                     'loki jacket', 'loki mouse',
#                     'loki legs'
#                 ]
#             }
#         },
#         {
#             'name': 'loki',
#             'cars': ['super', 'not super', 'average'],
#             'cat': {
#                 'name': 'Tor',
#                 'age': 10,
#                 'toys': [
#                     'loki jacket', 'loki mouse',
#                     'loki legs'
#                 ]
#             }
#         }
#     ]
#     from pprint import pprint
#     pprint(some)

import re

# regexp = r'^-?\d+(\.\d+)?$'
regexp = r'^\d+$'
text = """
qwewqeqwe qw eqw e qwe qwe qwe 32 432 ase d 234wewdsr qaer  qwears ewq e4 awesdeqw3
"""

nums = re.findall('\d', text)
print(nums)

# while True:
#     val = input('Enter number: ')
#     if re.match(regexp, val):
#         print("Hell Yeah!")
#     else:
#         print('Are you stupid?! Number only!')



