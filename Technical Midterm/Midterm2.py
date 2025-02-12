months = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

date_input = input("Enter the date (mm/dd/yyyy): ").strip()

parts = date_input.split('/')
month, day, year = parts
month_name = months[month]
day_num = int(day)
readable_date = f"{month_name} {day_num}, {year}"
print("Date Output:", readable_date)
