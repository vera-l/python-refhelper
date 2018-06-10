# coding: utf-8

import os
from datetime import datetime
from jinja2 import Template
from subprocess import call


TPL_PATH = 'report.tpl'
REPORT_DIR = '/tmp'
REPORT_FILENAME = 'report.html'
IDEA_API_URL = 'http://localhost:63342/api/file'

report_path = '{}/{}'.format(REPORT_DIR, REPORT_FILENAME)
TEMPLATE = Template(
    open(
        '{}/{}'.format(
            os.path.dirname(__file__),
            TPL_PATH
        ), 'r').read()
    )


def report(task_name, results, target_path):
    report_file = open(report_path, 'w')
    report_file.write(
        TEMPLATE.render(
            target_path=target_path,
            task=task_name,
            results=results,
            len=len(results),
            datetime=datetime.utcnow(),
            idea_url=IDEA_API_URL
        )
    )
    call(['open', report_path])
