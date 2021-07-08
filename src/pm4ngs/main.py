#!/usr/bin/env python
import argparse
import os
import subprocess

import requests

from pm4ngs import __version__
from pm4ngs.cookiecutter import execute_cookiecutter

PIPELINES = {
    1: {
        'name': 'RNA-Seq',
        'url': 'https://github.com/ncbi/pm4ngs-rnaseq',
        'example_yml':
            'https://raw.githubusercontent.com/ncbi/pm4ngs-rnaseq/master'
            '/example/pm4ngs_rnaseq_demo_config.yaml',
        'sample_sheet':
            'https://raw.githubusercontent.com/ncbi/pm4ngs-rnaseq/master'
            '/example/pm4ngs_rnaseq_demo_sample_data.csv'
    },
    2: {
        'name': 'ChIP-Seq',
        'url': 'https://github.com/ncbi/pm4ngs-chipseq',
        'example_yml':
            'https://raw.githubusercontent.com/ncbi/pm4ngs-chipseq/master'
            '/example/pm4ngs_chipseq_demo_config.yaml',
        'sample_sheet':
            'https://raw.githubusercontent.com/ncbi/pm4ngs-chipseq/master'
            '/example/pm4ngs_chipseq_demo_sample_data.csv'
    },
    3: {
        'name': 'ChIP-exo',
        'url': 'https://github.com/ncbi/pm4ngs-chipexo',
        'example_yml':
            'https://raw.githubusercontent.com/ncbi/pm4ngs-chipexo/master'
            '/example/pm4ngs_chipexo_demo_config.yaml',
        'sample_sheet':
            'https://raw.githubusercontent.com/ncbi/pm4ngs-chipexo/master'
            '/example/pm4ngs_chipexo_demo_sample_data.csv'
    },
    4: {
        'name': 'Transcriptome-Annotation',
        'url': 'https://github.com/ncbi/pm4ngs-transcriptome-annotation',
        'example_yml':
            'https://raw.githubusercontent.com/ncbi/pm4ngs-transcriptome-annotation/master'
            '/example/pm4ngs_transcriptome_demo_config.yaml',
        'sample_sheet':
            'https://raw.githubusercontent.com/ncbi/pm4ngs-transcriptome-annotation/master'
            '/example/pm4ngs_transcriptome_demo_sample_data.csv'
    }
}


def command_line(pipeline, is_general=False):
    if pipeline > 0:
        description = 'Generate a PM4NGS project for {} data analysis'.format(
            PIPELINES[pipeline]['name'])
    else:
        description = 'Generate a PM4NGS project from cookiecutter template'
    parser = argparse.ArgumentParser(description)

    parser.add_argument('-v', '--version', action='version',
                        version='PM4NGS version: {}'.format(__version__))
    parser.add_argument('--sample-sheet',
                        help='Sample sheet CSV file with columns: '
                             'sample_name,file,condition,replicate',
                        required=True)
    parser.add_argument('--config-file',
                        help='User configuration file with project description',
                        required=False)
    parser.add_argument('--copy-rawdata',
                        help='Copy the raw data defined in the sample table '
                             'to the project/data/DATASET folder',
                        action='store_true',
                        required=False)

    if is_general:
        parser.add_argument('--template',
                            help='PM4NGS cookiecutter template',
                            required=True)
    args = parser.parse_args()
    return args


def rnaseq():
    create_predefined(1)


def rnaseq_demo():
    generate_demo(1)


def chipseq():
    create_predefined(2)


def chipseq_demo():
    generate_demo(2)


def chipexo():
    create_predefined(3)


def chipexo_demo():
    generate_demo(3)


def transcriptome_annotation():
    create_predefined(4)


def transcriptome_annotation_demo():
    generate_demo(4)


def create_predefined(pipeline):
    args = command_line(pipeline)
    print('Generating {} data analysis project'.format(
        PIPELINES[pipeline]['name']))
    execute_cookiecutter(PIPELINES[pipeline]['url'], args.config_file,
                         args.sample_sheet, args.copy_rawdata)


def generate_demo(pipeline):
    print('Generating demo for {} data analysis project'.format(
        PIPELINES[pipeline]['name']))
    config_file = os.path.basename(PIPELINES[pipeline]['example_yml'])
    print('Downloading file: ' + config_file)
    r = requests.get(PIPELINES[pipeline]['example_yml'], allow_redirects=True)
    open(config_file, 'wb').write(r.content)
    sample_sheet = os.path.basename(PIPELINES[pipeline]['sample_sheet'])
    print('Downloading file: ' + sample_sheet)
    r = requests.get(PIPELINES[pipeline]['sample_sheet'], allow_redirects=True)
    open(sample_sheet, 'wb').write(r.content)
    execute_cookiecutter(PIPELINES[pipeline]['url'], config_file,
                         sample_sheet, False)


def create_project():
    args = command_line(0, True)
    print('Generating data analysis project from template: {}'.format(
        args.template))
    execute_cookiecutter(args.template, args.config_file,
                         args.sample_sheet, args.copy_rawdata)


def start_server_main():
    parser = argparse.ArgumentParser(
        description='Start the PM4NGS jupyter server')

    parser.add_argument('-v', '--version', action='version',
                        version='PM4NGS version: {}'.format(__version__))
    parser.add_argument('--no_browser',
                        help='Don\'t open the notebook in a browser after startup',
                        action='store_true',
                        required=False)
    parser.add_argument('--ip',
                        help='The IP address the notebook server will listen on. '
                             'Default: localhost',
                        type=str,
                        required=False)
    parser.add_argument('--port',
                        help='The port the notebook server will listen on. '
                             'Default: 8888',
                        type=int,
                        required=False)

    args = parser.parse_args()
    jupyter_cmd = "jupyter notebook"
    if args.no_browser:
        jupyter_cmd += " --NotebookApp.open_browser=False"
    else:
        jupyter_cmd += " --NotebookApp.open_browser=True"
    if args.ip:
        jupyter_cmd += " --ip=" + args.ip
    if args.port:
        jupyter_cmd += " --port={}".format(args.port)
    print('Starting server with command:\n{}'.format(jupyter_cmd))
    subprocess.run(jupyter_cmd, shell=False)
