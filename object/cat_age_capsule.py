class Cat :
    def __init__(self, name, age) :
        self.__name = name
        if age <= 3 :
            raise ValueError('3살 이상의 야옹이만 입장 가능합니다.')
        self.__age = age

    def __str__(self) :
        return f"Cat(name={self.__name}, age={self.__age})"

    @property
    def age(self) :
        return self.__age
    
    @age.setter
    def age(self, age) :
        if age <= 10 :
            raise ValueError('10살이 넘어야 이름을 바꿀 수 있습니다.')
        self.__age = age

cat = Cat('나비',4)
print(cat)
print('===================================================')
cat.age = 11
print(cat)

