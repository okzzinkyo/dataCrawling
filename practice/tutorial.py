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

mathScore = int(input('수학점수는?'))
scienceScore = int(input('과학점수는?'))
studentIsPass = True

if mathScore + scienceScore > 100:
  studentIsPass = True
else:
  studentIsPass = False

if studentIsPass == True:
  print('합격')
else :
  print('불합격')

# 3. 시퀀스형
  # - 문자열형 '물','아이유','안녕하세요','HELLO' 

score = 0
str(score)
print(score)
# '0'