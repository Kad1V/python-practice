import json


def add_task(tasks: list, title: str) -> None:
    tasks.append({"title": title, "done": False})


def list_tasks(tasks: list) -> None:
    if tasks:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['title']} - {status}")
    else:
        print("No tasks added yet!\n")


def mark_done(tasks: list, task_number: int) -> bool:
    if task_number < 1 or task_number > len(tasks):
        return False
    tasks[task_number - 1]["done"] = True
    return True


def delete_task(tasks: list, task_number: int) -> bool:
    if task_number > 0 and task_number <= len(tasks):
        tasks.pop(task_number - 1)
        return True
    else:
        return False


def save_tasks(tasks: list) -> None:
    with open("to_do.json", "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks() -> list:
    try:
        with open("to_do.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def main():
    tasks = load_tasks()
    while True:
        try:
            selected_option = int(
                input(
                    "\nSelect an option:\n\n"
                    "1. Add Task\n"
                    "2. Delete Task\n"
                    "3. List Tasks\n"
                    "4. Mark task as done\n"
                    "5. Quit\n\n"
                    "Enter your choice: "
                )
            )
            if selected_option == 5:
                save_tasks(tasks)
                break
            elif selected_option == 1:
                title = input("Add your task: ").strip()
                if title:
                    add_task(tasks, title)
                    save_tasks(tasks)
                    print("Task added successfully!\n")
                else:
                    print("Task title cannot be empty.\n")
            elif selected_option == 2:
                delete_no = int(
                    input("Enter the task number that you want to delete: ")
                )
                delete_check = delete_task(tasks, delete_no)
                if delete_check:
                    save_tasks(tasks)
                    print("Task deleted successfully!\n")
                else:
                    print("!!Enter a valid task number!!\n")
            elif selected_option == 3:
                list_tasks(tasks)
            elif selected_option == 4:
                completed_task_no = int(input("Enter the task number that is done: "))
                done_check = mark_done(tasks, completed_task_no)
                if done_check:
                    save_tasks(tasks)
                    print("Task completed successfully!\n")
                else:
                    print("!!Enter a valid task number!!\n")
            else:
                print("!!Invalid Option!!\n")
        except ValueError:
            print("!!Use a valid number!!\n")


if __name__ == "__main__":
    main()
