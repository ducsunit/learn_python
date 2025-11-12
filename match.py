day = 10
month = 5
match day:
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case 8:
        print("Sunday")
    case _:
        print("Looking forward to the weekend !")

# can add if statements in the case evaluation as an extra condition-check
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A week in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
