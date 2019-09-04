Differential Gene expression from RNA-Seq data
==============================================

.. warning::  Read the :doc:`Background Information </background_information>` before proceeding with these steps

.. warning::
   Read the :doc:`Project Templates Installation </envs/installation>` notes to have the **cookiecutter** available
   in you shell depending on the execution environment you will be using.

.. include:: /extra/factors_file.rst

Installation
------------

RNA-Seq workflow with Conda/Bioconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The RNA-Seq project structure is created using the conda environment named **templates**.

First step is to activate the  **templates** environment:

.. code-block:: bash

    localhost:~> conda activate templates

Then, a YAML file (for this example I will call this file: **rnaseq-sra-paired.yaml**) with your project detail should
be created.

.. code-block:: yaml
    :linenos:

    default_context:
      author_name: "Roberto Vera Alvarez"
      user_email: "veraalva@ncbi.nlm.nih.gov"
      project_name: "rnaseq-sra-paired"
      dataset_name: "PRJNA290924"
      is_data_in_SRA: "y"
      ngs_data_type: "RNA-Seq"
      sequencing_technology: "paired-end"
      create_demo: "y"
      number_spots: "1000000"
      organism: "human"
      genome_dir: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38"
      genome_name: "hg38"
      aligner_index_dir: "{{ cookiecutter.genome_dir}}/STAR"
      genome_fasta: "{{ cookiecutter.genome_dir}}/genome.fa"
      genome_gtf: "{{ cookiecutter.genome_dir}}/genes.gtf"
      genome_gff: "{{ cookiecutter.genome_dir}}/genes.gff"
      genome_gff3: "{{ cookiecutter.genome_dir}}/genes.gff3"
      genome_bed: "{{ cookiecutter.genome_dir}}/genes.bed"
      genome_chromsizes: "{{ cookiecutter.genome_dir}}/chrom.sizes"
      genome_mappable_size: "hg38"
      genome_blacklist: "{{ cookiecutter.genome_dir}}/hg38-blacklist.bed"
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

After the **rnaseq-sra-paired.yaml** is created the project structure should be created using this command obtaining the
following output.

.. code-block:: bash

    localhost:~> cookiecutter --no-input --config-file rnaseq-sra-paired.yaml https://github.com/ncbi/cookiecutter-jupyter-ngs.git
    Checking RNA-Seq workflow dependencies .......... Done
    localhost:~>

This process should create a project organizational structure like this:

.. code-block:: bash

    localhost:~> tree rnaseq-sra-paired
    rnaseq-sra-paired
    ├── bin
    │   ├── bioconda (This directory include a conda envs for all bioinfo tools)
    │   ├── cwl-ngs-workflows-cbb (CWL workflow repo cloned here)
    │   └── jupyter (This directory include a conda envs for Jupyter notebooks)
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA290924
    ├── doc
    ├── index.html
    ├── LICENSE
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   ├── 04 - Quantification.ipynb
    │   ├── 05 - DGA.ipynb
    │   └── 06 - GO enrichment.ipynb
    ├── README.md
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA290924
    ├── src
    └── tmp

    14 directories, 12 files

Now you should copied the **factors.txt** file to the folder: **data/PRJNA290924**.

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
                             /home/veraalva/rnaseq-sra-paired/bin/bioconda
                             /home/veraalva/rnaseq-sra-paired/bin/jupyter

    localhost:~>

Please, note that the Conda prefix **/gfs/conda** will be different in you host. Also, note that the **bioconda** and
**jupyter** envs are inside the **bin** directory of your project keeping them static inside the project organizational
structure.

RNA-Seq workflow usage with Conda/Bioconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For start using the workflow you need to activate the conda environments **bioconda** and **jupyter**.

.. code-block:: bash

    localhost:~> conda activate /home/veraalva/rnaseq-sra-paired/bin/bioconda
    localhost:~> conda activate --stack /home/veraalva/rnaseq-sra-paired/bin/jupyter

Note the **--stack** option to have both environment working at the same time. Also, the order is important, **bioconda**
should be activated before **jupyter**.

Test the conda envs:

.. code-block:: bash

    localhost:~> which fastqc
    /home/veraalva/rnaseq-sra-paired/bin/bioconda/bin/fastqc
    localhost:~> which jupyter
    /home/veraalva/rnaseq-sra-paired/bin/jupyter/bin/jupyter

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

RNA-Seq workflow with Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, the RNA-Seq project structure is created using the Python virtual environment as described
:doc:`here </envs/installation>`

First step is to activate the Python virtual environment.

.. code-block:: bash

    localhost:~> source venv-templates/bin/activate

Then, a YAML file (for this example I will call this file: **rnaseq-sra-paired.yaml**) with your project detail should
be created.

.. code-block:: yaml
    :linenos:

    default_context:
      author_name: "Roberto Vera Alvarez"
      user_email: "veraalva@ncbi.nlm.nih.gov"
      project_name: "rnaseq-sra-paired"
      dataset_name: "PRJNA290924"
      is_data_in_SRA: "y"
      ngs_data_type: "RNA-Seq"
      sequencing_technology: "paired-end"
      create_demo: "y"
      number_spots: "1000000"
      organism: "human"
      genome_dir: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38"
      genome_name: "hg38"
      aligner_index_dir: "{{ cookiecutter.genome_dir}}/STAR"
      genome_fasta: "{{ cookiecutter.genome_dir}}/genome.fa"
      genome_gtf: "{{ cookiecutter.genome_dir}}/genes.gtf"
      genome_gff: "{{ cookiecutter.genome_dir}}/genes.gff"
      genome_gff3: "{{ cookiecutter.genome_dir}}/genes.gff3"
      genome_bed: "{{ cookiecutter.genome_dir}}/genes.bed"
      genome_chromsizes: "{{ cookiecutter.genome_dir}}/chrom.sizes"
      genome_mappable_size: "hg38"
      genome_blacklist: "{{ cookiecutter.genome_dir}}/hg38-blacklist.bed"
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

After the **rnaseq-sra-paired.yaml** is created the project structure should be created using this command obtaining the
following output.

.. code-block:: bash

    localhost:~> cookiecutter --no-input --config-file rnaseq-sra-paired.yaml https://github.com/ncbi/cookiecutter-jupyter-ngs.git
    Cloning Git repo: https://github.com/ncbi/cwl-ngs-workflows-cbb to /home/veraalva/rnaseq-sra-paired/bin/cwl-ngs-workflows-cbb
    Creating a Python3.7 virtualenv
    Installing packages in: /home/veraalva/rnaseq-sra-paired/venv using file /home/veraalva/rnaseq-sra-paired/requirements/python.txt
    Checking RNA-Seq workflow dependencies .
        Pulling image: quay.io/biocontainers/fastqc:0.11.8--1 . Done .
        Pulling image: quay.io/biocontainers/trimmomatic:0.39--1 . Done .
        Pulling image: quay.io/biocontainers/star:2.7.1a--0 . Done .
        Pulling image: quay.io/biocontainers/samtools:1.9--h91753b0_8 . Done .
        Pulling image: quay.io/biocontainers/rseqc:3.0.0--py_3 . Done .
        Pulling image: quay.io/biocontainers/tpmcalculator:0.0.3--hdbb99b9_0 . Done .
        Pulling image: quay.io/biocontainers/igvtools:2.5.3--0 . Done .
        Pulling image: quay.io/biocontainers/sra-tools:2.9.6--hf484d3e_0 . Done .
        Pulling image: ubuntu:18.04 . Done
        Building image: r-3.5_ubuntu-18.04 . Done  Done
    localhost:~>

This process should create a project organizational structure like this:

.. code-block:: bash

    localhost:~> tree rnaseq-sra-paired
    rnaseq-sra-paired
    ├── bin
    │   └── cwl-ngs-workflows-cbb (CWL workflow repo cloned here)
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA290924
    ├── doc
    ├── index.html
    ├── LICENSE
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   ├── 04 - Quantification.ipynb
    │   ├── 05 - DGA.ipynb
    │   └── 06 - GO enrichment.ipynb
    ├── README.md
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA290924
    ├── src
    ├── tmp
    └── venv
        ├── bin
        ├── etc
        ├── include
        ├── lib
        ├── locale
        ├── README.rst
        └── share

    19 directories, 13 files

Now you should copied the **factors.txt** file to the directory: **data/PRJNA238004**.

After this process, **cookiecutter** should have pulled all docker images require by the project.

RNA-Seq workflow usage with Docker
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

Notebook generated fro the Chip-exo data analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /img/rnaseq-notebooks.png
    :width: 800px
    :align: center
    :alt: Notebook generated fro the RNA-Seq data analysis

CWL workflows
-------------

.. include:: /cwl/sra_workflow.rst
.. include:: /cwl/trimmomatic.rst
.. include:: /cwl/rnaseq-star-aligner-workflow.rst
.. include:: /cwl/rnaseq-tpmcalculator-qc-workflow.rst
.. include:: /cwl/rnaseq-dga-workflow.rst
.. include:: /cwl/rnaseq-GO-enrichment-workflow.rst

Test Project
------------

A test project is available (read-only) at https://ftp.ncbi.nlm.nih.gov/pub/cookiecutter-jupyter-ngs/examples/rnaseq-sra-paired

Extra requirements
------------------

Creating STAR indexes
^^^^^^^^^^^^^^^^^^^^^

This workflow uses STAR for sequence alignment. The STAR index creation is not included in the workflow, that's why we
are including an small section here to describe how the STAR indexes can be created.

The **genome.fa** and **genes.gtf** files should be copied to the genome directory.

.. code-block:: bash

    localhost:~> conda activate /home/veraalva/rnaseq-sra-paired/bin/bioconda
    localhost:~> conda activate --stack /home/veraalva/rnaseq-sra-paired/bin/jupyter
    localhost:~> cd rnaseq-sra-paired/data
    localhost:~> mkdir genome
    localhost:~> cd genome
    localhost:~> mkdir STAR
    localhost:~> cd STAR
    localhost:~> cwl-runner --no-container ../../../bin/cwl-ngs-workflows-cbb/tools/STAR/star-index.cwl --runThreadN 16 --genomeDir . --genomeFastaFiles ../genome.fa  --sjdbGTFfile ../genes.gtf
    localhost:~> cd ..
    localhost:~> tree
    .
    ├── genes.gtf
    ├── genome.fa
    └── STAR
        ├── chrLength.txt
        ├── chrNameLength.txt
        ├── chrName.txt
        ├── chrStart.txt
        ├── exonGeTrInfo.tab
        ├── exonInfo.tab
        ├── geneInfo.tab
        ├── Genome
        ├── genomeParameters.txt
        ├── Log.out
        ├── SA
        ├── SAindex
        ├── sjdbInfo.txt
        ├── sjdbList.fromGTF.out.tab
        ├── sjdbList.out.tab
        └── transcriptInfo.tab

    1 directory, 18 files

Here all files inside the directory **STAR** are created by the workflow.

Creating BED files from GTF
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For generating a BED file from a GTF.

The **genes.gtf** file should be copied to the genome directory.

.. code-block:: bash

    localhost:~> conda activate /home/veraalva/rnaseq-sra-paired/bin/bioconda
    localhost:~> conda activate --stack /home/veraalva/rnaseq-sra-paired/bin/jupyter
    localhost:~> cd rnaseq-sra-paired/data
    localhost:~> mkdir genome
    localhost:~> cd genome
    localhost:~> cwl-runner --no-container ../../bin/cwl-ngs-workflows-cbb/workflows/UCSC/gtftobed.cwl --gtf genes.gtf
    localhost:~> tree
    .
    ├── genes.bed
    ├── genes.genePred
    ├── genes.gtf
    └── genome.fa

    0 directory, 4 files

Here the files **genes.bed** and **genes.genePred** are created from the workflow.

