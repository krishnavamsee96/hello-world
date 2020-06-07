courses= []
grades = []
def data():
    i = 0
    while (i <= 2):
        CourseName = input("Enter Class Name: ")
        courses.append(CourseName)
        i = i +1
    print(courses)
    j = 0
    while (j <=2):
        grade = int(input("Enter Your grades for each class (only numbers): "))
        grades.append(grade)
        j = j + 1
    calculate()
    
def calculate():
    GPA= 0
    for i in range(0,3):
            GPA = grades[i] + GPA
            Final_GPA = GPA / 3
    print(Final_GPA)
data()
