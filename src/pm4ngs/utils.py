import os
import subprocess
import sys
from multiprocessing import Pool, cpu_count
from shutil import copytree, copyfile, Error

import numpy as np
import pandas
import yaml
from bioconda2biocontainer.update_cwl_docker_image import update_cwl_docker_from_tool_name
from git import Repo


def clone_git_repo(repo, dest_dir):
    """
    Clone the git repo from the cookiecutter.cwl_workflow_repo to the bin directory
    :return:
    """
    print('Cloning Git repo: {0} to {1}'.format(repo, dest_dir))
    Repo.clone_from(repo, dest_dir)


def copy_directory(src, dest):
    try:
        copytree(src, dest)
    # Directories are the same
    except Error as e:
        print('Directory not copied. Error: %s' % e)
        sys.exit(-1)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)
        sys.exit(-1)


def copy_file(src, dest):
    if os.path.exists(src):
        try:
            dest = os.path.join(dest, os.path.basename(src))
            print(src + ' ==> ' + dest)
            copyfile(src, dest)
            return 0
            # Directories are the same
        except Error as e:
            print('File not copied. Error: %s' % e)
        # Any error saying that the directory doesn't exist
        except OSError as e:
            print('File not copied. Error: %s' % e)
    else:
        print('File {} not found'.format(src))
    return -1


def download_file(src, dest):
    dest = os.path.join(dest, os.path.basename(src))
    print('Downloading file {} to {}'.format(src, dest))
    status = subprocess.run(['curl', '-o', dest, src], capture_output=True)
    return status.returncode


def rawdata_file_manager(file, work_dir, dataset_dir):
    if file.startswith('/') and os.path.exists(file):
        return copy_file(file, dataset_dir)
    elif file.startswith('http') or file.startswith('ftp'):
        return download_file(file, dataset_dir)
    return copy_file(os.path.join(work_dir, file), dataset_dir)


def copy_rawdata_to_project(copy_rawdata, dataset_dir):
    if copy_rawdata == 'True':
        sample_table_file = os.path.join(dataset_dir, 'sample_table.csv')
        sample_table = pandas.read_csv(sample_table_file, skip_blank_lines=True)
        sample_table = sample_table.replace(np.nan, '', regex=True)
        sample_table = sample_table[['sample_name', 'file', 'condition', 'replicate']]
        print('{} files loaded\nUsing table:'.format(len(sample_table)))
        print(sample_table)
        files = []
        for f in sample_table[sample_table['file'] != '']['file'].unique():
            files.extend(f.split('|'))
        if len(files) > 0:
            print('Copying files in parallel using: {} CPUs'.format(cpu_count() - 1))
            p = Pool(processes=cpu_count() - 1)
            status = p.map(rawdata_file_manager, files)
            for s in status:
                if s != 0:
                    print('Error copying raw data to project')
                    sys.exit(-1)


def copy_cwl_repo(repo, dest_dir):
    if 'github.com' in repo:
        clone_git_repo(repo, dest_dir)
    elif os.path.exists(repo):
        print('Copying CWL directory {} to {}'.format(repo, dest_dir))
        copy_directory(repo, dest_dir)
    else:
        print('CWL_WORKFLOW_REPO = {} not available.'.format(repo))
        print('Use Github URL or absolute path')
        sys.exit(-1)


def update_cwl_biocontainers(conda_dependencies, dest_dir):
    print('Updating CWLs dockerPull and SoftwareRequirement from: ' + conda_dependencies)
    with open(conda_dependencies) as fin:
        conda_env = yaml.load(fin, Loader=yaml.FullLoader)
        if 'dependencies' in conda_env:
            for d in conda_env['dependencies']:
                update_cwl_docker_from_tool_name(d, dest_dir)


def copy_sample_table(sample_table_file, dataset_dir):
    print('Copying file {}  to {}'.format(
        sample_table_file, os.path.join(dataset_dir, 'sample_table.csv')
    ))
    copyfile(sample_table_file, os.path.join(dataset_dir, 'sample_table.csv'))


def main_hook_standard_template(dataset,
                                cwl_workflow_repo='https://github.com/ncbi/cwl-ngs-workflows-cbb'):

    sample_table_file = os.environ.get('PM4NGS_SAMPLE_TABLE', None)
    copy_rawdata = os.environ.get('PM4NGS_COPY_RAWDATA', None)
    work_dir = os.environ.get('PM4NGS_WORK_DIR', None)
    project_directory = os.path.realpath(os.path.curdir)

    if sample_table_file and copy_rawdata and work_dir:
        dataset_dir = os.path.join(project_directory, 'data', dataset)
        conda_dependencies = os.path.join(project_directory, 'requirements', 'conda-env-dependencies.yaml')
        if os.path.exists(conda_dependencies):
            copy_cwl_repo(cwl_workflow_repo, os.path.join(project_directory, 'bin', 'cwl'))
            update_cwl_biocontainers(conda_dependencies, os.path.join(project_directory, 'bin', 'cwl'))
            copy_sample_table(sample_table_file, dataset_dir)
            copy_rawdata_to_project(copy_rawdata, dataset_dir)
            print(' Done')
        else:
            print('No conda env dependency file in {0}'.format(conda_dependencies))
            sys.exit(-1)
    else:
        print('Error reading user env')
        print('PM4NGS_SAMPLE_TABLE: ' + str(sample_table_file))
        print('PM4NGS_COPY_RAWDATA: ' + str(copy_rawdata))
        print('PM4NGS_WORK_DIR: ' + str(work_dir))
        sys.exit(-1)
