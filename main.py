class ToDo():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Unfinished"})
    
    def add_multi_tasks(self, tasks):
        l_tasks = tasks.split(',')
        for task in l_tasks:
            self.add_task(task.strip())

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["status"] = "Completed"
                break

    def clear_all(self):
        self.tasks = []     

#console exect

todo_list = ToDo()
while True:
    print("1. Add Task")
    print("2. Add Multiple Tasks")
    print("3. List Tasks")
    print("4. Mark Task as Completed")
    print("5. Clear all Tasks")
    print("6. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.add_task(task)
    elif choice == '2':
        tasks = input("Enter multiple tasks separated by ',' ")
        todo_list.add_multi_tasks(tasks)
    elif choice == '3':
        tasks = todo_list.list_tasks()
        for t in tasks:
            print(f"{t['task']} - {t['status']}")
    elif choice == '4':
        task = input("Enter task to mark as completed: ")
        todo_list.complete_task(task)
    elif choice == '5':
        todo_list.clear_all()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
   