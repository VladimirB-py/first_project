import text

text_line = "new text"


def plus(a, b):
    return a + b


def mull(a, b):
    return a * b


def minus(a, b):
    return a - b

def failture():
    print('this is failture')

if __name__ == '__main__':
    print(plus(2, 3))
    print(minus(3, 4))
    print(mull(5, 7))
    text.up(text_line)
    failture()