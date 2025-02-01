numbers = [1, 3, 5, 6, 7]

i = 0

while i < len(numbers):
    num = numbers[i]
    j = 0
    
    while j < num:
        print(num, end="")
        j += 1

    print("\n")
    i += 1