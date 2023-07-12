def hello_name(*args) :
    print(type(args))
    for name in args :
        print(f"{name}님 안녕하세요!!!")


hello_name("오이","오이1","오이2", "오이3")
hello_name("김태경", "김대뽕","김태풍")


def 함수(*args) :
    num = 0
    for i in args :
        num += i
    return num

print(함수(1,2,3,4,5,6,3,4,5,7,8,9,0))

def input_sum(*args) :
    args = input("원하는 숫자를 ,를 기준으로 적어주세요!!!")
    num = 0
    for i in args :
        if i == ',' :
            continue
        num += int(i)
    return num    

print(input_sum())

def keyword_함수(**kwargs) :
    print(type(kwargs))
    num = 0
    for i in kwargs.values() :
        num += i
    return num

print(keyword_함수(a=1,b=2,c=3,d=4))