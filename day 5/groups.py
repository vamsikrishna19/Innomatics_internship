import re
s = input()
pattern = r'([a-z A-Z 0-9])\1'
a = re.search(pattern,s)
if a:
    print(a.groups()[0])
else:
    print(-1)
