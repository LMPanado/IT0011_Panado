records = []
filename = "records.txt"

while True:
    print("\nMenu:")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Add Record")
    print("9. Edit Record")
    print("10. Delete Record")
    print("11. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        try:
            records = [tuple(line.strip().split(",")) for line in open(filename)]
            print("Records loaded successfully!")
        except FileNotFoundError:
            print("File not found.")

    elif choice == '2':
        open(filename, "w").writelines(",".join(r) + "\n" for r in records)
        print("Records saved.")

    elif choice == '3':
        filename = input("Enter new filename: ")
        open(filename, "w").writelines(",".join(r) + "\n" for r in records)
        print("Saved as", filename)

    elif choice == '4':
        for r in records:
            grade = 0.6 * float(r[2]) + 0.4 * float(r[3])
            print(f"ID: {r[0]} | Name: {r[1]} {r[2]} | Grade: {grade:.2f}")

    elif choice == '5':
        records.sort(key=lambda r: r[2])
        print("Sorted by last name.")

    elif choice == '6':
        records.sort(key=lambda r: 0.6 * float(r[2]) + 0.4 * float(r[3]), reverse=True)
        print("Sorted by grade.")

    elif choice == '7':
        sid = input("Enter Student ID: ")
        for r in records:
            if r[0] == sid:
                print(r)
                break
        else:
            print("Not found.")

    elif choice == '8':
        while True:
            sid = input("Enter 6-digit Student ID: ")
            if len(sid) == 6 and sid.isdigit():
                break
            print("Invalid ID.")

        name = input("Enter First Name: "), input("Enter Last Name: ")
        try:
            records.append((sid,) + name + (input("Class Standing: "), input("Major Exam: ")))
            print("Record added.")
        except ValueError:
            print("Invalid input!")

    elif choice == '9':
        sid = input("Enter Student ID: ")
        for i, r in enumerate(records):
            if r[0] == sid:
                name = input("New First Name: "), input("New Last Name: ")
                records[i] = (sid,) + name + (input("New Class Standing: "), input("New Major Exam: "))
                print("Updated.")
                break
        else:
            print("Not found.")

    elif choice == '10':
        sid = input("Enter Student ID: ")
        records = [r for r in records if r[0] != sid]
        print("Deleted.")

    elif choice == '11':
        break

    else:
        print("Invalid choice.")

