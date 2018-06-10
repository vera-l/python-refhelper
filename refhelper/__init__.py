# coding: utf-8

import sys
import tasks
import finder


def get_target_path():
    if len(sys.argv) < 3:
        sys.exit('Call format is "pyrefhelper [path] [task=list|division|rounding]"')

    if sys.argv[2] not in tasks.TASKS:
        sys.exit('Task name is wrong. Available values is "list" and "division"')

    return sys.argv[1], sys.argv[2]

def main():
    target_path, task_name = get_target_path()

    tasks.run(
        task_name,
        finder.get_py_files_list(target_path),
        target_path
    )
