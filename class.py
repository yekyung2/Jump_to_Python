#클래스 구조 만들기
# class FourCal:
#     pass

# a = FourCal()
# print(type(a))

#객체에 숫자 지정할 수 있게 만들기 a.setdata(4,2)
#클래스 안에서 구현된 함수는 '메서드(Method)'라고 부른다. 
class FourCal :
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4,2)
print(a.first)


b = FourCal()
b.setdata(3,7)
print(b.first)

print(id(a.first))
print(id(b.first))
print(a.add())
print()

print("사칙연산 계산기 테스트2")
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result 

a = FourCal()
a.setdata(90,9)
print(a.first)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())