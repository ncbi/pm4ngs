Project Templates Installation
==============================

Project Templates with Python virtual environment
-------------------------------------------------

Install Cookiecutter and other basic Python packages using the **requirements.txt** file.

.. code-block:: bash

    localhost:~> virtualenv venv-templates
    localhost:~> source venv-templates/bin/activate
    localhost:~> pip install -r https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/requirements.txt


Project Templates with Conda/BioConda
-------------------------------------

Conda_ should be already installed and configured.

.. code-block:: bash

    localhost:~> wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    localhost:~> sh Miniconda3-latest-MacOSX-x86_64.sh

A Conda virtual environment will be created with name **templates** using these instructions:

.. code-block:: bash

    localhost:~> wget https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/conda-requirements.yaml
    localhost:~> conda env create -f conda-requirements.yaml

If Conda is installed with prefix **/gfs/conda** you should see the available environments like in this block:

.. code-block:: bash

    localhost:~> conda env list
    # conda environments:
    #
    base                     /gfs/conda
    templates             *  /gfs/conda/envs/templates

    localhost:~>

To activate the templates env

.. code-block:: bash

    localhost:~> conda activate templates
    localhost:~>


.. _Conda: https://github.com/conda/conda

Using the Template Project
--------------------------

This project template uses the workflow defined in the project cwl-ngs-workflows-cbb_. Depending on the execution
environment selected: **docker**, **conda** or **programs in the path** the project template will check the
availability of the Bioinformatic tools required by the workflow.

.. _cwl-ngs-workflows-cbb: https://github.com/ncbi/cwl-ngs-workflows-cbb
