############################################
###         Räkna ut veckodagen
###         Leonardo Gast
###         -------------
############################################

year = int(input("Year: "))
while year < 1583 or year > 9999:
    print("Out of allowed range 1583 to 9999")
    year = (int(input("Year: ")))

month = int(input("Month: "))
while month < 1 or month > 12:
    print("Out of allowed range 1 to 12")
    month = int(input("Month: "))
    
day = int(input("Day: "))
if (year %400 == 0 and year %100 == 0 and year %4 == 0) or (year % 4 == 0 and year % 100 != 0):
    while month == 2 and (day < 1 or day > 29):
        print("Out of allowed range 1 to 29")
        day = int(input("Day: "))

elif month == 2:
    while (day < 1 or day > 28):
        print("Out of allowed range 1 to 28")
        day = int(input("Day: "))

while month in (1, 3, 5, 7, 8, 10, 12) and (day < 1 or day > 31):
        print("Out of allowed range 1 to 31")
        day = int(input("Day: "))
    
while month in (4, 6, 9, 11) and (day < 1 or day > 30):
        print("Out of allowed range 1 to 30")
        day = int(input("Day: "))
        
if month == 1 or month == 2:
    month += 12
    year -= 1

weekday = (day + 13 * (month+1) //5 + year + year//4 - year//100 + year//400) % 7

if weekday == 0:
    print("\nIt is a Saturday")

elif weekday == 1:
    print("\nIt is a Sunday")

elif weekday == 2:
    print("\nIt is a Monday")

elif weekday == 3:
    print("\nIt is a Tuesday")

elif weekday == 4:
    print("\nIt is a Wednesday")

elif weekday == 5:
    print("\nIt is a Thursday")

else:
    print("\nIt is a Friday")
