student={"name":"Naomi cherono", "age":16, "town":"anairo"}
student["age"]=16
del (student["age"])

# print(student)
# print(student["name"])
# print(student["age"])
# print(student["town"])

for key,value in student.items():
    print(f"{key}:{value}")