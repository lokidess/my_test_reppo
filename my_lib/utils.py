MY_SUPER_LIST = [1, 2, 3, 4, 5]


def no_numbers(text):
    from lesson7 import some
    some()
    for num in range(0, 10):
        text = text.replace(str(num), '')
    return text
