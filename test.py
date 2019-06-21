import re

if __name__ == '__main__':
    text = "asd.123 asd asd123"
    print(
        re.findall("([a-z]+)(\.\d+)?", text)
    )
