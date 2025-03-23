def divide(a, b):
    return None if b == 0 else a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    return None if b == 0 else a % b

def summation(a, b):
    return None if a > b else sum(range(a, b + 1))

def main():
    operations = {
        'D': divide,
        'E': exponentiate,
        'R': remainder,
        'F': summation
    }

    while True:
        print("\n[D] Divide")
        print("[E] Exponentiate")
        print("[R] Remainder")
        print("[F] Summation")

        choice = input("Enter choice: ").strip().upper()
        
        if choice in operations:
            try:
                a = int(input("First number: "))
                b = int(input("Second number: "))
                result = operations[choice](a, b)
                print("Result:", result if result is not None else "Invalid input")
            except ValueError:
                print("Invalid input! Enter numbers only.")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()