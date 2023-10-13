tasks = []
def addTask(taskName, dueDate):
    if taskName not in tasks:
        tasks[taskName] = dueDate
        print(f"Task '{taskName}' added with due date {dueDate}.")
    else:
        print(f"Task '{taskName}' already exists.")
def removeTask(taskName):
    if taskName in tasks:
        del tasks[taskName]
        print(f"Task '{taskName}' removed.")
    else:
        print(f"Task '{taskName}' not found.")
def listTasks():
    if tasks:
        print("Tasks:")
        for task, dueDate in tasks.items():
            print(f" - {task} (Due: {dueDate})")
    else:
        print("You have no tasks.")
while True:
    print("To-Do List")
    print("Add Task")
    print("Remove Task")
    print("Show Tasks")
    print("Close")
    choice = input("Enter your choice (Add/Remove/Show/Close): ").lower()
    if choice == "add":
        taskName = input("Enter task name: ")
        dueDate = input("Enter due date: ")
        addTask(taskName, dueDate)
    elif choice == "remove":
        taskName = input("Enter task name to remove: ")
        removeTask(taskName)
    elif choice == "show":
        listTasks()
    elif choice == "close":
        break
    else:
        print("Invalid choice, please choose either Add/Remove/Show/Close")