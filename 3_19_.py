score = int(input("정수입력: ")) 
if score >= 90:
    print("성적 A")
    print("장학금 수여")

age_0=22
age_1=18

age = int(input('your age? '))
if age < age_0 and age > age_1:
    print("당신의 나이는 18~22세 사이입니다.")



year = int(input("type a year : "))
if(year%4==0 and year%100 !=0 )or(year%400)==0:
    print(year, "is leap year")
else:
    print(year, "is not a leap year")












