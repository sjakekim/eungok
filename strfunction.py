str = "Hello"

a = len(str)

for i in range(0,a):
    print(str[i] + "_" , end="!!!")

str_1 = "Hello World"
str2 = str_1.upper()
print(str2)

bool = str2.isupper()
print(bool)

str2.swapcase()
print(str2)

a = "Hello world"
b = a.replace("Hello","Hi")
print(b)

str =''' 
안녕하세요.
비오는 화요일입니다.
어서오세요.
반갑습니다.
'''

result = str.splitlines()
print(result)