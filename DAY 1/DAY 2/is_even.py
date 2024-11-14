grades = {80: "A", 70: "B", 60: "C", 50: "D", 40: "E", 0: "F"}
attained_score = int(input("Enter your score: "))
if attained_score >= 80:
    grade = "A"
elif 70 <= attained_score < 80:
    grade = "B"
elif 60 <= attained_score < 70:
    grade = "C"
elif 50 <= attained_score < 60:
    grade = "D"
elif 40 <= attained_score < 50:
    grade = "E"
elif 0 <= attained_score < 40:
    grade = "F"
else:
    grade = "Invalid score"
print(f"You scored a {grade}")