import os
import ast
from collections import namedtuple
import logging
from functools import partial

from . import reporter


ReportItem = namedtuple('ReportItem', 'file line column')
logger = logging.getLogger('file')

HTTP_METHODS = {'get_url', 'post_url', 'put_url', 'delete_url'}


def _has_callback_as_arg_or_keyword(node: ast.Call) -> bool:
    if len(node.args) > 9 and isinstance(node.args[9], ast.Name):
        return True

    for keyword in node.keywords:
        if keyword.arg == 'callback':
            return True

    return False


def _callback_matcher(node):
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in HTTP_METHODS
        and _has_callback_as_arg_or_keyword(node)
    )


NODE_MATCHERS = {
    'division': lambda node: isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div),
    'rounding': lambda node: isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'round',
    'callback': _callback_matcher,
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
        logger.debug(file_path)

        with open(file_path, 'r') as py_file:
            try:
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
            except Exception as e:
                logger.error(f'ERROR in {file_path}\n ---> {e}!')

    logger.warning(f'{50 * "-"}\nTask for {len(files)} files has been done')

    return result


TASKS = {
    'list': _py_list,
    'division': partial(_find_in_ast, NODE_MATCHERS['division']),
    'rounding': partial(_find_in_ast, NODE_MATCHERS['rounding']),
    'callback': partial(_find_in_ast, NODE_MATCHERS['callback']),
}


def run(task_name, files, target_path):
    if task_name not in TASKS:
        print('Task "{}" is not found'.format(task_name))

    results = TASKS[task_name](files, target_path)

    reporter.report(task_name, results, target_path)
