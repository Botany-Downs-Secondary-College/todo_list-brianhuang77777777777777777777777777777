modes = ["Add a task", "View List", "Exit"]
tasks = []


def mode_select():
    print("\nChoose a mode by entering the number:")
    for i in range(3):
        print("%s : %s" % (i + 1, modes[i]))
    select = input("")
    if select == "1":
        add_tasks()
    elif select == "2":
        print("\nHere is your todo list:")
        for i in tasks:
            print("- %s" % (i))
        mode_select()
    elif select == "3":
        exit()
    else:
        print("Please input a valid number")
        mode_select()


def add_tasks():
    while True:
        task = input("Enter the task or type 'end' to return to menu: ")
        if task != "end":
            tasks.append(task)
            continue
        break
    mode_select()


mode_select()
