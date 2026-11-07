def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(file_path, todos_arg):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)