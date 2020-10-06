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