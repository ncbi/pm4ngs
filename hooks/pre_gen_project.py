import re
import sys
from cookiecutter.main import cookiecutter

PROJECT_REGEX = r'^[\-_a-zA-Z0-9]+$'

PROJECT_NAME = '{{ cookiecutter.project_name }}'

if not re.match(PROJECT_REGEX, PROJECT_NAME):
    print('ERROR: %s is not a valid PROJECT name!' % PROJECT_NAME)

    # exits with status 1 to indicate failure
    sys.exit(1)

