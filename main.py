print("This program helps you create and maintain a todo list ")
print("How to use?")
print("To show list: Type show")
print("To add: Type add <todo item>")
print("To edit:Type edit <item number>")
print("to mark complete:Type complete <item number>")
print("to exit the list:Just Type <exit>")

user_prompt = "What action would you like to perform? "
todos = []

import functions
import time

now = time.strftime("%b,%d,%Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        todos = functions.get_todos()
        # todos.txt is the argument of the parameter

        todos.append(todo + '\n')

        functions.write_todos("todos.txt", todos)
        # this todos is actually a list the value will be assigned to todos_arg

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        number = int(user_action[5:])
        print(number)

        number = number - 1

        todos = functions.get_todos()

        new_todo = input("Enter new Todo:")
        todos[number] = new_todo + '\n'

        write_todos = ("todos.txt", todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        todos = functions.get_todos()

        todos.pop(number - 1)
        functions.write_todos = ("todos.txt", todos)

    elif user_action.startswith('exit'):
        break
    else:
        print("No output")
