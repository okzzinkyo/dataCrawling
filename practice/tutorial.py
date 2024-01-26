# 01. 설치 및 실행
# print('Hellow World!')



# 02.변수, 출력
# studentName = '옥진경'
# studentAge = 30
# student_age = 30
# studentage != studentAge (대소문자 구분O)
# 1studentAge >> X
# student age >> X
# student-age >> X

# print(studentAge)
# 30

# person = input('누구세요?')
# 누구세요?  아이유
# print(person)  
# 아이유



#03.자료형
# value의 종류 - 숫자형,논리형,시퀀스형,매핑형,집합형

# 1. 숫자형
  # - 정수 0,1,-1,100,100000000000
  # - 실수 1.4, 2.3, 4.6

    # 형변환
      # 변수의 자료형을 바꾸는 것 (ex. 정수 >> 실수)
      # int(3.0) >> 3
      # float(3) >> 3.0

    # 사칙연산
      # 나눗셈(/)
      # 나눗셈의 결과는 항상 실수로 계산되어 출력
      # 2/1 >> 2.0

      # 몫(//) 
      # 10//3 >> 3

      #나머지(%)
      # 10%3 >> 1

# 2. 논리형
  # - bool Trun,False 

# mathScore = input('수학점수는?') ..40
# scienceScore = input('과학점수는?') ..90
# ** error - 사칙연산
  # input() 문자든 숫자든 문자형으로 형변환한다.
  # input() 으로 입력받은 숫자는 숫자형으로 바꿔줘야한다.
  # int(input('수학점수는?'))

# mathScore = int(input('수학점수는?'))
# scienceScore = int(input('과학점수는?'))
# studentIsPass = True

# if mathScore + scienceScore > 100:
#   studentIsPass = True
# else:
#   studentIsPass = False

# if studentIsPass == True:
#   print('합격')
# else :
#   print('불합격')

# 3. 시퀀스형
  # - 문자열형 '물','아이유','안녕하세요','HELLO' 

# score = 0
# str(score)
# print(score)
# '0'



# 04.출력
# sep 각 출력 값 사이에 들어가는 것을 정의
# end 출력의 마지막에 end로 정의한 값이 붙어서 출력

print(1,2,3)
# 1 2 3

print(1,2,3, sep='')
# 123

print(1,2,3, sep='&')
# 1&2&3

print(1,2,3)
print(4,5,6)
# 1 2 3
# 4 5 6

print(1,2,3,end='')
print(4,5,6)
#1 2 34 5 6

# 포맷형 문자열 출력
month = '1월'
day = '24일'

print('Today is', month,day)
print('Today is %s %s' %(month,day))

month = 1
day = 24
print('Today is %d월 %d일' %(month,day))

month = 1
day = 24.0
print('Today is %f월 %f일' %(month,day))



# 05. 숫자형

# 제곱(**)

# 2*3
# 8

# (2**3)**2
# 64

count = 1
count = count + 1
count += 1
count -= 1
count *= 1
count /= 1
count %= 1
count //= 1

## pow(x,y) - 제곱함수
pow(2,3)  # 8

# abs(x) - 절대값 함수
abs(3)  # 3
abs(-3) # 3

# round(x) - 반올림 함수
round(3.66) # 4
round(3.24) # 3
round(3.225,1)  # 3.3 - 소수점 1의 자리에서 반올림
round(3.225,2)  # 3.25 - 소수점 2의 자리에서 반올림



# 06.문자열형

# "" 따옴표 출력
# 아이유가 말했다. "안녕하세요"
print('아이유가 말했다. "안녕하세요."')
print("아이유가 말했다.'안녕하세요.'")

# ''' 작은 따옴표 세개는 줄바꿈, "" 도 출력 가능하다.
# 아이유가 말했다
# "안녕하세요"
print('''아이유가 말했다.
      "안녕하세요"''')

word1 = '아이유'
word2 = '공유'

# 문자열 연산(더하기,곱하기)
print(word1+word2)
  # 아이유공유
print(word1*5)
  # 아이유아이유아이유아이유아이유


# 문자열에 해당 문자열이 존재하는지 아닌지 확인
# 결과는 True False로 출력됨
sentence = '장원영 안유진 리즈 가을 레이 이서'

'장원영' in sentence
# True
'장원영' not in sentence
# False

#문자열 대/소문자 변환
 
word = 'apple'
word.upper()
# APPLE

word2 = 'BANANA'
word.lower()
# banana

# upper/lower함수는 값 자체를 대/소문자로 바꾸는것은 아니다.

print(word)
# apple 

# 변환 값을 변수에 저장하고 싶다면 결과 값을 재할당한다.
word = word.upper()

print(word)
# APPLE

# 문자열 INDEX
# 문자에는 순서가 있어 특정 위치의 문자를 확인할 수 있다.
# 0부터 시작
word = 'samsungapple'

word[0]
# s

word[1]
# a

# 문자열 길이
len(word)
# 12

word[11]
# e

# 뒤에서 부터 count
word[-1]
# e

word[-2]
# l

# word[시작:하나 앞에서 종료]
word[0:2]
# sa

word[3:6]
# sun

word[:3]
# 0부터 2까지

word[5:]
# 5부터 끝까지



# 07. 조건문 과 부울형

# 1층에는 프론트를 넣고
# 2층에는 매점을 넣고
# 3층에는 피씨방을 넣고
# 4층 위는 주거집을 넣는다.

floor =  int(input('몇 층이냐? '))

if floor == 1:
  print('프론트 설치')
elif floor ==2 :
  print('매점 설치')
elif floor ==3 :
  print('피씨방 설치')
else:
  print('주거집 설치')

# if 조건1:
#   실행1
# elif 조건2:
#   실행2
# else: (조건1도 조건2도 아닌 그 외)
#   실행3

floor =  int(input('몇 층이냐? '))
apt = input('누구꺼? ')

if floor == 1 and apt == 'mine' :
  # and >> A 와 B 동시 만족
  # floor가 1층이고, 내꺼일때 실행
  print('프론트 설치')
elif floor == 2 or apt == 'mine':
  # or >> A 또는 B 만족
  # floor가 2층이거나 내꺼일 때 실행
  print('매점 설치')
else :
  print('주거지')



# 08.반복문

# while문
floor = 1
while floor < 10:
  print('%d층 청소' %floor)
  # floor = floor + 1
  floor += floor

print('끝!')

# 1층 청소
# 2층 청소
# 3층 청소
# 4층 청소
# 5층 청소
# 6층 청소
# 7층 청소
# 8층 청소
# 9층 청소
# 끝!

# for문
for i in 'Hello':
  print(i)

print('끝!')

# H
# e
# l
# l
# o
# 끝

# 반복문 - break
floor = 1
while True:
  print('청소')
  floor +=1
  if(floor > 5):
    break # 가장 가까운 반복문을 끝낸다

print(floor)

# 청소 ..floor = 2
# 청소 ..floor = 3
# 청소 ..floor = 4
# 청소 ..floor = 5
# 청소 .. break

# 반복문 - continue
floor = 1
while floor < 10 :
  floor += 1
  if floor % 2 == 0:
    continue # 반복문의 시작으로 돌아간다.
  print('%d층' %floor)

# 3층
# 5층
# 7층
# 9층
  


# 09.리스트형
students = ['옥진경', '아이유', '공유', '뷔', '정한']
print(students)

score = [100,90,50,40,100]
print(score)

price=['과자', 1000, '음료수', 3000]
print(price)

studentInfo = [students,score]
print(studentInfo)

# 리스트 - for문에 사용 가능
for i in students:
  print(i)

for i in score:
  print(i)

# range() - for문에 사용 가능
# range(시작값,끝값+1,커지는 값)
  
range(1,10,1)
# range(1,10)

list(range(1,10,1))
# [1,2,3,4,5,6,7,8,9]

list(range(1,100,11))
# [0,10,20,30,40,50,60,70,90]

for i in range(1,10,1):
  print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# 시작값이 없을 경우 0부터 시작!
for i in range(10):
  print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
  

# while문과 for문 - range()의 결과가 동일함
floor = 1
while floor < 10:
  print('%d층 청소' %floor)
  floor += floor

for i in range(1,10):
  print('%d층 청소' %i)

# list() - 형변환 
word = 'hellow'
temp = list(word)
print(temp)
# ['h','e','l','l','o','w']

# 리스트도 index(순서)를 이용해서 원하는 정보 추출 가능
score = [1,10,3,5,7,19]
print(score[0])
# 1
print(score[3:5])
# [5,7]



# 10.리스트연산
a = [1,2,3]
b=[100,200,300]

# 1.+
a+b
# [1,2,3,100,200,300]

b+a
# [100,200,300,1,2,3]

# 2.*
a*3
# [1,2,3,1,2,3,1,2,3]

# 3.A in B / A not in B
# A가 B에 있다/없다(True/False)
3 in a 
# True
4 in b 
# False

# 4.del[index]
# 대상이 존재하는 위치(index)를 괄호안에 적는다.
a = [1,2,3,4,5,6,7,8,9]
del a[1] 
# a[1] = 2 를 제거
# [1,3,4,5,6,7,8,9]

# 5.len()
# 리스트 길이를 출력한다
a = [1,2,5,7,5,44,4,4,36,8,6,2,4]
len(a)
# 13

# 6.max() / min()
a = [1,2,5,7,5,44,4,4,36,8,6,2,4]
# 가장 큰 값을 출력한다.
max(a) # 44
# 가장 작은 값을 출력한다.
min(a) # 1

# 7.append()
c = [1,4]
c.append(5)
# [1,4,5]

# 8.index()
a.index(5)
# '5'의 위치(index)를 출력한다.
# 4

# 9.remove()
a = [1,2,3,4,5,6,7,8,9]
a.remove(1)
# 지우고자 하는 대상을 괄호안에 적는다.
# a[2,3,4,5,6,7,8,9]

b = [1,2,3,2,4,5,6,7]
b.remove(2)
# 지우려는 대상이 여러개일때 맨 앞에 있는 값이 지워진다.
# [1,3,2,4,5,6,7]

# 10.pop()
a = [1,2,3,4,5,6,7,8,9]
a.pop()
# 맨 뒤에 있는 값이 제거되며 넘겨준다.
deleteValue = a.pop()
# 9
deleteValue = a.pop(2) 
# 해당 index의 값을 뺄 수 있다.
# 3

# 11.count()
a = [1,2,5,7,5,44,4,4,36,8,6,2,4]
a.count(4)
# 3

# 12.extend([])
a=[1,2,3]
b=[100,200,300]
a.extend(b)
# 변수에 재할당 하지 않아도 b가 더해진 리스트 출력
# a = a+b 와 동일
# [1,2,3,100,200,300]

# 13.sort()
# 순서대로 정렬
a=[7,6,56,4,3,12]
a.sort()
# [3,4,6,7,12,56]

# 14.reverse()
# 리스트 순서만 뒤집어서 출력
a=[7,6,56,4,3,12]
a.reverse()
# [12,3,4,56,6,7]



# 11. 컴퓨팅 사고
# 컴파일 언어(C언어) - 내부 속도 빠름,
# 인터프린터 언어(python) - 수정이 용이, 컴퓨터 언어로 변환하는 작업이 필요
# if, while, for문을 통해 동작한다
# 알고리즘 - 일련의 과정을 따르는 것



# 12.함수
# 반복적으로 재사용할 수 있게 만들어 놓은 코드

def f(x):
  return print(x)

f('hello')
f('Jinkyung ock')
f('Yeah~!')

# hello
# Jinkyung ock
# Yeah~!

def add(x):
  x += 5
  return x

print(add(4))
print(add(6))
print(add(9))

# 9
# 11
# 14

a = 1  # 전역변수
def increase(a):
  a += 1 # 지역변수
  return a
b= increase(a)

print(b)
# 2
print(a)
# 1


# 변수를 복사해서 함수로 전달한다.
# 하지만, 리스트를 전달할 때는 리스트가 있는 좌표를 전달하기 때문에
# 함수 안에서 리스트를 조작할 경우 전역 변수에 선언된 리스트 값도 변한다.
a = 1
def increase(n):
  n+=1
  return n

def inc_list(l): # [1,2,3]
  for i in range(len(l)): # for i in range(3) == range(0,3,1) == [0,1,2]
    l[i] +=1 # i==0, l[0] = l[0] + 1
  return l # [2,3,4]

b = increase(a) 
l1 = [1,2,3]
l2 = inc_list(l1) # [2,3,4]

print(a,b,l1,l2) 
# 1 2 [2,3,4] [2,3,4]


# 갯수 상관없이 변수를 받고자 할때
# 파라미터명 앞에 *(별표) 표시를 한다.
def sum_many(*a):
  sum = 0
  for i in a:
    sum += i
  return sum
  
print(sum_many(1))
print(sum_many(1,2))
print(sum_many(1,2,3,4))
print(sum_many(1,2,3,4,5))


# 함수의 파라미터에 기본값을 선언하여
# 어떤 인자도 받지 않았을 때 사용된다.
def print_id(num=100, name='홍길동'):
  print(num,name)

print_id()
# 100 홍길동
print_id(200,'CT')
# 200 CT