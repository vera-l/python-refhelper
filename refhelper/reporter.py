import os
from datetime import datetime
from jinja2 import Template
from subprocess import call

from .version import version


TPL_PATH = 'report.tpl'
REPORT_DIR = '/tmp'
REPORT_FILENAME = 'report.html'
IDEA_API_URL = 'http://localhost:63342/api/file'

report_path = '{}/{}'.format(REPORT_DIR, REPORT_FILENAME)
template_path = '{}/{}'.format(os.path.dirname(__file__), TPL_PATH)

with open(template_path, 'r') as template_file:
    TEMPLATE = Template(template_file.read())


def report(task_name, results, target_path):
    with open(report_path, 'w') as report_file:
        report_file.write(
            TEMPLATE.render(
                target_path=target_path,
                task=task_name,
                results=results,
                len=len(results),
                datetime=datetime.utcnow(),
                version=version,
                idea_url=IDEA_API_URL,
            )
        )
    call(['open', report_path])
