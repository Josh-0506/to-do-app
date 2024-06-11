import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo")
add_button=sg.Button("Add")# this is a instance of add

# This is an instance of a window(this is father of all the arguments which contains the list)
window = sg.Window('My To-Do app',layout=[[label],[input_box,add_button]])

window.read()
window.close()
