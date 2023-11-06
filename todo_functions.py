FILEPATH = "todos.txt"


def get_todos():
    with open(FILEPATH,'r') as file:
        return file.readlines()

def write_todos(todos):
    with open(FILEPATH,'w') as file:
        return file.writelines(todos)


if __name__ == '__main__':
    write_todos("todo")
    get_todos()