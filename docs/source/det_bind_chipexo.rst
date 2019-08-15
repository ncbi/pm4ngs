Detection of binding events from ChIP-exo data
==============================================

Read :doc:`here <installation>` the notes to have the **cookiecutter** available in you shell.

Additionally, you should prepare the samples description file (**factors.txt**) as described
:doc:`here <factors_file>`.

ChIP-exo workflow with Conda/Bioconda
-------------------------------------

ChIP-exo workflow project structure with Conda/Bioconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ChIP-exo project structure is created using the conda environment named **templates**.

First step is to activate the  **templates** environment:

.. code-block:: bash

    perseo:~> conda activate templates

Then, a YAML file (for this example I will call this file: **chipexo-fur.yaml**) with your project detail should
be created.

.. code-block:: yaml
    :linenos:

    default_context:
        author_name: "Roberto Vera Alvarez"
        user_email: "veraalva@ncbi.nlm.nih.gov"
        project_name: "chipexo-fur"
        dataset_name: "PRJNA238004"
        is_data_in_SRA: "y"
        ngs_data_type: "ChIP-exo"
        sequencing_technology: "single-end"
        organism: "human"
        genome_dir: "/gfs/data/genomes/NCBI/Escherichia_coli/K-12/MG1655/"
        genome_name: "NC_000913.3"
        aligner_index_dir: "{{ cookiecutter.genome_dir}}/BWA"
        genome_fasta: "{{ cookiecutter.genome_dir}}/NC_000913.3.fa"
        genome_gtf: "{{ cookiecutter.genome_dir}}/NC_000913.3.gtf"
        genome_gff: "{{ cookiecutter.genome_dir}}/NC_000913.3.gff"
        genome_gff3: "{{ cookiecutter.genome_dir}}/NC_000913.3.gff3"
        genome_bed: "{{ cookiecutter.genome_dir}}/NC_000913.3.bed"
        genome_chromsizes: "{{ cookiecutter.genome_dir}}/NC_000913.3.sizes"
        genome_mappable_size: "3714120"
        genome_blacklist: "{{ cookiecutter.genome_dir}}/NC_000913.3.bed"
        fold_change: "2.0"
        fdr: "0.05"
        use_docker: "n"
        pull_images: "n"
        use_conda: "y"
        cwl_runner: "cwl-runner"
        cwl_workflow_repo: "/gfs/veraalva/Work/Developer/Python/cwl-ngs-workflows-cbb"
        create_virtualenv: "n"
        use_gnu_parallel: "y"
        max_number_threads: "16"

A full description of this parameters are :doc:`here <cookiecutter_json>`.

After the **chipexo-fur.yaml** is created the project structure should be created using this command obtaining the
following output.

.. code-block:: bash

    perseo:~> cookiecutter --no-input --config-file chipexo-fur.yaml https://github.com/ncbi/cookiecutter-jupyter-ngs.git
    Checking ChIP-exo workflow dependencies .......... Done
    perseo:~>

This process should create a project structure like this:

.. code-block:: bash

    perseo:~> tree chipexo-fur
    chipexo-fur
    ├── bin
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA238004
    ├── index.html
    ├── LICENSE
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   ├── 04 - Peak Calling.ipynb
    │   └── 05 - MEME Motif.ipynb
    ├── README.md
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA238004
    ├── src
    └── tmp

    10 directories, 11 files

Now you should copied the **factors.txt** file to the folder: **data/PRJNA238004**.

After this process, **cookiecutter** should have created create two virtual environment for this workflow.

The first one is for running the Jupyter notebooks which require Python 3.6+ and it is named: **jupyter**. It can be
manually installed as described in :doc:`here <jupyter_env>`.

The second environment is be used to install all Bioinformatics tools required by the workflow and it will be named:
**chipexo**.

You can verify the environments running this command:

.. code-block:: bash

    perseo:~> conda env list
    # conda environments:
    #
    base                  *  /gfs/conda
    chipexo                  /gfs/conda/envs/chipexo
    jupyter                  /gfs/conda/envs/jupyter
    tempates                 /gfs/conda/envs/templates

    perseo:~>

Please, note that the Conda prefix **/gfs/conda** will be different in you host.

ChIP-exo workflow usage with Conda/Bioconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For start using the workflow you need to activate the conda environments **chipexo** and **jupyter**.

.. code-block:: bash

    perseo:~> conda activate chipexo
    perseo:~> conda activate --stack jupyter

Note the **--stack** option to have both environment working at the same time. Also, the order is important, **chipexo**
should be activated before **jupyter**.

Then, you can start the jupyter notebooks.

.. code-block:: bash

    perseo:~> jupyter notebook

If the workflow is deployed in a remote machine using SSH access the correct way to start the notebooks is:

.. code-block:: bash

    perseo:~> jupyter notebook --no-browser --ip='0.0.0.0'

In this case the option **--ip='0.0.0.0'** will server the Jupyter notebook on all network interfaces and you can access
them from your desktop browser using the port returned by the Jupyter server.

ChIP-exo workflow with Docker
-----------------------------

ChIP-exo workflow project structure with Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, the ChIP-exo project structure is created using the Python virtual environment as described
:doc:`here <installation>`

First step is to activate the Python virtual environment.

.. code-block:: bash

    perseo:~> source venv-templates/bin/activate

Then, a YAML file (for this example I will call this file: **chipexo-fur.yaml**) with your project detail should
be created.

.. code-block:: yaml
    :linenos:

    default_context:
        author_name: "Roberto Vera Alvarez"
        user_email: "veraalva@ncbi.nlm.nih.gov"
        project_name: "chipexo-fur"
        dataset_name: "PRJNA238004"
        is_data_in_SRA: "y"
        ngs_data_type: "ChIP-exo"
        sequencing_technology: "single-end"
        organism: "human"
        genome_dir: "/gfs/data/genomes/NCBI/Escherichia_coli/K-12/MG1655/"
        genome_name: "NC_000913.3"
        aligner_index_dir: "{{ cookiecutter.genome_dir}}/BWA"
        genome_fasta: "{{ cookiecutter.genome_dir}}/NC_000913.3.fa"
        genome_gtf: "{{ cookiecutter.genome_dir}}/NC_000913.3.gtf"
        genome_gff: "{{ cookiecutter.genome_dir}}/NC_000913.3.gff"
        genome_gff3: "{{ cookiecutter.genome_dir}}/NC_000913.3.gff3"
        genome_bed: "{{ cookiecutter.genome_dir}}/NC_000913.3.bed"
        genome_chromsizes: "{{ cookiecutter.genome_dir}}/NC_000913.3.sizes"
        genome_mappable_size: "3714120"
        genome_blacklist: "{{ cookiecutter.genome_dir}}/NC_000913.3.bed"
        fold_change: "2.0"
        fdr: "0.05"
        use_docker: "y"
        pull_images: "y"
        use_conda: "n"
        cwl_runner: "cwl-runner"
        cwl_workflow_repo: "/gfs/veraalva/Work/Developer/Python/cwl-ngs-workflows-cbb"
        create_virtualenv: "y"
        use_gnu_parallel: "y"
        max_number_threads: "16"

A full description of this parameters are :doc:`here <cookiecutter_json>`.

After the **chipexo-fur.yaml** is created the project structure should be created using this command obtaining the
following output.

.. code-block:: bash

    perseo:~> cookiecutter --no-input --config-file chipexo-fur.yaml https://github.com/ncbi/cookiecutter-jupyter-ngs.git
    Checking ChIP-exo workflow dependencies .......... Done
    perseo:~>

This process should create a project structure like this:

.. code-block:: bash

    perseo:~> tree chipexo-fur
    chipexo-fur
    ├── bin
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA238004
    ├── index.html
    ├── LICENSE
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   ├── 04 - Peak Calling.ipynb
    │   └── 05 - MEME Motif.ipynb
    ├── README.md
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA238004
    ├── src
    ├── tmp
    └── venv

    11 directories, 11 files

Now you should copied the **factors.txt** file to the folder: **data/PRJNA238004**.

After this process, **cookiecutter** should have pulled all docker images require   bb bv           d by the project.

ChIP-exo workflow usage with Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For start using the workflow you need to activate the Python environment inside the project.

.. code-block:: bash

    perseo:~> source venv/bin/activate

Then, you can start the jupyter notebooks now.

.. code-block:: bash

    perseo:~> jupyter notebook

If the workflow is deployed in a remote machine using SSH access the correct way to start the notebooks is:

.. code-block:: bash

    perseo:~> jupyter notebook --no-browser --ip='0.0.0.0'

In this case the option **--ip='0.0.0.0'** will server the Jupyter notebook on all network interfaces and you can access
them from your desktop browser using the port returned by the Jupyter server.

