#클래스 구조 만들기
class FourCal:
    pass

a = FourCal()
print(type(a))

#객체에 숫자 지정할 수 있게 만들기 a.setdata(4,2)
#클래스 안에서 구현된 함수는 '메서드(Method)'라고 부른다. 
class FourCal :
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4,2)
print(a.first)


b = FourCal()
b.setdata(3,7)
print(b.first)

print(id(a.first))
print(id(b.first))