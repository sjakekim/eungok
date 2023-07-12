#람다 표현식에 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_a = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(list_a)

#filter 사용하기
def f(x) :
    return x > 5 and x < 10

a = [8,3,2,10,15,7,1,9,0,11]

print(list(filter(f,a)))