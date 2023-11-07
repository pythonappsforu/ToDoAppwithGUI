import PySimpleGUI as sg
import todo_functions as tf
import time
import os

sg.theme('GreenMono')

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

clock = sg.Text(key='clock')
todo_label = sg.Text('Type in a todo:')
todo_input= sg.InputText(tooltip='Enter todo',key='todo_input')
add_button = sg.Button('Add',key='Add',size=10)
# add_button = sg.Button(key='Add',size=5,image_source='images/add.png',tooltip='Add Todo')
todo_listbox = sg.Listbox(values=tf.get_todos(),key="todos_listbox",
                          size=[45,10],enable_events=True)
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')



window = sg.Window(title="My ToDos",
                   layout=[[clock],[todo_label],[todo_input,add_button],
                           [todo_listbox,edit_button,complete_button],[exit_button]],
                   font= ('Courier 12',20))


while True:
    event,values = window.read(timeout=800)
    print(event)
    print(values)
    window['clock'].update(time.strftime('%b %d,%Y %H:%M:%S'))
    match event:
        case 'Add':
            todos_list = tf.get_todos()
            if values['todo_input'] == '':
                sg.popup('please enter a todo')
            else:
                new_todo = values['todo_input'] + "\n"
                todos_list.append(new_todo)
                tf.write_todos(todos_list)
                window['todos_listbox'].update(values=todos_list)
        case sg.WIN_CLOSED:
            break
        case 'Edit':
            try:
                selected_text = values['todos_listbox'][0]
                edit_value = values['todo_input']
                todos = tf.get_todos()
                index = todos.index(selected_text)
                todos[index] = edit_value + "\n"
                tf.write_todos(todos)
                window['todos_listbox'].update(values=todos)
            except IndexError:
                sg.Popup('Please select a todo to edit',font=('Courier 12',20))

        case 'Complete':
            try:
                selected_text = values['todos_listbox'][0]
                todos = tf.get_todos()
                todos.remove(selected_text)
                tf.write_todos(todos)
                window['todos_listbox'].update(values=todos)
                window['todo_input'].update(value='')
            except IndexError:
                sg.Popup('Please select a todo to mark complete',font=('Courier 12',20))


        case 'todos_listbox':
            selected_text = values['todos_listbox'][0]
            window['todo_input'].update(value=selected_text)

        case 'Exit':
            break




window.close()



