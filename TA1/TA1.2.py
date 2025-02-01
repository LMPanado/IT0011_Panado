total = 0
input_string = input ("Enter a string containing digits: ")
for char in input_string:
     if char.isdigit():
         total += int(char)
print ("The sum of digits is: ", total)