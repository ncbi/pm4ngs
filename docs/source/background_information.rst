Background Information
======================

Introduction
------------

**cookiecutter-jupyter-ngs** is designed to generate a standard data analysis project structure including Jupyter
notebooks for data management and CWL workflows for pipeline execution. All type of projects generated from these
templates follow the same design principles explained in this document.

Currently, the projects are designed to be executed in a single server with multiple cores for simplicity. We are
working to extend the templates to execute the workflows in HPC or cloud systems. `GNU Parallel`_ is used to run
multiple workflows at the same time using all available cores in the server.

The projects are composed of three main parts. The first one is the **project structure** which define a standard
filesystem organization for the project. The second part are **Jupyter Notebooks** as user interfaces for data
management and execution of the CWL workflows. The third part are the **CWL workflow** that process the samples.

**cookiecutter-jupyter-ngs** include the templates for generating the project structure and the Jupyter notebook
specific to each type of data analysis. The CWL workflows are defined in a separate GitHub project named:
`cwl-ngs-workflows-cbb`_.

.. _GNU Parallel: https://www.gnu.org/software/parallel/
.. _cwl-ngs-workflows-cbb: https://github.com/ncbi/cwl-ngs-workflows-cbb

Project structure
-----------------

**cookiecutter-jupyter-ngs** creates, from a configuration yaml file, a project structure that allows users
organize the project input files, results files and report in a standard way that allow an easy localization of any
file.

The project has two main variables in the configuration file: **project_name** and **dataset_name**. The
**project_name** is used to create the main folder which contain all projects data. The **dataset_name** is used
to contain specific data for the dataset analyzed. For example, a project name can be: **rnaseq_project_1** and the
dataset can be a NCBI BioProject like **PRJNA238004**.

The tree shows the basic structure for the project. The variables **{{project_name}}** and **{{dataset_name}}** will be
substituted byt the value in the configuration yaml file.

.. code-block:: bash

    {{project_name}}
    ├── bin
    ├── config
    │   └── init.py
    ├── data
    │   └── {{dataset_name}}
    ├── index.html
    ├── LICENSE
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - .... .ipynb
    │   ├── 02 - .... .ipynb
    ├── README.md
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── {{dataset_name}}
    ├── src
    └── tmp

The structure has 8 folders: bin, config, data, notebooks, requirements, results, src and tmp.

.. topic:: Main folders

    * **bin**: This folder is used for scripts or executables used by the project that are developed or inserted by the
      project author.

      Also, in this folder the CWL workflow repo project will be clone. This allow to have a static copy of the
      workflows used for the analysis.

    * **config**: This folder is used for any configuration file for the project. Initially a **init.py** file is
      created. This file is used to configure all Jupyter notebook and include all project variables like
      dataset name, genome annotation location, if use docker or no, etc.

    * **data**: This folder is use for all data that will be used as input in the project.

      In this folder there is a subfolder {{dataset_name}} that will include the :doc:`factors.txt <factors_file>`
      file and all fastq files to be analyzed.

      In this folder the user should copy any public database or external data used during the data analysis.

    * **notebooks**: This folder include all Jupyter notebooks
    * **requirements**: This folder include any requirement the project may have. It is included the python requirements
      to starting the jupyter server.
    * **results**: This folder will include all results generated in the project.
    * **src**: This folder is used to include any source code developed for the project.
    * **tmp**: This is a temporal folder used for the cwl-runner.


Jupyter Notebooks
-----------------


CWL workflows
-------------

