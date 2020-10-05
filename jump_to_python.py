#if 문 연습
#파이썬 에디터 사용 연습 (1) 
money = 2000
if money >= 3000 :
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#파이썬 에디터 사용 연습 (2)
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#파이썬 에디터 사용 연습 (3)
print('안녕하세요'[0])
print('안녕하세요'[1])
print('안녕하세요'[2])
print('안녕하세요'[3])
print('안녕하세요'[4])

#파이썬 에디터 사용 연습(4)
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#파이썬 while 문 연습
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

#파이썬 while 문 연습(2) : 커피 자판기 이야기
coffee = 10
money = 300
while money: 
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# %개념 확인
name = 'scuba'
print('I am %s.' % name)

#파이썬 while 문 연습(3) : 커피 자판기 이야기2
coffee = 10
while True: 
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300: 
         print("거스름돈 %d를 주고 커피를 줍니다." %(money - 300))
         coffee = coffee -1
    else: 
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("%d원이 부족합니다." %(300 - money))
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
    break
