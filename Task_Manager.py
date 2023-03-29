class Task:
    def __init__(self, description):
        self.description = description
        self.is_complete = False

    def toggle_completion(self):
        self.is_complete = not self.is_complete

    def __str__(self):
        return f"{self.description} {'(Complete)' if self.is_complete else '(Incomplete)'}"
    

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        new_task = Task(task_description)
        self.tasks.append(new_task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")

    def toggle_task_completion(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].toggle_completion()


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Toggle Task Completion")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == 2:
            task_index = int(input("Enter task index: "))
            task_manager.remove_task(task_index)
        elif choice == 3:
            task_manager.view_tasks()
        elif choice == 4:
            task_index = int(input("Enter task index: "))
            task_manager.toggle_task_completion(task_index)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
