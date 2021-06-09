.. _installation:

############
Installation
############

************
Requirements
************

 1. Poppler (https://poppler.freedesktop.org/)

****************************************
PM4NGS with Conda/BioConda (Recommended)
****************************************

Conda installation
==================

Conda_ should be already installed and configured using these commands:

.. code-block:: bash

    localhost:~> wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    localhost:~> sh Miniconda3-latest-Linux-x86_64.sh
    localhost:~> conda config --add channels defaults
    localhost:~> conda config --add channels bioconda
    localhost:~> conda config --add channels conda-forge	

PM4NGS conda installation
=========================

PM4NGS should be installed in a Conda virtual environment named *pm4ngs*:

.. code-block:: bash

    localhost:~> conda create -n pm4ngs pm4ngs

PM4NGS conda env activation
===========================

For activating the conda env:

.. code-block:: bash

    localhost:~> conda activate pm4ngs
    localhost:~> pm4ngs-create -v
    PM4NGS version: 0.1.dev0+d20200819

.. _Conda: https://github.com/conda/conda

**************************************
PM4NGS with Python virtual environment
**************************************

PM4NGS python installation
==========================

Python 3.6 or above should be installed.

.. code-block:: bash

    localhost:~> python3 -m venv pm4ngs_venv
    localhost:~> source pm4ngs_venv/bin/activate
    (pm4ngs_venv) localhost:~> pip install wheel
    (pm4ngs_venv) localhost:~> pip install pm4ngs

PM4NGS python env activation
============================

For activating the virtual env:

.. code-block:: bash

    localhost:~> source pm4ngs_venv/bin/activate
    (pm4ngs_venv) localhost:~> pm4ngs-create -v
    PM4NGS version: 0.0.4
