import os

FILE_PATH = 'todo_list.txt'

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return [line.strip() for line in file]

def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def update_task(index, new_task):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1] = new_task
        save_tasks(tasks)
        print(f"Task updated: {new_task}")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. List tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            list_tasks()
        elif choice == '2':
            task = input("Enter the new task: ")
            add_task(task)
        elif choice == '3':
            list_tasks()
            index = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            update_task(index, new_task)
        elif choice == '4':
            list_tasks()
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

