import re
s = input()
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
l = re.findall(r"(?<-[%s])([%s]{2,})[%s]" %(c,v,c),s,flags = re.IGNORECASE)
print(l)
