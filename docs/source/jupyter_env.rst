Installing Jupyter Notebook environment
=======================================

.. _jupyter_env_conda:

Jupyter environment using Conda
-------------------------------

A Conda environment named: **jupyter** with Python 3.6+ should be created for running all Jupyter notebooks.

.. code-block:: bash

    localhost:~> wget https://raw.githubusercontent.com/ncbi/cwl-ngs-workflows-cbb/master/requirements/conda-jupyter.yaml
    localhost:~> conda env create -f conda-jupyter.yaml

Usage with Conda
^^^^^^^^^^^^^^^^

For using the Conda environment

.. code-block:: bash

    localhost:~> conda activate jupyter

.. _jupyter_env_python:

Jupyter environment using Python virtual environment
----------------------------------------------------

Python 3.6+ should be installed. Then, a virtual environment should be created from the requirements_ file and
these commands:

.. code-block:: bash

    localhost:~> wget https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/%7B%7Bcookiecutter.project_name%7D%7D/requirements/python.txt
    localhost:~> virtualenv -p `which python3` venv
    localhost:~> source venv/bin/activate
    localhost:~> pip install -r python.txt

Usage with Python virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For using the Python virtual environment

.. code-block:: bash

    localhost:~> source venv/bin/activate

.. _requirements: https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/%7B%7Bcookiecutter.project_name%7D%7D/requirements/python.txt
