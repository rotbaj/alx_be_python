# Prompt user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' is a task with unspecified priority"

# Add time sensitivity to the message
if time_bound == "yes":
    reminder = f"{base_message} that requires immediate attention today!"
else:
    reminder = f"{base_message}. Consider completing it when you have free time."

# Output the reminder
print(f"Reminder: {reminder}")
