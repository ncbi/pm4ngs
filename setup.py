import os
import os.path

from setuptools import find_packages
from setuptools import setup


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        return f.read()

# Set __version__
exec(open('src/pm4ngs/__init__.py').read())

setup(
    name='pm4ngs',
    packages=find_packages(where='src'),
    package_dir={
        '': 'src',
    },
    data_files=[('', ['README.md'])],
    use_scm_version=True,
    setup_requires=['wheel', 'setuptools_scm'],
    description='PM4NGS generates a standard organizational structure for Next '
                'Generation Sequencing (ngs) data analysis ',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='Public Domain',
    author='Vera Alvarez, Roberto',
    author_email='veraalva' '@' 'ncbi.nlm.nih.gov',
    maintainer='Vera Alvarez, Roberto',
    maintainer_email='veraalva' '@' 'ncbi.nlm.nih.gov',
    url='https://github.com/ncbi/pm4ngs',
    install_requires=['bioconda2biocontainer',
                      'biopython',
                      'cookiecutter',
                      'cwltool',
                      'docker',
                      'galaxy-tool-util',
                      'GitPython',
                      'goenrichment',
                      'jupyter',
                      'matplotlib',
                      'networkx',
                      'numpy',
                      'pandas',
                      'pdf2image',
                      'PyYAML',
                      'requests',
                      'scipy',
                      'seaborn',
                      'statsmodels',
                      'urllib3',
                      'xmltodict'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    keywords='Biocontainers',
    project_urls={
        'Documentation': 'https://pm4ngs.readthedocs.io/',
        'Source': 'https://github.com/ncbi/pm4ngs',
        'Tracker': 'https://github.com/ncbi/pm4ngs/issues',
    },
    entry_points={
        'console_scripts': [
            'pm4ngs-server = pm4ngs.main:start_server_main',
            'pm4ngs-create = pm4ngs.main:create_project',
            'pm4ngs-rnaseq = pm4ngs.main:rnaseq',
            'pm4ngs-rnaseq-demo = pm4ngs.main:rnaseq_demo',
            'pm4ngs-chipseq = pm4ngs.main:chipseq',
            'pm4ngs-chipseq-demo = pm4ngs.main:chipseq_demo',
            'pm4ngs-chipexo = pm4ngs.main:chipexo',
            'pm4ngs-chipexo-demo = pm4ngs.main:chipexo_demo'
        ],
    }
)
