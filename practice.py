#if, while, for문 연습문제 
# https://wikidocs.net/42527
#01. 다음 코드의 결과값은 무엇인가? 
a = "Life is too short, you need python"

if "wife" in a : print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else: print("none")

#02. While문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.
#1) 1에서 1000까지의 자연수 중 3의 배수를  

result = 0
i = 1
while i <=1000:
    if i % 3 ==0:
        result = result + i 
    i = i +1
        
print(result)


#03. While문을 사용해 별(*)을 표시하는 프로그램을 작성해 보자. 
#별을 줄지어 1개, 2개, 3개, 4개, 5개 표시

i = 0
while i <= 4:
    i = i+1
    print("*"*i)
   
#04. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for a in range(1,101):
    print(a)

#05. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다. 
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0 
for score in A:
    total = total + score 
#합을 먼저 구한다. 

average = total / len(A)
print(average)
#그다음에 학생 수로 나눠준다. 


#06.(01)다음의 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드를 만들어라
numbers = [1,2,3,4,5]
result=[]
for a in numbers:
    if a %2 ==1:
        result.append(a*2)
    print(result)

#06.(2)위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
numbers = [1,2,3,4,5]
result = [result*2 for result in numbers if result %2 ==1 ]
print(result)

