student_score = {
   "Henrique": 71,
   "Ronaldo": 81,
   "Pedrinho": 91,
   "Diego": 52,
   "Naldo": 98
}

#Create a empty dictionary to receive the grades

students_grades = {}

#write for loop

for student in student_score:
   score = student_score[student]
   if score > 90:
      students_grades[student] = "Excelente!"
   elif score > 80:
      students_grades[student] = "Muito Bom!"
   elif score > 70:
      students_grades[student] = "Isso ai!"
   else:
      students_grades[student] = "Não foi tão bem!"
      
      
print(students_grades)