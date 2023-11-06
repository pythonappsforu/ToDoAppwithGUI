import PySimpleGUI as sg
import todo_functions as tf

todo_label = sg.Text('Type in a todo:')
todo_input= sg.InputText(tooltip='Enter todo',key='todo_input')
add_button = sg.Button('Add')
todo_listbox = sg.Listbox(values=tf.get_todos(),key="todos_listbox",
                          size=[45,10],enable_events=True)
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')


window = sg.Window(title="My ToDos",
                   layout=[[todo_label],[todo_input,add_button],
                           [todo_listbox,edit_button,complete_button],[exit_button]],
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
            window['todos_listbox'].update(values=todos_list)
        case sg.WIN_CLOSED:
            break
        case 'Edit':
            selected_text = values['todos_listbox'][0]
            edit_value = values['todo_input']
            todos = tf.get_todos()
            index = todos.index(selected_text)
            todos[index] = edit_value + "\n"
            tf.write_todos(todos)
            window['todos_listbox'].update(values=todos)
        case 'Complete':
            selected_text = values['todos_listbox'][0]
            todos = tf.get_todos()
            todos.remove(selected_text)
            tf.write_todos(todos)
            window['todos_listbox'].update(values=todos)
            window['todo_input'].update(value='')


        case 'todos_listbox':
            selected_text = values['todos_listbox'][0]
            window['todo_input'].update(value=selected_text)

        case 'Exit':
            break




window.close()



