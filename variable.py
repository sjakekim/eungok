a = 10
b = "Hello"

print(type(a))
print(type(b))


a = True
print(type(a))

c=d=e=100
f,g,h = 10,35,23

print(a, b, c, d, e, f, g, h)

str = "안녕하세요!!! 'Jake'"

str_literal = ''' dfasdfsafsdafdsaf
lorem \n
dfasfsadfsdfsdfdsafdsaf\n
'''

print(str)
print(str_literal)

#리터럴 표기 방법

name = "김석중"
literal_1 = "안녕하세요!!!" + "  " + name + " fdwfewrr"
print(literal_1)

literal_2 = f"안녕하세요!!! {name} fdwfewrr"
print(literal_2)