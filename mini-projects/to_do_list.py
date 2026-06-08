def tasks():
    tasks =[]
    print("----Welcome to your To-Do List----")
    total_tasks = int(input("How many tasks do you want to add = "))
    for i in range(total_tasks):
        task = input("Enter task:")
        tasks.append(task)
    print(f"Your today's tasks are: {tasks}")
    while True:
        operation = int(input("Do you want to add or remove a task? (1 for add, 2 for remove, 3 for update, 4 for exit)"))
        if operation ==1:
            new_task = input("Enter new task:")
            tasks.append(new_task)
            print(f"Now your today's tasks are : {tasks}")
        elif operation == 2 :
            remove_task = input("Enter task to remove:")
            if remove_task in tasks:
                tasks.remove(remove_task)
                print(f"Now your today's tasks are : {tasks}")
            else:
                print("Task not found in the list.")
        elif operation == 3:
            old_task = input("Enter task to update:")
            if old_task in tasks:
                new_task = input ("Enter new task:")
                index = tasks.index(old_task)
                tasks[index]= new_task
                print(f"Now your today's tasks are : {tasks}")
        else:
            print("Exiting the To-Do List. Have a productive day!")
            break   
tasks()



