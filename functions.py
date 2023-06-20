FILEPATH = r'C:\Python\To-Do List App\todos.txt'

def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list of to-do items """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
