class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task added: {title}")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks yet!")
            return
        
        print("\nYour Tasks:")
        print("-" * 40)
        for index, task in enumerate(self.tasks, 1):
            status = "✓" if task.completed else " "
            print(f"{index}. [{status}] {task.title}")
            if task.description:
                print(f"   {task.description}")
        print("-" * 40)

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.completed = True
            print(f"Marked complete: {task.title}")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {task.title}")
        else:
            print("Invalid task number!")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Quit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter description (optional): ")
            todo_list.add_task(title, description)
            
        elif choice == "2":
            todo_list.view_tasks()
            
        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter task number to complete: "))
                todo_list.complete_task(task_num)
            except ValueError:
                print("Please enter a valid number!")
            
        elif choice == "4":
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_num)
            except ValueError:
                print("Please enter a valid number!")
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
