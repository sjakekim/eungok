class Cat :
    def __init__(self, name, age) :
        self.__name = name
        self.__age = age

    def __str__(self) :
        return f"Cat(name={self.__name}, age={self.__age})"
    
    def lotto(self) :
        print(f"내 이름은 {self.__name}, 나이는 {self.__age})")

nabi = Cat("나비",10)
nero = Cat("네로",20)

print(nabi)
print(nero)

nabi.__age = 100
print("====================================================")
print(nabi) 
