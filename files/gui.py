import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add") # this is a instance of add
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[35,10])
edit_Button=sg.Button("edit")

# This is an instance of a window(this is father of all the arguments which contains the list)
window = sg.Window('My To-Do app',
                   layout=[[label], [input_box, add_button],[list_box,edit_Button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "edit":
            todos_to_edit = values['todos'][0]
            new_todo = values['todo']

            todo = functions.get_todos()
            index = todo.index(todos_to_edit)
            todo[index] = new_todo
            functions.write_todos(todo)
            window['todos'].update(values=todo)
        case "sg.WIN_Closed":
            break

window.close()
