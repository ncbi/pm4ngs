Installation
=============

Project Templates with Python virtual environment
-------------------------------------------------

Install Cookiecutter and other basic Python packages using the **requirements.txt** file.

.. code-block:: bash

    perseo:~> virtualenv venv-templates
    perseo:~> source venv-templates/bin/activate
    perseo:~> pip install -r https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/requirements.txt


Project Templates with Conda/BioConda
-------------------------------------

Conda_ should be already installed and configured.

.. code-block:: bash

    perseo:~> wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
    perseo:~> sh Miniconda3-latest-MacOSX-x86_64.sh

A Conda virtual environment will be created with name **templates** using these instructions:

.. code-block:: bash

    perseo:~> wget https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/conda-requirements.yaml
    perseo:~> conda env create -f conda-requirements.yaml

If Conda is installed with prefix **/gfs/conda/conda** you should see the available environments like in this block:

.. code-block:: bash

    perseo:~> conda env list
    # conda environments:
    #
    base                     /gfs/conda
    templates             *  /gfs/conda/envs/templates

    perseo:~>

.. _Conda: https://github.com/conda/conda

Using the Template Project
--------------------------

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

Creating the project structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Execute cookiecutter with the **cwl-ngs-workflows-cbb** repo:

.. code-block:: bash

    cookiecutter https://github.com/ncbi/cookiecutter-jupyter-rnaseq.git

You'll be prompted for some values.

.. code-block:: yaml

    author_name: "Roberto Vera Alvarez"
    user_email: "veraalva@ncbi.nlm.nih.gov"
    project_name: "rnaseq-sra-single"
    dataset_name: "PRJNA339968"
    is_data_in_SRA: "y"
    ngs_data_type: "RNA-Seq"
    sequencing_technology: "single-end"
    create_demo: "y"
    number_spots: "2000000"
    organism: "human"
    genome_dir: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38"
    genome_name: "hg38"
    aligner_index_dir: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/STAR"
    genome_fasta: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genome.fa"
    genome_gtf: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genes.gtf"
    genome_gff: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genes.gff"
    genome_gff3: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genes.gff3"
    genome_bed: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genes.bed"
    genome_mappable_size: "hg38"
    genome_blacklist: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/hg38-blacklist.bed"
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

Then a project folder will be created for you following this structure. I'm including here all files created after
processing the samples.

.. code-block:: text

    rnaseq-sra-single
    ├── LICENSE
    ├── README.md
    ├── bin
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA339968
    |       └── factors.txt
    ├── index.html
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   ├── 04 - Quantification.ipynb
    │   ├── 05 - DGA.ipynb
    │   └── 06 - GO enrichment.ipynb
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA339968
    ├── src
    ├── tmp
    └── venv

Then, copy a manually created **factors.txt** to the folder **data/PRJNA339968**.

The "factors.txt" file is the file where the initial data files and metadata are specified.
It should have the columns:

+----------------+------------+--------------+-----------+
| id             | SampleID   | condition    | replicate |
+================+============+==============+===========+
| classical01    | SRR4053795 | classical    | 1         |
+----------------+------------+--------------+-----------+
| classical01    | SRR4053796 | classical    | 2         |
+----------------+------------+--------------+-----------+
| nonclassical01 | SRR4053802 | nonclassical | 1         |
+----------------+------------+--------------+-----------+
| nonclassical01 | SRR4053803 | nonclassical | 2         |
+----------------+------------+--------------+-----------+


If the project option **is_data_in_SRA** is set to **y** (Yes) the **01 - Pre-processing QC.ipynb** will use the
**SampleID** to download the files from the NCBI SRA database using fastq-dump. If the data is **single-end**
you will see one file per sample **SRR4053795.fastq.gz**. However, if the data is paired-end you will see two
files per samples **SRR4053795_1.fastq.gz** and **SRR4053795_2.fastq.gz**

If the project option **is_data_in_SRA** is set to **n** (No) you should place your **fastq** files in the
**data/PRJNA339968** (this folder will have the value of the **dataset_name** specified during project creation)
folder using the **SampleID** column as the prefix of your sample leaving out the **.fastq.gz**.
