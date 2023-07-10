for entry in enumerate(['a','b','c']):
    print(entry)

for i, data in enumerate(['a','b','c']):
    print(i, data)

for i, data in enumerate(['a','b','c']):
    print(f"{i}번째는 {data}입니다.")

for i, data in enumerate(['a','b','c']):
    print("{}번째는 {}입니다." .format(i, data))