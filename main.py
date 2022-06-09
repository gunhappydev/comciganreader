from comcigan import School

print("학교 이름을 입력해주세요")
school = input()
print("몇 학년이십니까?")
grade = int(input())
print("몇 반이십니까?")
period = int(input())

myschool = School(school)

print(str(myschool.name)+"의 이번 주 시간표입니다.")

print("월요일"+str(myschool[grade][period][0]))
print("------------------------------")
print("화요일"+str(myschool[grade][period][1]))
print("------------------------------")
print("수요일"+str(myschool[grade][period][2]))
print("------------------------------")
print("목요일"+str(myschool[grade][period][3]))
print("------------------------------")
print("금요일"+str(myschool[grade][period][4]))