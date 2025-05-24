tasks = []
def create_task(task):
    tasks.append(task)
    
def view_task(): 
    for i, task in enumerate (tasks, start = 1):
        print(f"{i}. {tasks}")
 
def delete_task(tasknumber):
    try:
        tasks[tasknumber - 1]
    except IndexError:
        print("invalid..")

while True:
    print("Enter 1. for add Task")
    print("Enter 2. for View Task") 
    print("Enter 3 for Remove Task") 
    print("Enter 4 for Quit")
    taskk = input("Enter your task number: ")
    if taskk == "1":
        task = input("Enter your Task: ")
        create_task(task)
    elif taskk == "2":
        view_task()
    elif taskk == "3":
        tasknumber = int(input("Enter the task number to remove: "))
        delete_task(tasknumber)
    elif taskk == "4":
        break
    else:
        print("invalid choice.. Please choose correct option(1, 2, 3, 4)")
print("Exisiting todo list app..")