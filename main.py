birthdays = {'Alice': 'April 1', 'Alex': 'November 3', 'Michael': 'January 10', 'Carol': 'May 5'}




while True:
    print("Enter a name: (print 'exit' to quit)")
    name = input()
    if name == 'exit':
        print("Are you sure you want to quit? Print 'yes' or 'no'.")
        answer = input().lower()
        if answer == 'yes' or answer == 'y':
            print('Understandable. Have a nice day.')
            break
        if answer == 'no' or answer == 'n':
            print("Then try again.")
            continue


    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("I don't have such a name in my database.")
        print("Do you want to add birthday information for " + name + "? Enter 'yes' or 'no' to answer")
        answer = input().lower()
        if answer == 'yes' or answer == 'y':
            print("What is " + name + "'s birthday?")
            bday = input()
            birthdays[name] = bday

            print("Birthday for " + name + ' updated.')
        elif answer == 'no' or answer == 'n':
            print("Ok.")




print("Thank you. See you next time!")