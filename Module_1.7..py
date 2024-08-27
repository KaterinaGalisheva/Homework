grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#средний балл grades
grades[0]=((sum(grades[0])/len(grades[0])))
grades[1]=((sum(grades[1])/len(grades[1])))
grades[2]=((sum(grades[2])/len(grades[2])))
grades[3]=((sum(grades[3])/len(grades[3])))
grades[4]=((sum(grades[4])/len(grades[4])))
# студенты
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(len(grades)==len(students)) #значит мы можем применить команду zip()
students_list=list(students)
sort_students=sorted(students_list)
#теперь это списки с общей последовательностью
dictant=dict(zip(sort_students, grades))
print(dictant)