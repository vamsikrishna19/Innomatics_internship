import textwrap
from textwrap import fill
def wrap(string, max_width):
    a= fill(string,max_width)
    return a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
