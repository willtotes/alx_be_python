
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case "medium":
        print(f"Reminder: {task} is a {priority} priority task that requires moderate attention")
    case "high":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input")


'''
if priority == "high":
    print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
elif priority == "medium":
    print(f"{task} is a {priority} priority task that requires moderate attention")
else:
    print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
'''