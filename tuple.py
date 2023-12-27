student = ("Kevin",32,1.65, "male")

print(student.count("male"))
print(student.index("male"))


for i in student:
    if 1.65 in student:
        print("si hay estatura")