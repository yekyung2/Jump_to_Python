#파이썬 for문 연습(1)
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#파이썬 for문 연습(2)
a = [(1,2), (3,4), (5,6)]
for (first, last) in a: 
    print(first + last)

#파이썬 for문 연습(3)
marks = [90, 25, 65, 45, 80]
number = 0 
for mark in marks: 
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)

#파이썬 for문 연습(4) : len 함수(리스트 안의 요소 개수를 돌려주는 함수)
marks = [90, 25, 65, 45, 80]
for number in range(len(marks)):
    if marks[number] <60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))


#파이썬 for문 연습(5) : 구구단
for i in range(2,10): 
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

#파이썬 for문 연습(6) : 리스트 내포 사용하기 *append*
# 1) a list의 각 항목에 3을 곱한 값을 result라는 리스트에 담는다. 
a = [1,2,3,4]
result = []
for num in a: 
    result.append(num*3)
print(result)

#리스트 내포를 사용해 간단히 표현하자.
a = [1,2,3,4]
result = [num* 3 for num in a]
print(result)

# 2) a list의 항목 중 짝수에만 3을 곱하여 담기 위해, 리스트 내포 안에 if 조건'을 사용한다.
a = [1,2,3,4]
result = [num*3 for num in a if num %2 ==0]
print(result)