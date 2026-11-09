#Importing the functions and GUI Interface Module

import functions as fn
import FreeSimpleGUI as sg
import time

theme= sg.theme("DarkGrey4")
#Detailing the UI as to how we want it to look and which controls we want to have
clock = sg.Text('', key='clock')
label = sg.Text("Type a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do", key = "todo")
button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todos(), key = "todos",enable_events=True, size=(25,7))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit", size=30)

#Creating a UI Window
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label], [input_box, button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Cooper", 10))



while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%d/%m/%Y %H:%M:%S"))

    match event:
        case"Add":
            todos = fn.get_todos()
            new_todo = values['todo'].capitalize() + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                fn.write_todos(todos)

                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Cooper", 10))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = fn.get_todos()
                todos.remove(todo_to_complete)
                fn.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Cooper", 10))
        case 'todos':
            window["todo"].update(value=values["todos"][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break



window.close()