medical = input("Do you have a medical cause? Y/N:" ).upper().strip()

if medical == "Y":
    print("You are free to take the exam")
else: 
    attendance = int(input("Enter your attendance: "))
    if attendance >= 75:
        print("You can take the exam")
    else: 
        print("You cannot take the exam")