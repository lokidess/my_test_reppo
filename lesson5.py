# some_file = open('data/some_file.txt', 'w')
# some_file.seek(10)
# some_file.write('New data')
# print(some_file.readlines())
# count = 0
# while True:
#     some_file.writelines(str(count))
#     count += 1
# some_file.writelines(str(1))
# some_file.close()

# with open('data/some_file.txt', 'a+', encoding='utf-8') as my_file:
#     my_file.read()
#     my_file.write('qweeqw')
#


class MySuperError(Exception):
    def __init__(self, *args, **kwargs):
        super(MySuperError, self).__init__("It's my super error. Live with it")


try:
    raise MySuperError
except MySuperError as e:
    print(e)
