import re
from num2words import num2words

special = "!@#$%^&*()_"
text = '#H$e%#ll@#o'

special = '[' + special + ']'

result = re.sub(special, "", text)

print(result)

number = re.compile('\d+')


x = "23 is good, 24's 223, and 2.3 is "
x = re.sub('\d+', lambda n: num2words(int(n.group())), x)

print(x)

x = "I'm banana"
x = re.sub('\d+', lambda n: num2words(int(n.group())), x)

print(x)

