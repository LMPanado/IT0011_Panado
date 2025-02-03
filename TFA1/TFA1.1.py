fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")
slcname = fname[:3]

greeting = "Hello, {}! Welcome. You are {} years old.".format(slcname, age)

print("")
print("Full name: ", fname, lname)
print("Sliced name: ", slcname)
print("Greeting Message: ", greeting)