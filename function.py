def say():
    return 'hi'
a = say()
print(a)

def add(a,b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))
add(3,4)


def add(a,b):
    return a+b
result = add(3,7)
print(result)

#return 함수 사용하기
def say_nick(nick):
    if nick == '바보':
        return print("사용할 수 없는 별명입니다.")
    print("나의 별명은 %s 입니다." %nick)

say_nick('야호')
say_nick('바보')

#매개변수에 초깃값 미리 설정하기 
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나의 나이는 %d살 입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("점프투", 26, False)
# man = True 라는 초기값을 주었기 때문에, 입력하지 않아도 '남자입니다'라고 출력된다. 
#다만 이 같은 초깃값을 설정해 놓은 매개변수는 맨 뒤로 위치시켜야 오류가 안 뜬다. (name, man= True, old) 이런 형태는 오류뜸. 
say_myself("점프투", 26)


def vartest(a):
    a = a + 1
    return a
print(vartest(2))

#lambda: lambda 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다. lambda 함수는 return 명령어가 없어도 결괏값을 돌려준다. 
add = lambda a, b: a+b
result = add(3,4)
print(result)

def add(a,b):
    return a+b
result = add(3,4)
print(result)

test = lambda a,b: a*b
result = test(5,6)
print(result)

number = input("숫자를 입력하세요: ")
print(number)

for i in range(10):
    print(i, end='👀')

