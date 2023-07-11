a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']
e = [1, 2, ['Life', 'is']]
f = list(range(0,11))

print(b)

#리스트 수정


del f[1]
print(f)

a.append(3)
print(a)
a.insert(0,4)
a.insert(5,3)
print(a)
a.append([3,4])
print(a)
a.insert(0,[3,4])
print(a)

