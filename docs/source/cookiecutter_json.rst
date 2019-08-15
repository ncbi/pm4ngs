Project Description YAML file
=============================

Cookiecutter accept a YAML file as a config file for the project template creation. This YAML file is created from the
parameters:

.. code-block:: json
    :linenos:

    {
        "author_name": "Roberto Vera Alvarez",
        "email": "veraalva@ncbi.nlm.nih.gov",
        "project_name": "my_ngs_project",
        "dataset_name": "my_dataset_name",
        "is_data_in_SRA": "y" or "n",
        "ngs_data_type": ["RNA-Seq", "ChIP-Seq", "ChIP-exo"],
        "sequencing_technology": ["single-end", "paired-end"],
        "create_demo": "y" or "n",
        "number_spots": "5000000",
        "organism": "human",
        "genome_dir": "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg19",
        "genome_name": "hg19",
        "aligner_index_dir": "{{ cookiecutter.genome_dir }}/ALIGNER",
        "genome_fasta": "{{ cookiecutter.genome_dir }}/genome.fa",
        "genome_gtf": "{{ cookiecutter.genome_dir }}/genome.gtf",
        "genome_gff": "{{ cookiecutter.genome_dir }}/genome.gff",
        "genome_gff3": "{{ cookiecutter.genome_dir }}/genome.gff3",
        "genome_bed": "{{ cookiecutter.genome_dir }}/genome.bed",
        "genome_chromsizes": "{{ cookiecutter.genome_dir }}/genome.sizes",
        "genome_mappable_size": "hg19",
        "genome_blacklist": "{{ cookiecutter.genome_dir }}/hg19-blacklist.bed",
        "fold_change": "2.0",
        "fdr": "0.05",
        "use_docker": "y" or "n",
        "pull_images": "y" or "n",
        "use_conda": "y" or "n",
        "cwl_runner": "cwl-runner",
        "cwl_workflow_repo": "https://github.com/ncbi/cwl-ngs-workflows-cbb",
        "create_virtualenv": "y" or "n",
        "use_gnu_parallel": "y" or "n",
        "max_number_threads": "16"
    }

.. topic:: Parameters

    * **author_name**: Project author name
    * **email**: Author's email
    * **project_name**: Name of the project with no space nor especial characters. This will be used as project folder's
      name.
    * **dataset_name**: Dataset to process name with no space nor especial characters. This will be used as folder name to
      group the data. This folder will be created under the **data/{{dataset_name}}** and **results/{{dataset_name}}**.
    * **is_data_in_SRA**: If the data is in the SRA set this to **y**. A CWL workflow to download the data from the SRA
      database to the folder **data/{{dataset_name}}** and execute FastQC on it will be included in the
      **01 - Pre-processing QC.ipynb** notebook.
    * **ngs_data_type**: Select one of the available technologies to process:
        1. RNA-Seq
        2. ChIP-Seq
        3. ChIP-exo
    * **sequencing_technology**: Select one of the available sequencing technologies in your data:
        1. single-end
        2. paired-end
      Mixed datasets with single and paired-end samples should be processed independently.
    * **create_demo**: If the data is downloaded from the SRA and this option is set to **y**, then only the number of
      spots specified in the next variable will be downloaded. Useful to test the workflow.
    * **number_spots**: Number of sport to download from the SRA database. It is ignored is the **create_demo** is set
      to **n**.
    * **organism**: Organism to process, e.g. human. This is used to link the selected genes to the NCBI gene database.
    * **genome_dir**: Absolute path to the directory with the genome annotation to be used by the workflow.
    * **genome_name**: Genome name , e.g. hg38 or mm10.
    * **aligner_index_dir**: Absolute path to the directory with the aligner indexes.
    * **genome_fasta**: Absolute path to the directory to the genome fasta.
    * **genome_gtf**: Absolute path to the directory with the genome GTF.
    * **genome_gff**: Absolute path to the directory with the genome GFF.
    * **genome_gff3**: Absolute path to the directory with the genome GFF3.
    * **genome_bed**: Absolute path to the directory with the genome BED.
      All these files are note required to exist. It depends on the workflow executed.
    * **genome_chromsizes**: Genome chromosome sizes file like `hg19.chrom.sizes`_.
    * **genome_mappable_size**: Genome mappable size used by MACS. For human can be hg38 or in case of other genomes
      it is a number.
    * **genome_blacklist**: Genome blacklist file.
    * **fold_change**: A real number used as fold change value, e.g. 2.0.
    * **fdr**: Adjusted P-Value to be used, e.g. 0.05.
    * **use_docker**: Set this to **y** if you will be using Docker.
    * **pull_images**: Set this to **y** if you want pull the required docker images during the project structure
      creation.
    * **use_conda**: Set this to **y** if you want to use Conda. The environments required by the **ngs_data_type**
      to process will be installed during the project structure creation.
    * **cwl_runner**: Absulute path to the cwl-runner.
    * **cwl_workflow_repo**: Always use: https://github.com/ncbi/cwl-ngs-workflows-cbb. This repo will be cloned in the
      **bin** folder.
    * **create_virtualenv**: Set this to **y** if not using Docker nor Conda for creating a Python virtual environment
      in a folder **venv**.
    * **use_gnu_parallel**: Use `GNU Parallel`_ for parallel execution of the jobs.
    * **max_number_threads**: Number of threads available in the host

.. _hg19.chrom.sizes: http://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.chrom.sizes
.. _GNU Parallel: https://www.gnu.org/software/parallel/
