# Udemy python course to-do-app
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f'It is {now}')
while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.capitalize()
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            edit = int(user_action[5:])
            edit = edit - 1

            todos = functions.get_todos()

            new_todo = input('Enter new to-do: ')
            try:
                todos[edit] = new_todo + '\n'

                functions.write_todos(todos)

            except IndexError:
                print(f'Number {(edit + 1)}, is not in the list!')
                continue
        except ValueError:
            print('Your command is not valid!')
            continue

    elif user_action.startswith('complete'):
        try:
            try:
                complete = int(user_action[9:])

                todos = functions.get_todos()
                todo_to_remove = todos[complete - 1].strip('\n')
                todos.pop(complete - 1)

                functions.write_todos(todos)

                message = f"Todo {todo_to_remove} was removed from the list!"
                print(message)
            except ValueError as e:
                print(f"expecting integer: {e}")
                continue
        except IndexError or ValueError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Not a valid input!')
# test