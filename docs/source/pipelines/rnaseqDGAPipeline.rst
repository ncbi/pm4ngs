.. _rnaseqDGAPipeline:

################################################################
Differential Gene expression and GO enrichment from RNA-Seq data
################################################################

Differential expression (DE) analysis allows the comparison of RNA expression levels between multiple conditions.

The differential gene expression and GO enrichment pipeline is comprised of five steps, shown in next Table.
The first step involves downloading samples from the NCBI SRA database, if necessary, or executing the pre-processing
quality control tools on local samples. Subsequently, sample trimming, alignment, and quantification processes are
executed. Once all samples are processed, groups of differentially expressed genes are identified per condition,
using DESeq and EdgeR. Over- and under-expressed genes are reported by each program, and the interception
of their results is computed.

Finally, once differentially expressed genes are identified, a GO enrichment analysis is executed to
provide key biological processes, molecular functions, and cellular components for identified genes.

.. table:: DGA and Go enrichment, RNASeq pipeline
    :widths: 15 15 15 13 10 12 20

    +------------------------+---------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Step                   | Jupyter Notebook                      | Workflow CWL                           | Tool            | Input         | Output              | CWL Tool                         |
    +========================+=======================================+========================================+=================+===============+=====================+==================================+
    | Sample Download        | `01 - Pre-processing QC`_             | `download_quality_control.cwl`_        | SRA-Tools       | SRA accession | Fastq               | `fastq-dump.cwl`_                |
    | and Quality Control    |                                       |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                       |                                        | FastQC          | Fastq         | FastQC HTML and Zip | `fastqc.cwl`_                    |
    +------------------------+---------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Trimming               | `02 - Samples trimming`_              |                                        | Trimmomatic     | Fastq         | Fastq               | `trimmomatic-PE.cwl`_            |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               |                     | `trimmomatic-SE.cwl`_            |
    +------------------------+---------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Alignments and         | `03 - Alignments and Quantification`_ | `rnaseq-alignment-quantification.cwl`_ | STAR            | Fastq         | BAM                 | `star.cwl`_                      |
    | Quantification         |                                       |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                       |                                        | Samtools        | SAM           | BAM                 | `samtools-view.cwl`_             |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               | Sorted BAM          | `samtools-sort.cwl`_             |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               | BAM index           | `samtools-index.cwl`_            |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               | BAM stats           | `samtools-stats.cwl`_            |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               | BAM flagstats       | `samtools-flagstat.cwl`_         |
    |                        |                                       |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                       |                                        | IGVtools        | Sorted BAM    | TDF                 | `igvtools-count.cw`_             |
    |                        |                                       |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                       |                                        | RSeQC           | Sorted BAM    | Alignment quality   | `rseqc-bam_stat.cwl`_            |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               | control             | `rseqc-infer_experiment.cwl`_    |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               | (TXT and PDF)       | `rseqc-junction_annotation.cwl`_ |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               |                     | `rseqc-junction_saturation.cwl`_ |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               |                     | `rseqc-read_distribution.cwl`_   |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               |                     | `rseqc-read_quality.cwl`_        |
    |                        |                                       |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                       |                                        | TPMCalculator   | Sorted BAM    | Read counts (TSV)   | `tpmcalculator.cwl`_             |
    |                        |                                       |                                        |                 |               |                     |                                  |
    |                        |                                       |                                        |                 |               | TPM values (TSV)    |                                  |
    +------------------------+---------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Differential Gene      | `04 - DGA`_                           |                                        | DeSEq2          | Read Matrix   | TSV                 | `deseq2-2conditions.cwl`_        |
    | Analysis               |                                       |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                       |                                        | EdgeR           | Read Matrix   | TSV                 | `edgeR-2conditions.cwl`_         |
    +------------------------+---------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | Go enrichment          | `05 - GO enrichment`_                 |                                        | `goenrichment`_ | gene IDs      | TSV                 |  Python code in the notebook     |
    +------------------------+---------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+


Input requirements
------------------

The input requirement for the DGA pipeline is the :ref:`sampleSheet` file.

Pipeline command line
---------------------

The RNASeq based project can be created using the following command line:

.. code-block:: bash

    localhost:~> pm4ngs-rnaseq
    usage: Generate a PM4NGS project for RNA-Seq data analysis [-h] [-v]
                                                           --sample-sheet
                                                           SAMPLE_SHEET
                                                           [--config-file CONFIG_FILE]
                                                           [--copy-rawdata]

.. topic:: Options:

    * **sample-sheet**: Sample sheet with the samples metadata
    * **config-file**: YAML file with configuration for project creation
    * **copy-rawdata**: Copy the raw data defined in the sample sheet to the project structure. (The data can be hosted locally or in an http server)

Creating the DGA and GO enrichment from RNA-Seq data project
------------------------------------------------------------

The **pm4ngs-rnaseq** command line executed with the **--sample-sheet** option will let you type the different variables
required for creating and configuring the project. The default value for each variable is shown in the brackets. After
all questions are answered, the CWL workflow files will be
cloned from the github repo `ncbi/cwl-ngs-workflows-cbb`_ to the folder **bin/cwl**.

.. _ncbi/cwl-ngs-workflows-cbb: https://github.com/ncbi/cwl-ngs-workflows-cbb

.. code-block:: bash

    localhost:~> pm4ngs-rnaseq --sample-sheet my-sample-sheet.tsv
    Generating RNA-Seq data analysis project
    author_name [Roberto Vera Alvarez]:
    email [veraalva@ncbi.nlm.nih.gov]:
    project_name [my_ngs_project]:
    dataset_name [my_dataset_name]:
    is_data_in_SRA [y]:
    Select sequencing_technology:
    1 - single-end
    2 - paired-end
    Choose from 1, 2 [1]: 2
    create_demo [y]: y
    number_spots [1000000]:
    organism [human]:
    genome_name [hg38]:
    genome_dir [hg38]:
    aligner_index_dir [hg38/STAR]:
    genome_fasta [hg38/genome.fa]:
    genome_gtf [hg38/genes.gtf]:
    genome_bed [hg38/genes.bed]:
    fold_change [2.0]:
    fdr [0.05]:
    use_docker [y]:
    max_number_threads [16]:
    Cloning Git repo: https://github.com/ncbi/cwl-ngs-workflows-cbb to /home/veraalva/tmp/cookiecutter/my_ngs_project/bin/cwl
    Updating CWLs dockerPull and SoftwareRequirement from: /home/veraalva/my_ngs_project/requirements/conda-env-dependencies.yaml
    bioconductor-diffbind with version 2.16.0 update image to: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_0
        /home/veraalva/my_ngs_project/bin/cwl/tools/R/deseq2-pca.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /home/veraalva/my_ngs_project/bin/cwl/tools/R/macs-cutoff.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /home/veraalva/my_ngs_project/bin/cwl/tools/R/dga_heatmaps.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /home/veraalva/my_ngs_project/bin/cwl/tools/R/diffbind.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /home/veraalva/my_ngs_project/bin/cwl/tools/R/edgeR-2conditions.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /home/veraalva/my_ngs_project/bin/cwl/tools/R/volcano_plot.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /home/veraalva/my_ngs_project/bin/cwl/tools/R/readQC.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /home/veraalva/my_ngs_project/bin/cwl/tools/R/deseq2-2conditions.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
    Copying file /home/veraalva/Work/Developer/Python/pm4ngs/pm4ngs-rnaseq/example/pm4ngs_rnaseq_demo_sample_data.csv  to /Users/veraalva/my_ngs_project/data/my_dataset_name/sample_table.csv
    20 files loaded
    Using table:
       sample_name file       condition  replicate
    0   SRR2126784             PRE_NACT          1
    1   SRR2126785             PRE_NACT          1
    2   SRR2126786             PRE_NACT          1
    3   SRR2126787             PRE_NACT          1
    4   SRR3383790             PRE_NACT          1
    5   SRR3383791             PRE_NACT          1
    6   SRR3383792             PRE_NACT          1
    7   SRR3383794             PRE_NACT          1
    8   SRR3383796             PRE_NACT          1
    9   SRR3383797             PRE_NACT          1
    10  SRR3383798             PRE_NACT          1
    11  SRR2126788       POST_NACT_CRS3          1
    12  SRR2126789       POST_NACT_CRS3          1
    13  SRR2126790       POST_NACT_CRS3          1
    14  SRR2126791       POST_NACT_CRS3          1
    15  SRR2126792       POST_NACT_CRS3          1
    16  SRR2126793       POST_NACT_CRS3          1
    17  SRR2126794       POST_NACT_CRS3          1
    18  SRR2126795       POST_NACT_CRS3          1
    19  SRR2126796       POST_NACT_CRS3          1
     Done


The **pm4ngs-rnaseq** command line will create a project structure as:

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
    │       └── sample_table.csv
    ├── doc
    ├── index.html
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments and Quantification.ipynb
    │   ├── 04 - DGA.ipynb
    │   └── 05 - GO enrichment.ipynb
    ├── requirements
    │   └── conda-env-dependencies.yaml
    ├── results
    │   └── my_dataset_name
    ├── src
    └── tmp

    61 directories, 239 files

.. note:: **RNASeq based project variables**

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
        **03 - Alignments and Quantification.ipynb** notebook to download the genome files.
        The genome data will be at **data/{{dataset_name}}/{{genome_name}}/**

        Default: [hg38]
    * **aligner_index_dir**:
        Absolute path to the directory with the genome indexes for STAR.

        If **{{genome_name}}/STAR** is used, PM4NGS will include a cell in the
        **03 - Alignments and Quantification.ipynb** notebook to create the genome indexes for STAR.

        Default: [hg38/STAR]
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
    * **fold_change**:
        A real number used as fold change cutoff value for the DG analysis, e.g. 2.0.

        Default: [2.0]
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
.. include:: /cwl/rnaseq-star-aligner-workflow.rst
.. include:: /cwl/rnaseq-tpmcalculator-qc-workflow.rst
.. include:: /cwl/rnaseq-dga-workflow.rst
.. include:: /cwl/rnaseq-GO-enrichment-workflow.rst

Demo
----

PM4NGS includes a demo project that users can use to test the framework. It is pre-configured to use Docker as execution
environment.

The RNASeq based demo process samples from the BioProject PRJNA290924_.

Use this command to create the project structure in your local computer

.. code-block:: bash

    localhost:~> pm4ngs-rnaseq-demo

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


The results of this analysis is `https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/rnaseq-sra-paired/`_


.. _01 - Pre-processing QC: https://github.com/ncbi/pm4ngs-rnaseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/01%20-%20Pre-processing%20QC.ipynb
.. _download_quality_control.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/sra/download_quality_control.cwl
.. _fastq-dump.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/sra-tools/fastq-dump.cwl
.. _fastqc.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/fastqc/fastqc.cwl

.. _02 - Samples trimming: https://github.com/ncbi/pm4ngs-rnaseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/02%20-%20Samples%20trimming.ipynb
.. _trimmomatic-PE.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/trimmomatic/trimmomatic-PE.cwl
.. _trimmomatic-SE.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/trimmomatic/trimmomatic-SE.cwl

.. _03 - Alignments and Quantification: https://github.com/ncbi/pm4ngs-rnaseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/03%20-%20Alignments%20and%20Quantification.ipynb
.. _rnaseq-alignment-quantification.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/RNA-Seq/rnaseq-alignment-quantification.cwl
.. _igvtools-count.cw: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/igvtools/igvtools-count.cwl
.. _rseqc-bam_stat.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/rseqc/rseqc-bam_stat.cwl
.. _rseqc-infer_experiment.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/rseqc/rseqc-infer_experiment.cw
.. _rseqc-junction_annotation.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/rseqc/rseqc-junction_annotation.cwl
.. _rseqc-junction_saturation.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/rseqc/rseqc-junction_saturation.cwl
.. _rseqc-read_distribution.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/rseqc/rseqc-read_distribution.cwl
.. _rseqc-read_quality.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/rseqc/rseqc-read_quality.cwl
.. _samtools-flagstat.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-flagstat.cwl
.. _samtools-index.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-index.cwl
.. _samtools-sort.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-sort.cwl
.. _samtools-stats.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-stats.cwl
.. _samtools-view.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-view.cwl
.. _star.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/star/star.cwl
.. _tpmcalculator.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/tpmcalculator/tpmcalculator.cwl

.. _04 - DGA: https://github.com/ncbi/pm4ngs-rnaseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/04%20-%20DGA.ipynb
.. _deseq2-2conditions.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/R/deseq2-2conditions.cwl
.. _edgeR-2conditions.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/R/edgeR-2conditions.cwl

.. _05 - GO enrichment: https://github.com/ncbi/pm4ngs-rnaseq/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/05%20-%20GO%20enrichment.ipynb
.. _goenrichment: https://pypi.org/project/goenrichment/

.. _PRJNA290924: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA290924
.. _`https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/rnaseq-sra-paired/`: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/rnaseq-sra-paired/
