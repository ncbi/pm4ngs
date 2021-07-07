import os
import subprocess
import sys
from multiprocessing import Pool, cpu_count
from shutil import copytree, copyfile, Error

import numpy as np
import pandas
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


def rawdata_file_manager(file, WORK_DIR, DATASET_DIR):
    if file.startswith('/') and os.path.exists(file):
        return copy_file(file, DATASET_DIR)
    elif file.startswith('http') or file.startswith('ftp'):
        return download_file(file, DATASET_DIR)
    return copy_file(os.path.join(WORK_DIR, file), DATASET_DIR)


def copy_rawdata_to_project(COPY_RAWDATA, DATASET_DIR):
    if COPY_RAWDATA == 'True':
        sample_table_file = os.path.join(DATASET_DIR, 'sample_table.csv')
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
