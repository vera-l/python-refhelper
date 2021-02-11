import sys
from . import tasks
from . import finder
from .tasks import TASKS


AVAILABLE_TASKS = ' | '.join(TASKS.keys())


def get_target_path():
    if len(sys.argv) < 3:
        sys.exit(f'Execute: "pyrefhelper [path] [task={AVAILABLE_TASKS}]"')

    if sys.argv[2] not in tasks.TASKS:
        sys.exit(f'Task name is wrong. Available values is {AVAILABLE_TASKS}')

    return sys.argv[1], sys.argv[2]


def main():
    target_path, task_name = get_target_path()

    tasks.run(
        task_name,
        finder.get_py_files_list(target_path),
        target_path
    )
