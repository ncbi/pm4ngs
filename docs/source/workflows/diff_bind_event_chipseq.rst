Differential Binding detection from ChIP-Seq data
=================================================

.. warning::  Read the :doc:`Background Information </background_information>` before proceeding with these steps

.. warning::
   Read the :doc:`Project Templates Installation </envs/installation>` notes to have the **cookiecutter** available
   in you shell depending on the execution environment you will be using.

.. include:: /extra/factors_file.rst

Installation
------------

ChIP-Seq workflow with Conda/Bioconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ChIP-Seq project structure is created using the conda environment named **templates**.

First step is to activate the  **templates** environment:

.. code-block:: bash

    localhost:~> conda activate templates

Then, a YAML file (for this example I will call this file: **chipseq-hmgn1.yaml**) with your project detail should
be created.

.. code-block:: yaml
    :linenos:

    default_context:
      author_name: "Roberto Vera Alvarez"
      user_email: "veraalva@ncbi.nlm.nih.gov"
      project_name: "chipseq-hmgn1"
      dataset_name: "PRJNA481982"
      is_data_in_SRA: "y"
      ngs_data_type: "ChIP-Seq"
      sequencing_technology: "paired-end"
      create_demo: "y"
      number_spots: "2000000"
      organism: "mouse"
      genome_dir: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/Mus_musculus/mm9"
      genome_name: "mm9"
      aligner_index_dir: "{{ cookiecutter.genome_dir}}/BWA"
      genome_fasta: "{{ cookiecutter.genome_dir}}/genome.fa"
      genome_gtf: "{{ cookiecutter.genome_dir}}/genes.gtf"
      genome_gff: "{{ cookiecutter.genome_dir}}/genes.gff"
      genome_gff3: "{{ cookiecutter.genome_dir}}/genes.gff3"
      genome_bed: "{{ cookiecutter.genome_dir}}/genes.bed"
      genome_chromsizes: "{{ cookiecutter.genome_dir}}/mm9.chrom.sizes"
      genome_mappable_size: "mm9"
      genome_blacklist: "{{ cookiecutter.genome_dir}}/mm9-blacklist.bed"
      fold_change: "2.0"
      fdr: "0.05"
      use_docker: "n"
      pull_images: "n"
      use_conda: "y"
      cwl_runner: "cwl-runner"
      cwl_workflow_repo: "https://github.com/ncbi/cwl-ngs-workflows-cbb"
      create_virtualenv: "n"
      use_gnu_parallel: "y"
      max_number_threads: "16"

A full description of this parameters are :doc:`here </extra/cookiecutter_json>`.

After the **chipseq-hmgn1.yaml** is created the project structure should be created using this command obtaining the
following output.

.. code-block:: bash

    localhost:~> cookiecutter --no-input --config-file chipseq-hmgn1.yaml https://github.com/ncbi/pm4ngs.git
    Checking ChIP-Seq workflow dependencies .......... Done
    localhost:~>

This process should create a project organizational structure like this:

.. code-block:: bash

    localhost:~> tree chipseq-hmgn1
    chipseq-hmgn1
    ├── bin
    │   ├── bioconda (This directory include a conda envs for all bioinfo tools)
    │   ├── cwl-ngs-workflows-cbb (CWL workflow repo cloned here)
    │   └── jupyter (This directory include a conda envs for Jupyter notebooks)
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA481982
    ├── doc
    ├── index.html
    ├── LICENSE
    ├── notebooks
    │   ├── 00\ -\ Project\ Report.ipynb
    │   ├── 01\ -\ Pre-processing\ QC.ipynb
    │   ├── 02\ -\ Samples\ trimming.ipynb
    │   ├── 03\ -\ Alignments.ipynb
    │   └── 04\ -\ Peak\ Calling.ipynb
    ├── README.md
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA481982
    ├── src
    └── tmp

    12 directories, 9 files

Now you should copied the **factors.txt** file to the folder: **data/PRJNA481982**.

After this process, **cookiecutter** should have created create two virtual environment for this workflow.

The first one is for running the Jupyter notebooks which require Python 3.6+ and it is named: **jupyter**. It can be
manually installed as described in :doc:`here </envs/jupyter_env>`.

The second environment is be used to install all Bioinformatics tools required by the workflow and it will be named:
**bioconda**.

You can verify the environments running this command:

.. code-block:: bash

    localhost:~> conda env list
    # conda environments:
    #
    base                  *  /gfs/conda
    tempates                 /gfs/conda/envs/templates
                             /home/veraalva/chipseq-hmgn1/bin/bioconda
                             /home/veraalva/chipseq-hmgn1/bin/jupyter

    localhost:~>

Please, note that the Conda prefix **/gfs/conda** will be different in you host. Also, note that the **bioconda** and
**jupyter** envs are inside the **bin** directory of your project keeping them static inside the project organizational
structure.

ChIP-Seq workflow usage with Conda/Bioconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For start using the workflow you need to activate the conda environments **bioconda** and **jupyter**.

.. code-block:: bash

    localhost:~> conda activate /home/veraalva/chipseq-hmgn1/bin/bioconda
    localhost:~> conda activate --stack /home/veraalva/chipseq-hmgn1/bin/jupyter

Note the **--stack** option to have both environment working at the same time. Also, the order is important, **bioconda**
should be activated before **jupyter**.

Test the conda envs:

.. code-block:: bash

    localhost:~> which fastqc
    /home/veraalva/chipseq-hmgn1/bin/bioconda/bin/fastqc
    localhost:~> which jupyter
    /home/veraalva/chipseq-hmgn1/bin/jupyter/bin/jupyter

Note that the **fastqc** tools is installed in the **bioconda** env and the **jupyter** command is installed in the
**jupyter** env.

Then, you can start the jupyter notebooks.

.. code-block:: bash

    localhost:~> jupyter notebook

If the workflow is deployed in a remote machine using SSH access the correct way to start the notebooks is:

.. code-block:: bash

    localhost:~> jupyter notebook --no-browser --ip='0.0.0.0'

In this case the option **--ip='0.0.0.0'** will server the Jupyter notebook on all network interfaces and you can access
them from your desktop browser using the port returned by the Jupyter server.

Finally, you should navegate in your browser to the **notebooks** folder and start executing all notebooks by their
order leaving the **00 - Project Report.ipynb** to the end.

ChIP-Seq workflow with Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, the ChIP-Seq project structure is created using the Python virtual environment as described
:doc:`here </envs/installation>`

First step is to activate the Python virtual environment.

.. code-block:: bash

    localhost:~> source venv-templates/bin/activate

Then, a YAML file (for this example I will call this file: **chipseq-hmgn1.yaml**) with your project detail should
be created.

.. code-block:: yaml
    :linenos:

    default_context:
      author_name: "Roberto Vera Alvarez"
      user_email: "veraalva@ncbi.nlm.nih.gov"
      project_name: "chipseq-hmgn1"
      dataset_name: "PRJNA481982"
      is_data_in_SRA: "y"
      ngs_data_type: "ChIP-Seq"
      sequencing_technology: "paired-end"
      create_demo: "y"
      number_spots: "2000000"
      organism: "mouse"
      genome_dir: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/Mus_musculus/mm9"
      genome_name: "mm9"
      aligner_index_dir: "{{ cookiecutter.genome_dir}}/BWA"
      genome_fasta: "{{ cookiecutter.genome_dir}}/genome.fa"
      genome_gtf: "{{ cookiecutter.genome_dir}}/genes.gtf"
      genome_gff: "{{ cookiecutter.genome_dir}}/genes.gff"
      genome_gff3: "{{ cookiecutter.genome_dir}}/genes.gff3"
      genome_bed: "{{ cookiecutter.genome_dir}}/genes.bed"
      genome_chromsizes: "{{ cookiecutter.genome_dir}}/mm9.chrom.sizes"
      genome_mappable_size: "mm9"
      genome_blacklist: "{{ cookiecutter.genome_dir}}/mm9-blacklist.bed"
      fold_change: "2.0"
      fdr: "0.05"
      use_docker: "y"
      pull_images: "y"
      use_conda: "n"
      cwl_runner: "cwl-runner"
      cwl_workflow_repo: "https://github.com/ncbi/cwl-ngs-workflows-cbb"
      create_virtualenv: "y"
      use_gnu_parallel: "y"
      max_number_threads: "16"

A full description of this parameters are :doc:`here </extra/cookiecutter_json>`.

After the **chipseq-hmgn1.yaml** is created the project structure should be created using this command obtaining the
following output.

.. code-block:: bash

    localhost:~>  cookiecutter --no-input --config-file chipseq-paired.yaml https://github.com/ncbi/pm4ngs.git
    Cloning Git repo: https://github.com/ncbi/cwl-ngs-workflows-cbb to /home/veraalva/chipseq-hmgn1/bin/cwl-ngs-workflows-cbb
    Creating a Python3.7 virtualenv
    Installing packages in: /home/veraalva/chipseq-hmgn1/venv using file /home/veraalva/chipseq-hmgn1/requirements/python.txt
    Checking ChIP-Seq workflow dependencies .
            Pulling image: quay.io/biocontainers/fastqc:0.11.8--1 . Done .
            Pulling image: quay.io/biocontainers/trimmomatic:0.39--1 . Done .
            Pulling image: quay.io/biocontainers/bwa:0.7.17--h84994c4_5 . Done .
            Pulling image: quay.io/biocontainers/bedtools:2.28.0--hdf88d34_0 . Done .
            Pulling image: quay.io/biocontainers/bcftools:1.9--h5c2b69b_5 . Done .
            Pulling image: quay.io/biocontainers/phantompeakqualtools:1.2--1 . Done .
            Pulling image: quay.io/biocontainers/samtools:1.9--h91753b0_8 . Done .
            Pulling image: quay.io/biocontainers/rseqc:3.0.0--py_3 . Done .
            Pulling image: quay.io/biocontainers/sra-tools:2.9.6--hf484d3e_0 . Done .
            Pulling image: quay.io/biocontainers/igvtools:2.5.3--0 . Done .
            Pulling image: quay.io/biocontainers/macs2:2.1.2--py27r351h14c3975_1 . Done .
            Pulling image: quay.io/biocontainers/homer:4.10--pl526hc9558a2_0 . Done .
            Pulling image: ubuntu:18.04 . Done
            Building image: r-3.5_ubuntu-18.04 . Done  Done
    localhost:~>

This process should create a project organizational structure like this:

.. code-block:: bash

    localhost:~> tree chipseq-hmgn1
    chipseq-hmgn1
    .
    ├── bin
    │   └── cwl-ngs-workflows-cbb (CWL workflow repo cloned here)
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA481982
    ├── doc
    ├── index.html
    ├── LICENSE
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   └── 04 - Peak Calling.ipynb
    ├── README.md
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA481982
    ├── src
    ├── tmp
    └── venv
        ├── bin
        ├── etc
        ├── include
        ├── lib
        ├── lib64 -> lib
        ├── LICENSE.txt
        ├── locale
        ├── README.md
        ├── README.rst
        ├── setup.cfg
        └── share

    20 directories, 14 files

Now you should copied the **factors.txt** file to the directory: **data/PRJNA481982**.

After this process, **cookiecutter** should have pulled all docker images require by the project.

ChIP-Seq workflow usage with Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For start using the workflow you need to activate the Python environment inside the project.

.. code-block:: bash

    localhost:~> source venv/bin/activate

Then, you can start the jupyter notebooks now.

.. code-block:: bash

    localhost:~> jupyter notebook

If the workflow is deployed in a remote machine using SSH access the correct way to start the notebooks is:

.. code-block:: bash

    localhost:~> jupyter notebook --no-browser --ip='0.0.0.0'

In this case the option **--ip='0.0.0.0'** will server the Jupyter notebook on all network interfaces and you can access
them from your desktop browser using the port returned by the Jupyter server.

Finally, you should navigate in your browser to the **notebooks** directory and start executing all notebooks by their
order leaving the **00 - Project Report.ipynb** to the end.

Jupyter Notebook Server
-----------------------

Top-level directories from the Jupyter server viewed in a web browser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /img/top-level-structure.png
    :width: 800px
    :align: center
    :alt: Top-level directories from the Jupyter server viewed in a web browser

Notebook generated fro the ChIP-Seq data analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /img/chipseq-notebooks.png
    :width: 800px
    :align: center
    :alt: Notebook generated fro the ChIP-Seq data analysis

CWL workflows
-------------

.. include:: /cwl/sra_workflow.rst
.. include:: /cwl/trimmomatic.rst
.. include:: /cwl/chip-seq-alignment.rst
.. include:: /cwl/peak-caller-MACS2.rst
.. include:: /cwl/differential_binding-DiffBind.rst

Test Project
------------

A test project is available (read-only) at https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/chipseq-hmgn1

Extra requirements
------------------

Configuring Homer databases
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Homer needs organism, promoter and genome databases for the annotation process. These databases are not distributed with
the default installation package.

The users need to install the specific databases for the organism analyzed in their projects. The next example is for
mouse.

**Using Conda**

.. code-block:: bash

    localhost:~> conda activate /home/veraalva/chipseq-hmgn1/bin/bioconda
    localhost:~> perl /home/veraalva/chipseq-hmgn1/bin/bioconda/share/homer-4.10-0/configureHomer.pl -install mouse-o mouse-p mm9
    localhost:~> perl /home/veraalva/chipseq-hmgn1/bin/bioconda/share/homer-4.10-0/configureHomer.pl -list | grep -v "^-"

        Current base directory for HOMER is /home/veraalva/chipseq-hmgn1/bin/bioconda/share/homer-4.10-0/

    --2019-08-30 12:05:27--  http://homer.ucsd.edu/homer/update.txt
    Resolving homer.ucsd.edu (homer.ucsd.edu)... 169.228.63.226
    Connecting to homer.ucsd.edu (homer.ucsd.edu)|169.228.63.226|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 16187 (16K) [text/plain]
    Saving to: ‘/home/veraalva/chipseq-hmgn1/bin/bioconda/share/homer-4.10-0//update.txt’

    /gfs/projects/ngs_templates/cookiecutter/chips 100%[===================================================================================================>]  15.81K  --.-KB/s    in 0.07s

    2019-08-30 12:05:28 (211 KB/s) - ‘/home/veraalva/chipseq-hmgn1/bin/bioconda/share/homer-4.10-0//update.txt’ saved [16187/16187]

        Updating Settings...
    Packages with name conflicts have a trailing -o, -p, or -g
    Version Installed	Package	Version	Description
    SOFTWARE
    +	homer	v4.10.4	Code/Executables, ontologies, motifs for HOMER
    ORGANISMS
    +	mouse-o	v6.0	Mus musculus (mouse) accession and ontology information
    PROMOTERS
    +	mouse-p	v5.5	mouse promoters (mouse)
    GENOMES
    +	mm9	v6.0	mouse genome and annotation for UCSC mm9
    SETTINGS

**Using Docker**

A directory named **data/homer** will be used to store all homer configuration and databases.

.. code-block:: bash

    localhost:~> cd chipseq-hmgn1/data
    localhost:~> mkdir -p homer
    localhost:~> docker run -u `id -u`:`id -g` -i -t -v `pwd`/homer:/data quay.io/biocontainers/homer:4.10--pl526hc9558a2_0 cp /usr/local/share/homer-4.10-0/config.txt /data/
    localhost:~> docker run -u `id -u`:`id -g` -i -t -v `pwd`/homer:/data quay.io/biocontainers/homer:4.10--pl526hc9558a2_0 cp /usr/local/share/homer-4.10-0/update.txt /data/
    localhost:~> docker run -u `id -u`:`id -g` -i -t -v `pwd`/homer:/data quay.io/biocontainers/homer:4.10--pl526hc9558a2_0 cp -rf /usr/local/share/homer-4.10-0/data /data/
    localhost:~> docker run -i -t -v `pwd`/homer/config.txt:/usr/local/share/homer-4.10-0/config.txt -v `pwd`/homer/update.txt:/usr/local/share/homer-4.10-0/update.txt -v `pwd`/homer/data:/usr/local/share/homer-4.10-0/data  quay.io/biocontainers/homer:4.10--pl526hc9558a2_0 perl /usr/local/share/homer-4.10-0/configureHomer.pl -install mouse-o mouse-p mm9
    localhost:~> docker run -i -t -v `pwd`/homer/config.txt:/usr/local/share/homer-4.10-0/config.txt -v `pwd`/homer/update.txt:/usr/local/share/homer-4.10-0/update.txt -v `pwd`/homer/data:/usr/local/share/homer-4.10-0/data  quay.io/biocontainers/homer:4.10--pl526hc9558a2_0 perl /usr/local/share/homer-4.10-0/configureHomer.pl -list | grep -v "^-"

        Current base directory for HOMER is /usr/local/share/homer-4.10-0/

    Connecting to homer.ucsd.edu (169.228.63.226:80)
    update.txt           100% |*******************************| 16187   0:00:00 ETA
        Updating Settings...
    Packages with name conflicts have a trailing -o, -p, or -g
    Version Installed	Package	Version	Description
    SOFTWARE
    +	homer	v4.10.4	Code/Executables, ontologies, motifs for HOMER
    ORGANISMS
    +	mouse-o	v6.0	Mus musculus (mouse) accession and ontology information
    PROMOTERS
    +	mouse-p	v5.5	mouse promoters (mouse)
    GENOMES
    +	mm9	v6.0	mouse genome and annotation for UCSC mm9
    SETTINGS
