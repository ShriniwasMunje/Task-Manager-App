import functions
import time

now = time.strftime("%d/%b/%Y %H:%M:%S")
print("It's", now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
            todo = user_action[4:]

            todos = functions.get_todos("todos.txt")

            todos.append(todo + "\n")

            functions.write_todos("todos.txt", todos)

    elif user_action.startswith('show'):
        with open('todos.txt') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1}: {item.strip("\n").capitalize()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos("todos.txt", todos)

        except ValueError:
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos("todos.txt")

            todos.pop(number - 1)

            functions.write_todos("todos.txt", todos)

        except IndexError:
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command")

print("Good Luck with your List!")