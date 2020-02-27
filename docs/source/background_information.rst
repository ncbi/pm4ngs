Background Information
======================

Project organizational structure
--------------------------------

**pm4ngs** creates, from a configuration yaml file, a project organizational structure that allows
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
PM4NGS uses Jupyter Notebooks for data and workflow management. The notebooks are designed with minimum Python code,
making them simple to understand and execute. For a standard analysis, notebooks can be executed without any
modification, just by clicking on the Jupyter Menu Cell and then on Run All. This action will execute the complete
workflow implemented in that notebook. It is important to highlight that Jupyter Notebook was selected as the user
interface in this project because it allows more advanced users the extension of the analysis with customized workflows.

In addition, the entire workflow can be distributed in multiple notebooks, making it easy to understand and re-execute,
if necessary. Further, making the workflow interactive allows a visualization and check of the intermediate results,
saving time and resources in case errors are detected.

All workflows include a notebook named 00 – Project Report. This notebook should be executed after each step is finished.
It will automatically create tables and figures that users can use to validate the data-analysis process.
This notebook also creates its own version in HTML format that could be used to share the results with collaborators
or supervisors, see these examples for an `RNASeq project`_

CWL Workflows
-------------

The tools and workflows included in this framework are published in a separate Git repository;
see `cwl-ngs-workflows-cbb`_. This repository is comprised of three main directories. The first directory,
named requirements, includes a set of Conda environment-definition files for the workflow execution.
These files define the computational tools and exact a version used for the analysis. They can be used in any
computational environment to recreate the same scenario in which the project was executed. If Docker is selected
as an execution environment, each computational tool included in this repository contains a statement that defines
the exact Docker image that will be used for the tool execution. The second directory, named tools, includes all
computational tools used by the workflows. Finally, the third folder, named workflows, includes all workflows.


.. _RNASeq project: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/rnaseq-sra-paired/
.. _cwl-ngs-workflows-cbb: https://github.com/ncbi/cwl-ngs-workflows-cbb