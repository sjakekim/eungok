a = 3

def local_variable() :
    global a
    b = 4
    a = a+b
    print(a)

print(a)

def local_variable_error() :
    print()

local_variable()