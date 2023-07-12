def multiple_add(a,b,c) :
    num = a * b + c
    return num

res = multiple_add(2,3,4)
print(res)

#키워드 인자로 전달

res = multiple_add(a=2,c=4,b=3) 
print(f"키워드 값 {res}")

def multiple_add_keywords(a,b,c=100) :
    num = a * b + c
    return num

print(multiple_add_keywords(10,20))