Background Information
======================

Project organizational structure
--------------------------------

**cookiecutter-jupyter-ngs** creates, from a configuration yaml file, a project organizational structure that allows
users organize the relevant files and directories in a standard way. The main idea behind this organizational
structure is allow someone unfamiliar with the project understand how the data analysis process was executed and an
easy localization of any file inside the project directories.

The project organizational structure depends on two main variables defined in the configuration file: **project_name**
and **dataset_name**. The **project_name** is used to create the top-level directory which contain all projects data.
The **dataset_name** is used create a directory which contains specific data for the dataset analyzed.
For example, a project name can be: **rnaseq_project_1** and the dataset can be a NCBI BioProject like **PRJNA238004**.

The tree shows the organizational structure that will be created for a project. The variables **{{project_name}}** and
**{{dataset_name}}** will be substituted by the value in the configuration yaml file.

.. code-block:: bash

    {{project_name}}
    ├── bin
    │   ├── bioconda (If using Conda this folder include a conda envs for all bioinfo tools)
    │   ├── cwl-ngs-workflows-cbb (CWL workflow repo cloned here)
    │   └── jupyter  (If using Conda this folder include a conda envs for Jupyter notebooks)
    ├── config
    │   └── init.py
    ├── data
    │   └── {{dataset_name}}
    ├── doc
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

The structure has 8 directories: bin, config, data, notebooks, requirements, results, src and tmp.

.. topic:: Main directories

    * **bin**: This directory is used for scripts or executables used by the project that are developed or inserted by the
      project author.

      Also, in this directory the CWL workflow repo project will be clone. This allow to have a static copy of the
      workflows used for the analysis.

    * **config**: This directory is used for any configuration file for the project. Initially a **init.py** file is
      created. This file is used to configure all Jupyter notebook and include all project variables like
      dataset name, genome annotation location, if use docker or no, etc.

    * **data**: This directory is use for all data that will be used as input in the project.

      In this directory there is a subdirectory {{dataset_name}} that will include the :doc:`factors.txt <factors_file>`
      file and all fastq files to be analyzed.

      In this directory the user should copy any public database or external data used during the data analysis.

    * **doc**: This directory is used to store any project documentation and the manuscript files.
    * **notebooks**: This directory include all Jupyter notebooks
    * **requirements**: This directory include any requirement the project may have. It is included the python
      requirements to starting the jupyter server.
    * **results**: This directory will include all results generated in the project organized by directories.
    * **src**: This directory is used to include any source code developed for the project.
    * **tmp**: This is a temporal directory used for the cwl-runner.


Jupyter Notebooks
-----------------



CWL workflows
-------------

