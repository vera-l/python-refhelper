import os
import ast
from collections import namedtuple
import logging
from functools import partial

from . import reporter


ReportItem = namedtuple('ReportItem', 'file line column')
logger = logging.getLogger('file')

NODE_MATCHERS = {
    'division': lambda node: isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div),
    'rounding': lambda node: isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'round',
}


def _py_list(files, target_path):
    result = []

    for a in files:
        result.append(
            ReportItem(
                file=os.path.relpath(a, target_path),
                line='-',
                column='-'
            )
        )

    return result


def _find_in_ast(node_mather, files, target_path):
    result = []

    for file_path in files:
        logger.error(file_path)

        with open(file_path, 'r') as py_file:
            ast_ = ast.parse(py_file.read())

            for node in ast.walk(ast_):
                if node_mather(node):
                    result.append(
                        ReportItem(
                            file=os.path.relpath(file_path, target_path),
                            line=node.lineno,
                            column=node.col_offset
                        )
                    )

    return result



TASKS = {
    'list': _py_list,
    'division': partial(_find_in_ast, NODE_MATCHERS['division']),
    'rounding': partial(_find_in_ast, NODE_MATCHERS['rounding']),
}


def run(task_name, files, target_path):
    if task_name not in TASKS:
        print('Task "{}" is not found'.format(task_name))

    results = TASKS[task_name](files, target_path)

    reporter.report(task_name, results, target_path)
