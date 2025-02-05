# gradin
score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 85:
    grade = "A-"
elif score >= 80:
    grade = "B+"
elif score >=75:
    grade = "B"
elif score >= 70:
    grade = "B-"
elif score >= 65:
    grade = "C+"
elif score >= 60:
    grade = "C"
elif score >= 55:
    grade = "C-"
elif score >= 50:
    grade = "D"
else:
    grade = "F"
print(f"your score is: {grade}")
if score >= 60:
    print("YOU HAVE PASSED WITH FLYING COLOURS !!!!!")
else:
    print("YOU ARE A FAILURE!")