

counter = 5

while counter > 0 :
    # ask frist name
    first_name_input = input('Enter your first name: ')
    # ask last name, if last name is ZZZ then stop
    last_name_input = input('Enter your last name: ')
    if last_name_input == "ZZZ":
        break
    # Ask for GPA, if GPA is 3.5-3.24 you made dean's list
    ask_gpa = float(input('What is your GPA?: '))
    if ask_gpa == 3.5 or 3.24:
        print(f"{first_name_input} has made the Dean's List.")
    # if you have a 3.25 and higher GPA you made Honor Roll
    elif ask_gpa >= 3.25:
        print(f'{first_name_input} has made Honor Roll.')
