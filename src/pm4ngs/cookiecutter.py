import json
import os

import yaml
from cookiecutter.exceptions import FailedHookException, OutputDirExistsException
from cookiecutter.main import cookiecutter


def execute_cookiecutter(template, config_file, sample_table, copy_rawdata):
    extra_context = {
        'default_context': {}
    }
    no_input = False
    if config_file:
        print('Using config file: {}'.format(config_file))
        with open(config_file) as file:
            extra_context = yaml.load(file, Loader=yaml.FullLoader)
            print(json.dumps(extra_context['default_context'], indent=4))
            no_input = True
    if os.path.exists(sample_table):
        os.environ['PM4NGS_SAMPLE_TABLE'] = os.path.abspath(sample_table)
        os.environ['PM4NGS_COPY_RAWDATA'] = str(copy_rawdata)
        os.environ['PM4NGS_WORK_DIR'] = os. getcwd()
        try:
            cookiecutter(template,
                         no_input=no_input,
                         extra_context=extra_context['default_context'])
        except FailedHookException as e:
            print(e)
        except OutputDirExistsException as e:
            print(e)
    else:
        print('Sample table file {} not found.'.format(sample_table))
