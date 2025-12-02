# Write a JSON file from a dict and read it back.


student1 = {"Name" : "Rishabh1", "roll_no" : 1000}
student2 = {"Name" : "Rishabh2", "roll_no" : 1001}
student3 = {"Name" : "Rishabh3", "roll_no" : 1002}
student4 = {"Name" : "Rishabh4", "roll_no" : 1003}

student_list = [student1,student2,student3, student4]


# 1] By importing json library
import json

# write
with open("jsonBook.json", "w") as f:
    json.dump(student_list, f, indent=4)
    
# read
with open("jsonBook.json", "r") as f:
    student_data = json.load(f)
    
for data in student_data:
    print(data)
    
    
# 2] Without importing json library

with open("jsonBook2.json", "w") as f:
    f.write("[\n")
    for i, s in enumerate(student_list):
        line = str(s).replace("'", '"')
        if i != len(student_list) - 1:
            f.write(line + "," + "\n")
        else:
            f.write(line + "\n")
    
    f.write("]")
    
with open("jsonBook2.json", "r") as f:
    data2 = f.read()
    print(type (data2))
    students = eval(data2)
    
print(students,type(students))
for student in students:
    print(student)
