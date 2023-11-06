import PySimpleGUI as sg
import todo_functions as tf

todo_label = sg.Text('Type in a todo:')
todo_input= sg.InputText(tooltip='Enter todo',key='todo_input')
add_button = sg.Button('Add')

window = sg.Window(title="My ToDos",
                   layout=[[todo_label],[todo_input,add_button]],
                   font= ('Courier 12',20))


while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos_list = tf.get_todos()
            new_todo = values['todo_input'] + "\n"
            todos_list.append(new_todo)
            tf.write_todos(todos_list)
        case sg.WIN_CLOSED:
            break

window.close()



