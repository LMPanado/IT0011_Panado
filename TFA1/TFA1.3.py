lname = input("Enter your last name: ")
fname = input("Enter your first name: ")
age = input("Enter your age: ")
contact = input("Enter your contact number: ")
crs = input("Enter your course: ")

formatted = f"Last Name: {lname}\nFirst Name: {fname}\nAge: {age}\nContact Number: {contact}\nCourse: {crs}\n"

f = open("TFA1/students.txt", "a")
f.write(formatted)
f.close()

print("Student information has been saved to students.txt")

