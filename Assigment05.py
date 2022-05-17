# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PMcGiffin, 5.14.22, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

try:
    objToDoList = open(objFile, "r")
    for row in objToDoList:
        task, priority = row.split(",")
        dicRow = {"Task": task.strip(), "Priority": priority.strip()}
        lstTable.append(dicRow)
    objToDoList.close()
except:
    print("This task has not been created.  Follow directions to create a new task.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
       print("TASK", "|", "PRIORITY")
       for row in lstTable:
           print(row["Task"] + " " + "|" + " " + row["Priority"])
           continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("Enter a task: ")
        priority = input("\nEnter a priority: ")
        lstTable.append({"Task": task, "Priority": priority})
        print("Task has been added to list")
        continue
    # Step 5 - Remove a item from the list/Table
    elif (strChoice.strip() == '3'):
        deltask = input("What task would you like to delete?")
        for row in lstTable:
            if row["Task"].lower() == deltask.lower():
                lstTable.remove(row)
                print("This task has been deleted")
            else:
                print("This task does not exist.")
        continue


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('ToDoList.txt', 'a')
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str((row["Priority"], "\n")))
        objFile.close()
        print("Your new task has been saved")
        continue
        # TODO: Add Code Here

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
