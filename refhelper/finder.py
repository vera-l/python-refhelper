import os


def get_py_files_list(dir_path, files=None):
    if files is None:
        files = []

    for some_path in os.listdir(dir_path):
        some_path = '{}/{}'.format(dir_path, some_path)
        if os.path.islink(some_path):
            continue

        if os.path.isfile(some_path) and some_path.endswith('.py'):
            files.append(some_path)

        if os.path.isdir(some_path):
            get_py_files_list(some_path, files)

    return files
