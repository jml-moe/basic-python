# function -> reusable unit of code

def say_hello():
    print("hello")

say_hello()

def name_student(name):
    print(f"my name is {name}")

name_student("jamil")

def my_grade(sem1, sem2):
    return(sem1 + sem2)
result = my_grade(80, 90)

print(result)