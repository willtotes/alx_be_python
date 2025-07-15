
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


'''
if priority == "high" and time_bound == "yes":
    print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
elif priority == "high" and time_bound == "no":
    print(f"Reminder: {task} is a {priority} priority task with a flexible schedule. Plan carefully.")
elif priority == "medium" and time_bound == "yes":
    print(f"Reminder: {task} is a {priority} priority task that requires high attention.")
elif priority == "medium" and time_bound == "no":
    print(f"Reminder: {task} is a {priority} priority task with a flexible schedule.")
elif priority == "low" and time_bound == "yes":
    print(f"Note: {task} is a {priority} priority task but has a deadline.")
elif priority == "low" and time_bound == "no":
    print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
else:
    print(f"Invalid input!!!")
'''


match priority, time_bound:
    case "high", "yes":
        print(f"Reminder: {task} is a {priority} priority task that requires immerdiate attention today!")
    case "high", "no":
        print(f"Reminder: {task} is a {priority} priority with a flexible schedule. Plan carefully.")
    case "medium", "yes":
        print(f"Reminder: {task} is a {priority} priority tasl that requires high attention.")
    case "medium", "no":
        print(f"Reminder: {task} is a {priority} priority with a flexible schedule.")
    case "low", "yes":
        print(f"Reminder: {task} is a {priority} priority but has a deadline.")
    case "low", "no":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input!!!")
    
    
