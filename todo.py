tasks=[]


def addTask():
    task=input("Please Enter a task: ")
    tasks.append(task)
    print(f"task '{task}' added to llist. ")


def listTask():
    if not tasks:
        print("Thre are No task currently. ")
    else:
        print("Current Tasks are:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deletetask():
  listTask()
  try:
    taskToDelete = int(input("Enter the #  to delete: "))
    if taskToDelete >=0 and taskToDelete < len(tasks):
        tasks.pop(taskToDelete)
        print(f"Task{taskToDelete} has been removed. ")
    else:
        print(f"Task #{taskToDelete} was not found!!")

  except:
    print("Invalid Input")

if __name__ == "__main__":
  print("Welcome to TO DO tsk using Pyhton ")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("-------------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if(choice=="1"):
        addTask()

    elif(choice=="2"):
        deletetask()

    elif(choice=="3"):
        listTask()

    elif(choice=="4"):
      break
    else:
        print("Invalid input. please try again.")

print("Good Bye!!!!")
