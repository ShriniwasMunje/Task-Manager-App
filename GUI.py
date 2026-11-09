import functions as fn

import FreeSimpleGUI as sg

label = sg.Text("Type a To-Do")
input_box = sg.InputText(tooltip="Enter a To-Do", key = "todo")
button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todos(), key = "todos",enable_events=True, size=(25,15))
edit_button = sg.Button("Edit")


window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, button], [list_box, edit_button],],
                   font=("Helvetica", 15))

while True:
    event, values = window.read()

    match event:
        case"Add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = fn.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            fn.write_todos(todos)
            window["todos"].update(values=todos)

        case 'todos':
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break



window.close()