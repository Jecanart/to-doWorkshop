class ToDo():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Unfinished"})
    
    def add_multi_tasks(self, tasks):
        l_tasks = tasks.split(';')
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