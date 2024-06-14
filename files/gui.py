import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")  # this is a instance of add

# This is an instance of a window(this is father of all the arguments which contains the list)
window = sg.Window('My To-Do app',
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "sg.WIN_Closed":
            break

window.close()
