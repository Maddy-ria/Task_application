# task_manager.py

class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date):
        task = Task(title, due_date)
        self.tasks.append(task)

    def list_tasks(self):
        for index, task in enumerate(self.tasks, 1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index}. {task.title} (Due: {task.due_date}) - {status}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.mark_completed()
            print(f"Task '{task.title}' marked as completed.")
        else:
            print("Invalid task index.")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            due_date = input("Enter due date: ")
            task_manager.add_task(title, due_date)
            print("Task added successfully.")
        elif choice == "2":
            print("Tasks:")
            task_manager.list_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            task_manager.mark_task_completed(task_index)
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
