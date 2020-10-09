.. _chipseqPipeline:

Differential Binding detection from ChIP-Seq data
=================================================

Differential binding analysis pipeline from ChIP-Seq data.

The workflow is comprised of five steps, as shown in next table. The first step, sample download and quality control,
is for downloading samples from the NCBI SRA database, if necessary, or for executing the pre-processing quality
control tools on all samples. Sample trimming and alignment are executed next. Post-processing quality control on
ChIP-Seq samples is executed using Phantompeakqualtools, as recommended by the ENCODE consortia].
Then, a peak calling step is performed using MACS2, and peak annotation is executed with Homer.
Peak reproducibility is explored with IDR. Finally, a differential binding analysis is completed with DiffBind.

.. table:: Differential binding analysis, ChIP-Seq pipeline
    :widths: 15 15 15 13 10 12 20

    +------------------------+----------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Step                   | Jupyter Notebook                       | Workflow CWL                           | Tool            | Input         | Output              | CWL Tool                         |
    +========================+========================================+========================================+=================+===============+=====================+==================================+
    | Sample Download        | `01 - Pre-processing QC`_              | `download_quality_control.cwl`_        | SRA-Tools       | SRA accession | Fastq               | `fastq-dump.cwl`_                |
    | and Quality Control    |                                        |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                        |                                        | FastQC          | Fastq         | FastQC HTML and Zip | `fastqc.cwl`_                    |
    +------------------------+----------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Trimming               | `02 - Samples trimming`_               |                                        | Trimmomatic     | Fastq         | Fastq               | `trimmomatic-PE.cwl`_            |
    |                        |                                        |                                        |                 |               |                     |                                  |
    |                        |                                        |                                        |                 |               |                     | `trimmomatic-SE.cwl`_            |
    +------------------------+----------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Alignments and         | `03 - Alignments`_                     |    `chip-seq-alignment.cwl`_           | BWA             | Fastq         | BAM                 | `bwa-mem.cwl`_                   |
    | Quantification         |                                        |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                        |                                        | Samtools        | SAM           | BAM                 | `samtools-view.cwl`_             |
    |                        |                                        |                                        |                 |               |                     |                                  |
    |                        |                                        |                                        |                 |               | Sorted BAM          | `samtools-sort.cwl`_             |
    |                        |                                        |                                        |                 |               |                     |                                  |
    |                        |                                        |                                        |                 |               | BAM index           | `samtools-index.cwl`_            |
    |                        |                                        |                                        |                 |               |                     |                                  |
    |                        |                                        |                                        |                 |               | BAM stats           | `samtools-stats.cwl`_            |
    |                        |                                        |                                        |                 |               |                     |                                  |
    |                        |                                        |                                        |                 |               | BAM flagstats       | `samtools-flagstat.cwl`_         |
    +------------------------+----------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Peak Calling           | `04 - Peak Calling and IDR`_           |  `peak-calling-MACS2.cwl`_             | IGVtools        | Sorted BAM    | TDF                 | `igvtools-count.cw`_             |
    |                        |                                        |                                        +-----------------+---------------+---------------------+----------------------------------+
    | and IDR                |                                        |                                        | MACS2           | tagAlign      | Peaks (TSV), plots  | `macs2-callpeak.cwl`_            |
    |                        |                                        |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                        |                                        | Homer           | BAM           | Annotation (TSV)    | `homer-annotatePeaks.cwl`_       |
    |                        |                                        |                                        |                 |               | FPKM values (TSV)   |                                  |
    |                        |                                        |                                        |                 |               |                     | `homer-makeTagDirectory.cwl`_    |
    |                        |                                        |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                        |                                        | IDR             | Peaks         | Peaks (TSV), plots  | `idr.cwl`_                       |
    +------------------------+----------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Differential binding   | `05 - Differential binding Detection`_ |                                        | DiffBind        | Read Matrix   | Peaks (TSV), plots  | `diffBind.cwl`_                  |
    | Analysis               |                                        |                                        |                 |               |                     |                                  |
    +------------------------+----------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+


Input requirements
------------------

The input requirement for the ChIPSeq pipeline is the :ref:`sampleSheet` file.

Pipeline command line
---------------------

The ChIPSeq based project can be created using the following command line:

.. code-block:: bash

    localhost:~> pm4ngs-chipseq
    usage: Generate a PM4NGS project for ChIPSeq data analysis [-h] [-v]
                                                           --sample-sheet
                                                           SAMPLE_SHEET
                                                           [--config-file CONFIG_FILE]
                                                           [--copy-rawdata]

.. topic:: Options:

    * **sample-sheet**: Sample sheet with the samples metadata
    * **config-file**: YAML file with configuration for project creation
    * **copy-rawdata**: Copy the raw data defined in the sample sheet to the project structure. (The data can be hosted locally or in an http server)

Creating the Differential Binding detection from ChIP-Seq data project
----------------------------------------------------------------------

The **pm4ngs-chipseq** command line executed with the **--sample-sheet** option will let you type the different variables
required for creating and configuring the project. The default value for each variable is shown in the brackets. After
all questions are answered, the CWL workflow files will be
cloned from the github repo `ncbi/cwl-ngs-workflows-cbb`_ to the folder **bin/cwl**.

.. _ncbi/cwl-ngs-workflows-cbb: https://github.com/ncbi/cwl-ngs-workflows-cbb

.. code-block:: bash

    localhost:~> pm4ngs-chipseq --sample-sheet my-sample-sheet.tsv
    Generating ChIP-Seq data analysis project
    author_name [Roberto Vera Alvarez]:
    email [veraalva@ncbi.nlm.nih.gov]:
    project_name [my_ngs_project]:
    dataset_name [my_dataset_name]:
    is_data_in_SRA [None]:
    Select sequencing_technology:
    1 - single-end
    2 - paired-end
    Choose from 1, 2 [1]: 2
    create_demo [y]:
    number_spots [1000000]:
    organism [human]:
    genome_name [hg38]:
    genome_dir [hg38]:
    aligner_index_dir [hg38/BWA]:
    genome_fasta [hg38/genome.fa]:
    genome_gtf [hg38/genome.gtf]:
    genome_mappable_size [hg38]:
    fdr [0.05]:
    use_docker [y]:
    max_number_threads [16]:
    Cloning Git repo: https://github.com/ncbi/cwl-ngs-workflows-cbb to /Users/veraalva/my_ngs_project/bin/cwl
    Updating CWLs dockerPull and SoftwareRequirement from: /Users/veraalva/my_ngs_project/requirements/conda-env-dependencies.yaml
    bedtools with version 2.29.2 update image to: quay.io/biocontainers/bedtools:2.29.2--hc088bd4_0
        /Users/veraalva/my_ngs_project/bin/cwl/tools/bedtools/bedtools-docker.yml with old image replaced: quay.io/biocontainers/bedtools:2.28.0--hdf88d34_0
    bioconductor-diffbind with version 2.16.0 update image to: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_0
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/deseq2-pca.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/macs-cutoff.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/dga_heatmaps.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/diffbind.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/edgeR-2conditions.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/volcano_plot.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/readQC.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/deseq2-2conditions.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
    bwa with version 0.7.17 update image to: quay.io/biocontainers/bwa:0.7.17--hed695b0_7
        /Users/veraalva/my_ngs_project/bin/cwl/tools/bwa/bwa-docker.yml with old image replaced: quay.io/biocontainers/bwa:0.7.17--h84994c4_5
    homer with version 4.11 update image to: quay.io/biocontainers/homer:4.11--pl526h9a982cc_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/homer/homer-docker.yml with old image replaced: quay.io/biocontainers/homer:4.11--pl526h2bce143_2
    Copying file /Users/veraalva/Work/Developer/Python/pm4ngs/pm4ngs-chipseq/example/pm4ngs_chipseq_demo_sample_data.csv  to /Users/veraalva/my_ngs_project/data/my_dataset_name/sample_table.csv
    6 files loaded
    Using table:
      sample_name file condition  replicate
    0  SRR7549105             ES          1
    1  SRR7549106             ES          2
    2  SRR7549109            MEF          1
    3  SRR7549110            MEF          2
    4  SRR7549114             rB          1
    5  SRR7549113             rB          2
     Done

The **pm4ngs-chipseq** command line will create a project structure as:

.. code-block:: bash

    .
    ├── LICENSE
    ├── README.md
    ├── bin
    │   └── cwl
    ├── config
    │   └── init.py
    ├── data
    │   └── my_dataset_name
    ├── doc
    ├── index.html
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   ├── 04 - Peak Calling and IDR.ipynb
    │   └── 05 - Differential binding Detection.ipynb
    ├── requirements
    │   └── conda-env-dependencies.yaml
    ├── results
    │   └── my_dataset_name
    ├── src
    └── tmp

    12 directories, 11 files

.. note:: **ChIP-Seq based project variables**

    * **author_name**:
        Default: [Roberto Vera Alvarez]
    * **email**:
        Default: [veraalva@ncbi.nlm.nih.gov]
    * **project_name**:
        Name of the project with no space nor especial characters. This will be used as project folder's name.

        Default: [my_ngs_project]
    * **dataset_name**:
        Dataset to process name with no space nor especial characters. This will be used as folder name to group the
        data. This folder will be created under the **data/{{dataset_name}}** and **results/{{dataset_name}}**.

        Default: [my_dataset_name]
    * **is_data_in_SRA**:
        If the data is in the SRA set this to y. A CWL workflow to download the data from the SRA database to the
        folder **data/{{dataset_name}}** and execute FastQC on it will be included in the **01 - Pre-processing QC.ipynb** notebook.

        Set this option to **n**, if the fastq files names and location are included in the sample sheet.

        Default: [y]
    * **Select sequencing_technology**:
        Select one of the available sequencing technologies in your data.

        Values: 1 - single-end, 2 - paired-end
    * **create_demo**:
        If the data is downloaded from the SRA and this option is set to y, only the number of spots specified
        in the next variable will be downloaded. Useful to test the workflow.

        Default: [y]: y
    * **number_spots**:
        Number of sport to download from the SRA database. It is ignored is the **create_demo** is set to **n**.

        Default: [1000000]
    * **organism**:
        Organism to process, e.g. human. This is used to link the selected genes to the NCBI gene database.

        Default: [human]
    * **genome_name**:
        Genome name , e.g. hg38 or mm10.

        Default: [hg38]
    * **genome_dir**:
        Absolute path to the directory with the genome annotation (genome.fa, genes.gtf) to be used by the workflow
        or the name of the genome.

        If the name of the genome is used, PM4NGS will include a cell in the
        **03 - Alignments.ipynb** notebook to download the genome files.
        The genome data will be at **data/{{dataset_name}}/{{genome_name}}/**

        Default: [hg38]
    * **aligner_index_dir**:
        Absolute path to the directory with the genome indexes for BWA.

        If **{{genome_name}}/BWA** is used, PM4NGS will include a cell in the
        **03 - Alignments.ipynb** notebook to create the genome indexes for BWA.

        Default: [hg38/BWA]
    * **genome_fasta**:
        Absolute path to the genome fasta file

        If **{{genome_name}}/genome.fa** is used, PM4NGS will use the downloaded fasta file.

        Default: [hg38/genome.fa]
    * **genome_gtf**:
        Absolute path to the genome GTF file

        If **{{genome_name}}/genes.gtf** is used, PM4NGS will use the downloaded GTF file.

        Default: [hg38/gene.gtf]
    * **genome_bed**:
        Absolute path to the genome BED file

        If **{{genome_name}}/genes.bed** is used, PM4NGS will use the downloaded BED file.

        Default: [hg38/genes.bed]
    * **genome_mappable_size**:
        Genome mappable size used by MACS. For human can be hg38 or in case of other genomes it is a number.

        Default: [hg38]
    * **fdr**:
        Adjusted P-Value to be used as cutoff in the DG analysis, e.g. 0.05.

        Default: [0.05]
    * **use_docker**:
        Set this to y if you will be using Docker. Otherwise Conda needs to be installed in the computer.

        Default: [y]
    * **max_number_threads**:
        Number of threads available in the computer.

        Default: [16]


Jupyter server
--------------

PM4NGS uses Jupyter as interface for users. After project creation the jupyter server should be started as shown below.
The server will open a browser windows showing the project's structure just created.

.. code-block:: bash

    localhost:~> jupyter notebook

Data processing
---------------

Start executing the notebooks from 01 to 05 waiting for each step completion. The **00 - Project Report.ipynb** notebook
can be executed after each notebooks to see the progress in the analysis.

CWL workflows
-------------

.. include:: /cwl/sra_workflow.rst
.. include:: /cwl/trimmomatic.rst
.. include:: /cwl/chip-seq-alignment.rst
.. include:: /cwl/peak-caller-MACS2.rst
.. include:: /cwl/meme-motif.rst
.. include:: /cwl/differential_binding-DiffBind.rst

Demo
----

PM4NGS includes a demo project that users can use to test the framework. It is pre-configured to use Docker as execution
environment.

The ChIPSeq based demo process samples from the BioProject PRJNA481982_.

Use this command to create the project structure in your local computer

.. code-block:: bash

    localhost:~> pm4ngs-chipseq-demo

Once it finish, start the jupyter server and execute the notebooks as it is indicated on them

.. code-block:: bash

    localhost:~> jupyter notebook
    [I 14:12:52.956 NotebookApp] Serving notebooks from local directory: /home/veraalva
    [I 14:12:52.956 NotebookApp] Jupyter Notebook 6.1.4 is running at:
    [I 14:12:52.956 NotebookApp] http://localhost:8888/?token=eae6a8d42ad12d6ace23f5d0923bcec14d0f798127750122
    [I 14:12:52.956 NotebookApp]  or http://127.0.0.1:8888/?token=eae6a8d42ad12d6ace23f5d0923bcec14d0f798127750122
    [I 14:12:52.956 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmatio
    n).
    [C 14:12:52.959 NotebookApp]

        To access the notebook, open this file in a browser:
            file:///home/veraalva/.local/share/jupyter/runtime/nbserver-23251-open.html
        Or copy and paste one of these URLs:
            http://localhost:8888/?token=eae6a8d42ad12d6ace23f5d0923bcec14d0f798127750122
         or http://127.0.0.1:8888/?token=eae6a8d42ad12d6ace23f5d0923bcec14d0f798127750122


The results of this analysis is `https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/chipseq-hmgn1/`_

.. _01 - Pre-processing QC: https://github.com/ncbi/pm4ngs-rnaseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/01%20-%20Pre-processing%20QC.ipynb
.. _download_quality_control.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/sra/download_quality_control.cwl
.. _fastq-dump.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/sra-tools/fastq-dump.cwl
.. _fastqc.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/fastqc/fastqc.cwl

.. _02 - Samples trimming: https://github.com/ncbi/pm4ngs-rnaseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/02%20-%20Samples%20trimming.ipynb
.. _trimmomatic-PE.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/trimmomatic/trimmomatic-PE.cwl
.. _trimmomatic-SE.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/trimmomatic/trimmomatic-SE.cwl

.. _03 - Alignments: https://github.com/ncbi/pm4ngs-chipseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/03%20-%20Alignments.ipynb
.. _chip-seq-alignment.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/ChIP-Seq/chip-seq-alignment.cwl
.. _bwa-mem.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/bwa/bwa-mem.cwl
.. _samtools-flagstat.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-flagstat.cwl
.. _samtools-index.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-index.cwl
.. _samtools-sort.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-sort.cwl
.. _samtools-stats.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-stats.cwl
.. _samtools-view.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-view.cwl
.. _igvtools-count.cw: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/igvtools/igvtools-count.cwl

.. _04 - Peak Calling and IDR: https://github.com/ncbi/pm4ngs-chipseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/04%20-%20Peak%20Calling%20and%20IDR.ipynb
.. _peak-calling-MACS2.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/ChIP-Seq/peak-calling-MACS2.cwl
.. _macs2-callpeak.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/macs/macs2-callpeak.cwl
.. _homer-annotatePeaks.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/homer/homer-annotatePeaks.cwl
.. _homer-makeTagDirectory.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/homer/homer-makeTagDirectory.cwl
.. _idr.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/idr/idr.cwl

.. _05 - Differential binding Detection: https://github.com/ncbi/pm4ngs-chipseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/05%20-%20Differential%20binding%20Detection.ipynb
.. _diffBind.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/R/diffbind.cwl

.. _PRJNA481982: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA481982
.. _`https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/chipseq-hmgn1/`: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/chipseq-hmgn1/
