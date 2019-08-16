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
    │   ├── 01 - .....ipynb
    │   ├── 02 - .....ipynb
    ├── README.md
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── {{dataset_name}}
    ├── src
    └── tmp

Jupyter Notebooks
-----------------


CWL workflows
-------------

