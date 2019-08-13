Installation
=============

Python virtual environment
--------------------------

Install Cookiecutter and other basic Python packages using the **requirements.txt** file.

.. code-block:: bash

    virtualenv venv
    source venv/bin/activate
    pip install -r https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/requirements.txt


Conda virtual environment
-------------------------

Conda_ should be already installed and configured.

.. code-block:: bash

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
    sh Miniconda3-latest-MacOSX-x86_64.sh

A Conda virtual environment will be created with name **templates** using these instructions:

.. code-block:: bash

    wget https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/conda-requirements.yaml
    conda env create -f conda-requirements.yaml

If Conda is installed with prefix `/home/user/conda` you should see the available environments like in this block:

.. code-block:: bash

    perseo:/home/user> conda env list
    # conda environments:
    #
    base                     /home/user/conda
    templates             *  /home/user/conda/envs/templates

    perseo:/home/user>

.. _Conda: https://github.com/conda/conda

Using the template project manager
----------------------------------

This project template uses the workflow defined in the project cwl-ngs-workflows-cbb_. Depending on the execution
environment selected: **docker**, **conda** or **programs in the path** the project template will check the
availability of the Bioinformatic tools required by the workflow.

.. _cwl-ngs-workflows-cbb: https://github.com/ncbi/cwl-ngs-workflows-cbb

Without Docker
^^^^^^^^^^^^^^

For using the **cookiecutter-jupyter-ngs** to generate a project structure, all programs required by the workflow should
be available on the user PATH.

If **conda** is selected as execution environment, the project template will create the conda virtual environment
defined by each project, see examples here_

.. _here: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/requirements

Using Docker
^^^^^^^^^^^^

For using the **cookiecutter-jupyter-ngs** to generate a project structure, all docker images required by the workflow
should be available on the machine.

If the user has **docker pull** permission the template project will pull all docker images automatically.
