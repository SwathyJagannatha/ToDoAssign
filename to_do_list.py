#Module 2: Mini-project | To-Do list Application

from colorama import Fore, Back, Style
from termcolor import colored
from datetime import date

class TodoListStillEmptyException(Exception):
    "Raised when we are trying to access Empty List(ToDo List)"
    pass

class ValueNotFoundException(Exception):
    "Raised when we are trying to access ToDo List which is not present!!"
    pass

class InvalidOptionException(Exception):
    "Raised when the user provides invalid input when prompted to chose from the list!!"
    pass

class InvalidDateException(Exception):
    "Raised when the user provides invalid Date for the Due Date!!"
    pass

todo_list=[]
special_task=[]

# sort items based on priority -- requires use of dictionary

# def sort_items_priority(special_task):

#     priority_list={"Urgent":1,"High":2,"Medium":3,"Low":4}

#     sorted_list = sorted(special_task,key = lambda x : priority_list[x['user_priority']])

#     print("Sorted list contents:")
#     print(sorted_list)
   
#     pass
    
def add_task(todo_list):
    user_task = input("Enter the task you would like to append to the to-do list\n")

    if user_task in todo_list:
        print("Task already exists in your list!! You are trying to add a duplicate task!")
    else:
        todo_list.append(user_task)
        print("Todo List after adding the item:")
        print(colored(todo_list,on_color="on_green"))

def add_special_task(special_task):
    user_task = input("Enter the task you would like to add to special Task list\n")

    try:
        user_due_date = input("Enter the Task Due Date(YYYY-MM-DD)\n")
        user_priority = input("Enter the Task Priority (Low , Medium , High , Urgent!)\n")

        user_date = date.fromisoformat(user_due_date)
    
        if user_date < date.today():
           raise InvalidDateException
        else:
            task_item = user_task +" : " + str(user_date) +" : " + user_priority

            if task_item in special_task:
                print("Duplicate Entry! Task already exists in your special list!!")
            else:
                special_task.append(task_item)
                print("List after adding the item:")
                print(colored(special_task ,on_color="on_light_magenta"))

    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    except InvalidDateException:
            print("Please enter date in the future while setting Due date!")
   
    pass

def display_special_task(special_task):  
    for indi_task in special_task:
        task = indi_task.split(":")
        print("Displaying special task details:")
        print(f"""...............................................................................................................................
          {Fore.GREEN}Task -{Fore.YELLOW}{task[0]} : {Fore.GREEN}Due Date - {Fore.YELLOW}{task[1]} : {Fore.GREEN}Priority - {Fore.YELLOW}{task[2]} 
          """)
        print(Style.RESET_ALL)

    user_ip = input("Do you want to mark as special task complete?\n").lower()
    if user_ip == "yes":
         mark_complete(special_task)

         user_input = input("Do you want to delete any special task?\n").lower()
         if user_input == "yes":
            delete_sp_task(special_task)
    pass 

def mark_complete(special_task):
    print(special_task)
    user_input = input("Enter the special task, which has been completed\n").lower()

    for task in special_task:
        task_name,due_date,priority = task.split(":") 
    
        if task_name.lower().strip() == user_input.lower().strip(): 
            index_val = special_task.index(task)
            updated_task = task_name+"-XX"
            special_task[index_val] = ":".join([updated_task]+ task.split(":")[1:])

            #special_task[index_val] = updated_task + str(task.split(":")[1:])

            print(f"Task : {user_input} is Marked as Complete")
            print(f""".....Updated List Contents.........
                {Fore.GREEN}{special_task}
                """)
            print(Style.RESET_ALL)
            return
    print("Please enter an existing Task!!")
    pass 
                    
def delete_sp_task(special_task):
    print(special_task)
    user_input = input("Enter the special task, which you want to delete\n").lower()

    for task in special_task:
        task_name,due_date,priority = task.split(":") 
    
        if task_name.lower().strip() == user_input.lower().strip(): 
            special_task.remove(task) 

    print(f"List contents after special task {Fore.CYAN}{user_input} {Style.RESET_ALL} delete:\n")
    print(Style.RESET_ALL)
    display_special_task(special_task)
    pass

def view_task(todo_list):
    try:
        if not todo_list:
            raise TodoListStillEmptyException
        else:
            print("List val:",todo_list)
            for task_val in todo_list:
                print(f"{Fore.GREEN}Task : {Fore.RED}{task_val}")
                print(Style.RESET_ALL)
        
    except TodoListStillEmptyException:
        print("Sorry,the list is empty! Please add some tasks to populate!")

    finally:
         print("Hope you got to know the complete todo list details(empty or populated)!")
         pass

def delete_task(todo_list):
    try:
        user_in = input("Enter the name of the task you wanna delete?")
        if user_in not in todo_list:
            raise ValueNotFoundException
        elif not todo_list:
            raise TodoListStillEmptyException
        
    except ValueNotFoundException:
        print("Sorry,the task cannot be found! Please provide an existing task!")

    except TodoListStillEmptyException:
        print("Sorry,the list is empty! Please add some tasks to populate!")

    else:
        todo_list.remove(user_in) 
        print(f"Congrats, The task {Fore.RED} {user_in} {Style.RESET_ALL} has been successfully deleted!! ")
        print(f"List contents after delete operation:{Fore.CYAN}{todo_list}")
        print(Style.RESET_ALL)
    pass

def update_task(todo_list):
    try:
         if not todo_list:
            raise TodoListStillEmptyException
         else:
            user_task = input("Enter the task you would like to Mark as Completed!")
            if user_task in todo_list:
                for idx,task in enumerate(todo_list):
                    if task == user_task:
                        todo_list[idx]+="-X"
            else:
                raise ValueNotFoundException

    except TodoListStillEmptyException:
         print("Sorry,the list is empty! Please add some tasks for you to carry on update operation!")

    except ValueNotFoundException:
        print("Sorry,the task cannot be found! Please provide an existing task!")

    except Exception as e:
        print(f"Unexpected Error occured: {e}")
    else:
        print("Good job!! You completed the task!")
        for task in todo_list:
            if 'X' in task:
                print(f"{Fore.WHITE}COMPLETED TASK:")
                print(Style.RESET_ALL)
                print(f"{Fore.LIGHTYELLOW_EX}Task - {Fore.LIGHTGREEN_EX}{task}")
                print(Style.RESET_ALL)
            else:
            #print(f"{Fore.RED}This text is red!{Fore.WHITE}")
                print(f"{Fore.LIGHTYELLOW_EX}Task-{Fore.LIGHTRED_EX}{task}")
                print(Style.RESET_ALL)

def main(todo_list):
    print(""" 
        Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Add Special Task ,Display Special Tasks, Mark that task as Completed
        6. Quit

    """)

    while True:
        try:
            choice = input("Hello there!! Please input your choice:\n")
            if choice == "1":
                add_task(todo_list)
    
            elif choice == "2":
                view_task(todo_list)

            elif choice == "3":
                update_task(todo_list)
                print("Your To-Do list after updating Task as complete:\n")
                print(todo_list)

            elif choice == "4":
                user_ip = input("Are you sure you want to delete the task?\n")
                if user_ip == "yes": 
                    delete_task(todo_list)
                    print("Your list after deletion:")
                    print(todo_list)
                else:
                    print("You have changed your mind!!The list remains intact!")
                    print(todo_list)
            elif choice == "5":
                user_ip = input("Do you want to add tasks with Priorities,Due Date\n").lower()
                if user_ip == "yes":
                    add_special_task(special_task)
                    user_val =input("Do you want to view the special tasks?\n").lower()
                    if user_val == "yes":
                        display_special_task(special_task)
                        
            # elif choice == "6":
            #     sort_items_priority(special_task)
            #     display_special_task(special_task)

            elif choice == "6":
                    print("You have chosen to quit!!Exiting.....")
                    break
            else: 
                raise InvalidOptionException
            
        except InvalidOptionException:
            print("Please choose a valid option between 1 to 6")

main(todo_list)


############ dictionary implementation ###################

# def add_special_task(special_task):
#     user_task = input("Enter the task you would like to add to special Task list\n")

#     try:
#         user_due_date = input("Enter the Task Due Date(YYYY-MM-DD)\n")
#         user_priority = input("Enter the Task Priority (Low , Medium , High , Urgent!)\n")

#         user_date = date.fromisoformat(user_due_date)
    
#         if user_date < date.today():
#            raise InvalidDateException
#         else:
#             #task_item = user_task +" : " + str(user_date) +" : " + user_priority
#             task_item = {'task': user_task, 'due_date': str(user_date), 'priority': user_priority.strip()}

#             if task_item in special_task:
#                 print("Duplicate Entry! Task already exists in your special list!!")
#             else:
#                 special_task.append(task_item)
#                 print("List after adding the item:")
#                 print(colored(special_task ,on_color="on_light_magenta"))

#     except ValueError:
#         print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

#     except InvalidDateException:
#             print("Please enter date in the future while setting Due date!")
   
#     pass

# def display_special_task(special_task):  
#     for task in special_task:
#         #task = indi_task.split(":")
#         print("Displaying special task details:")
#         print(f"""...............................................................................................................................
#           {Fore.GREEN}Task -{Fore.YELLOW}{task['task']} : {Fore.GREEN}Due Date - {Fore.YELLOW}{task['due_date']} : {Fore.GREEN}Priority - {Fore.YELLOW}{task['priority']} 
#           """)
#         print(Style.RESET_ALL)

#     user_ip = input("Do you want to mark as special task complete?\n").lower()
#     if user_ip == "yes":
#          mark_complete(special_task)

#          user_input = input("Do you want to delete any special task?\n").lower()
#          if user_input == "yes":
#             delete_sp_task(special_task)
#          else:
#             pass
#     pass 

# def mark_complete(special_task):
#     print(special_task)
#     user_input = input("Enter the special task, which has been completed\n").lower()
#     for task in special_task:
#         task_name = task['task']
#         print(task_name)
#         if task_name.lower().strip() == user_input.lower().strip():
#                 task['task'] +='-XX'
#                 print(special_task)
#         else:
#             print("Task names arent matching!")

#     display_special_task(special_task)
#     pass 

# sort items based on due date or priority
# def sort_items_priority(special_task):

#     priority_list={"Urgent":1,"High":2,"Medium":3,"Low":4}

#     sorted_list = sorted(special_task,key = lambda x : priority_list[x['priority']])

#     print("Sorted list contents:")
#     #print(sorted_list)
#     for task in sorted_list:
#         print(f"{Fore.LIGHTRED_EX}Task - {Fore.BLUE}{task['task']} : {Fore.LIGHTRED_EX}Due Date - {Fore.BLUE}{task['due_date']} : {Fore.LIGHTRED_EX}Priority - {Fore.BLUE}{task['priority']}")
#     pass

