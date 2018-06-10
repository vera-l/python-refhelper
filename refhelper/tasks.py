# coding: utf-8

import os
import ast
from collections import namedtuple
import reporter


ReportItem = namedtuple('ReportItem', 'file line column')

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

def _division(files, target_path):
    result = []

    for a in files:
        ast_ = ast.parse(open(a, 'r').read())

        for node in ast.walk(ast_):
            if isinstance(node, ast.BinOp):
                if not isinstance(node.op, ast.Div):
                    continue

                result.append(
                    ReportItem(
                        file=os.path.relpath(a, target_path),
                        line=node.lineno,
                        column=node.col_offset
                    )
                )

    return result

def _rounding(files, target_path):
    result = []

    for a in files:
        ast_ = ast.parse(open(a, 'r').read())

        for node in ast.walk(ast_):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id != 'round':
                        continue

                    result.append(
                        ReportItem(
                            file=os.path.relpath(a, target_path),
                            line=node.lineno,
                            column=node.col_offset
                        )
                    )

    return result

TASKS = {
    'list': _py_list,
    'division': _division,
    'rounding': _rounding
}

def run(task_name, files, target_path):
    if task_name not in TASKS:
        print 'Task "{}" is not found'.format(task_name)

    results = TASKS[task_name](files, target_path)

    reporter.report(task_name, results, target_path)
