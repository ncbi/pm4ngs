#!/usr/bin/env python
import os
import sys
import yaml
import docker
import virtualenv
import subprocess
import distutils.spawn
from subprocess import run
from git import Repo

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
NGS_DATA_TYPE = '{{ cookiecutter.ngs_data_type }}'
CREATE_VIRTUALENV = '{{ cookiecutter.create_virtualenv }}'
PULL_IMAGES = '{{ cookiecutter.pull_images }}'
CWL_WORKFLOW_REPO = '{{ cookiecutter.cwl_workflow_repo }}'
USE_CONDA = '{{ cookiecutter.use_conda }}'


def check_dependencies_path(config):
    """
    Check dependencies from the Yaml config file
    :param config_yaml_file: Yaml config file with dependencies
    """
    for tool in config:
        print('.', end='')
        sys.stdout.flush()
        tool, value = tool.popitem()
        if USE_CONDA == 'y':
            conda_dir = os.path.join(PROJECT_DIRECTORY, 'bin', 'bioconda', 'bin')
            tool_path = os.path.join(conda_dir, value['command'])
        else:
            tool_path = distutils.spawn.find_executable(value['command'])
        if not tool_path:
            if 'version' in value:
                print('\nERROR: {0} version: {1} not available.'.format(tool, value['version']))
            else:
                print('\nERROR: {0} not available.'.format(tool))
            sys.exit(-1)
        else:
            if 'out' in value:
                commands = [tool_path]
                if 'option' in value:
                    if type(value['option']) == str:
                        commands.append(value['option'])
                    elif type(value['option']) == list:
                        for a in value['option']:
                            commands.append(a)
                print(commands)
                process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()
                if 'stderr' in value['out']:
                    out = err
                if 'version' in value:
                    if value['version'] not in str(out.decode('UTF-8')).rstrip():
                        print('\nERROR: {0} version: {1} not available'.format(tool, value['version']))
                        print('Tools absolute path: {0}'.format(tool_path))
                        print('Installed version:\n{0}'.format(out.decode('UTF-8')))
                        print(out.decode('UTF-8'))
                        sys.exit(-1)
                if 'output' in value:
                    if value['output'] not in str(out.decode('UTF-8')).rstrip():
                        print('\nERROR: {0} not available.'.format(tool))
                        print('Tools absolute path: {0}'.format(tool_path))
                        print('Expected output:\n{0}'.format(value['output']))
                        print('Real output:\n{0}'.format(out.decode('UTF-8')))
                        print(out.decode('UTF-8'))
                        sys.exit(-1)


def check_docker_image(config, client):
    """
    Check if the docker images is available
    :param config: List of image names with tags
    :param client: Docker API client
    """
    for i in config:
        print('.', end='')
        sys.stdout.flush()
        try:
            client.images.get(i)
        except docker.errors.ImageNotFound as exc:
            if PULL_IMAGES == 'y':
                print('\n\tPulling image: {0}'.format(i), end=' . ')
                sys.stdout.flush()
                client.images.pull(i)
                print('Done '.format(i), end='')
                sys.stdout.flush()
            else:
                print('\nERROR: Image {0} not available.'.format(i))
                sys.exit(-1)


def build_docker_image(config, client):
    """
    Check if the docker images exists.
    If not, then build the image using the dockerfile
    :param config: List of image names with dockerfile
    :param client: Docker API client
    """
    for i in config:
        try:
            client.images.get(i)
        except docker.errors.ImageNotFound as exc:
            if PULL_IMAGES == 'y' and 'dockerfile' in config[i]:
                print('\n\tBuilding image: {0}'.format(i), end=' . ')
                sys.stdout.flush()
                dockerfile = os.path.basename(config[i]['dockerfile'])
                tag = i
                if 'tag' in config[i]:
                    tag += ':{0}'.format(config[i]['tag'])
                client.images.build(path=config[i]['dockerfile'],
                                    tag=tag,
                                    dockerfile=dockerfile)
                print('Done '.format(i), end='')
                sys.stdout.flush()
            else:
                print('\nERROR: Image {0} not available.'.format(i))
                sys.exit(-1)


def check_dependencies_docker(config):
    client = docker.from_env()
    if 'docker_pull' in config:
        check_docker_image(config['docker_pull'], client)
    if 'docker_build' in config:
        build_docker_image(config['docker_build'], client)


def check_dependencies(config_yaml_file):
    """
    Check dependencies from the Yaml config file
    :param config_yaml_file: Yaml config file with dependencies
    """
    with open(config_yaml_file, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            if 'tools' in config:
                check_dependencies_path(config['tools'])
            elif 'docker' in config:
                check_dependencies_docker(config['docker'])
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit(-1)


def create_virtualenv():
    """
    Creates the virtualenv and install all packages
    """
    print('Creating a Python3.7 virtualenv')
    venv_dir = os.path.join(PROJECT_DIRECTORY, "venv")
    virtualenv.create_environment(venv_dir)
    requirement_file = os.path.join(PROJECT_DIRECTORY, 'requirements', 'python.txt')
    print('Installing packages in: {0} using file {1}'.format(venv_dir, requirement_file))
    process = subprocess.Popen([os.path.join(venv_dir, 'bin', 'python'), '-m',
                                'pip', 'install', "--prefix", venv_dir, "-r",
                                requirement_file],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print('Error installing packages from {0}'.format(requirement_file))
        print(err.decode('UTF-8'))
        sys.exit(-1)


def rename_notebook(src, dest):
    """
    Rename the source notebook file with the dest or remove the src if dest = None
    :param src: Source file
    :param dest: Destiny file
    """
    src = os.path.join(PROJECT_DIRECTORY, 'notebooks', src + '.ipynb')
    if src and dest:
        dest = os.path.join(PROJECT_DIRECTORY, 'notebooks', dest + '.ipynb')
        os.rename(src, dest)
    else:
        os.remove(src)


def clone_git_repo():
    """
    Clone the git repo from the cookiecutter.cwl_workflow_repo to the bin directory
    :return:
    """
    BASE_NAME = os.path.basename(CWL_WORKFLOW_REPO)
    print('Cloning Git repo: {0} to {1}'.format(CWL_WORKFLOW_REPO,
                                                os.path.join(PROJECT_DIRECTORY, 'bin', BASE_NAME)))
    Repo.clone_from(CWL_WORKFLOW_REPO, os.path.join(PROJECT_DIRECTORY, 'bin', BASE_NAME))


def create_conda_env(conda_env):
    """
    Create a Conda environment from a conda env file
    :param conda_env: Conda env file in the CWL repo
    """
    if 'https://github.com/' in CWL_WORKFLOW_REPO:
        BASE_NAME = os.path.basename(CWL_WORKFLOW_REPO)
        conda_env = os.path.join(PROJECT_DIRECTORY, 'bin', BASE_NAME, 'requirements', conda_env)
        conda_jupyter_env = os.path.join(PROJECT_DIRECTORY, 'bin', BASE_NAME, 'requirements', 'conda-jupyter.yaml')
    else:
        conda_env = os.path.join(CWL_WORKFLOW_REPO, 'requirements', conda_env)
        conda_jupyter_env = os.path.join(CWL_WORKFLOW_REPO, 'requirements', 'conda-jupyter.yaml')

    conda_dir = os.path.join(PROJECT_DIRECTORY, 'bin', 'jupyter')
    if not os.path.exists(conda_dir):
        print('Installing Conda env: {0} to {1}'.format(conda_jupyter_env, conda_dir))
        run(['conda', 'env', 'create', '-f', conda_jupyter_env, '--prefix=' + conda_dir])

    conda_dir = os.path.join(PROJECT_DIRECTORY, 'bin', 'bioconda')
    if not os.path.exists(conda_dir):
        print('Installing Conda env: {0} to {1}'.format(conda_env, conda_dir))
        run(['conda', 'env', 'create', '-f', conda_env, '--prefix=' + conda_dir])


if __name__ == '__main__':
    notebook_01_dest = None
    notebook_02_dest = None
    notebook_03_dest = None
    notebook_04_dest = None
    notebook_05_dest = None
    notebook_06_dest = None

    if NGS_DATA_TYPE == 'RNA-Seq':
        config_path = os.path.join(PROJECT_DIRECTORY, 'config', 'rnaseq.yaml')
        conda_env = 'conda-rnaseq.yaml'
        notebook_01_dest = '01 - Pre-processing QC'
        notebook_02_dest = '02 - Samples trimming'
        notebook_03_dest = '03 - Alignments'
        notebook_04_dest = '04 - Quantification'
        notebook_05_dest = '05 - DGA'
        notebook_06_dest = '06 - GO enrichment'
    elif NGS_DATA_TYPE == 'ChIP-Seq':
        config_path = os.path.join(PROJECT_DIRECTORY, 'config', 'chipseq.yaml')
        conda_env = 'conda-chipseq.yaml'
        notebook_01_dest = '01 - Pre-processing QC'
        notebook_02_dest = '02 - Samples trimming'
        notebook_03_dest = '03 - Alignments'
        notebook_04_dest = '04 - Peak Calling'
        notebook_05_dest = '05 - Differential binding analysis'
    elif NGS_DATA_TYPE == 'ChIP-exo':
        config_path = os.path.join(PROJECT_DIRECTORY, 'config', 'chipexo.yaml')
        conda_env = 'conda-chipexo.yaml'
        notebook_01_dest = '01 - Pre-processing QC'
        notebook_02_dest = '02 - Samples trimming'
        notebook_03_dest = '03 - Alignments'
        notebook_04_dest = '04 - Peak Calling'
        notebook_05_dest = '05 - MEME Motif'
    elif NGS_DATA_TYPE == 'Transcript-Annotation':
        config_path = os.path.join(PROJECT_DIRECTORY, 'config', 'trans-annot.yaml')
        conda_env = 'conda-trans-annot.yaml'

    if config_path:
        if 'github.com' in CWL_WORKFLOW_REPO:
            clone_git_repo()

        if USE_CONDA == 'n':
            if CREATE_VIRTUALENV == 'y':
                create_virtualenv()
        elif USE_CONDA == 'y':
            create_conda_env(conda_env)

        print('Checking {0} workflow dependencies '.format(NGS_DATA_TYPE), end='')
        sys.stdout.flush()
        check_dependencies(config_path)
        print(' Done')
        config_path = os.path.join(PROJECT_DIRECTORY, 'config')
        yaml_files = [f for ds, dr, files in os.walk(config_path)
                      for f in files if f.endswith('.yaml')]
        for y in yaml_files:
            os.remove(os.path.join(config_path, y))

        rename_notebook('01', notebook_01_dest)
        rename_notebook('02', notebook_02_dest)
        rename_notebook('03', notebook_03_dest)
        rename_notebook('04', notebook_04_dest)
        rename_notebook('05', notebook_05_dest)
        rename_notebook('06', notebook_06_dest)
    else:
        print('No config_path file for NGS data type {0}'.format(NGS_DATA_TYPE))
        sys.exit(-1)
