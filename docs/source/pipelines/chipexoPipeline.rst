.. _chipexoPipeline:

Detection of binding events from ChIP-exo data
==============================================

.. table:: DNA motif identification, ChIP-exo data pipeline
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
    | Peak Calling           | `04 - Peak Calling`_                   |  `peak-caller-MACE-SE.cwl`_            | IGVtools        | Sorted BAM    | TDF                 | `igvtools-count.cw`_             |
    |                        |                                        |                                        +-----------------+---------------+---------------------+----------------------------------+
    | and IDR                |                                        |                                        | MACE            | tagAlign      | Peaks (TSV), plots  | `mace.cwl`_                      |
    |                        |                                        |                                        +-----------------+---------------+---------------------+----------------------------------+
    |                        |                                        |                                        | BAMScale        | BAM           | TPM values          | `bamscale-cov.cwl`_              |
    |                        |                                        |                                        |                 |               |                     |                                  |
    |                        |                                        |                                        |                 |               |                     | `bamscale-scale.cwl`_            |
    +------------------------+----------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+
    | DNA motif              | `05 - MEME Motif`_                     |                                        | MEME Suite      | Peaks         | DNA Motif , plots   | `meme-chip.cwl`_                 |
    | identification         |                                        |                                        |                 |               |                     |                                  |
    +------------------------+----------------------------------------+----------------------------------------+-----------------+---------------+---------------------+----------------------------------+

.. _01 - Pre-processing QC: https://github.com/ncbi/pm4ngs-chipexo/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/01%20-%20Pre-processing%20QC.ipynb
.. _download_quality_control.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/sra/download_quality_control.cwl
.. _fastq-dump.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/sra-tools/fastq-dump.cwl
.. _fastqc.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/fastqc/fastqc.cwl

.. _02 - Samples trimming: https://github.com/ncbi/pm4ngs-chipexo/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/02%20-%20Samples%20trimming.ipynb
.. _trimmomatic-PE.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/trimmomatic/trimmomatic-PE.cwl
.. _trimmomatic-SE.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/trimmomatic/trimmomatic-SE.cwl

.. _03 - Alignments: https://github.com/ncbi/pm4ngs-chipexo/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/03%20-%20Alignments.ipynb
.. _chip-seq-alignment.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/ChIP-Seq/chip-seq-alignment.cwl
.. _bwa-mem.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/bwa/bwa-mem.cwl
.. _samtools-flagstat.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-flagstat.cwl
.. _samtools-index.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-index.cwl
.. _samtools-sort.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-sort.cwl
.. _samtools-stats.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-stats.cwl
.. _samtools-view.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/tree/master/tools/samtools/samtools-view.cwl
.. _igvtools-count.cw: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/igvtools/igvtools-count.cwl

.. _04 - Peak Calling: https://github.com/ncbi/pm4ngs-chipexo/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/04%20-%20Peak%20Calling.ipynb
.. _peak-caller-MACE-SE.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/ChIP-exo/peak-caller-MACE-SE.cwl
.. _mace.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/mace/mace.cwl
.. _bamscale-cov.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/bamscale/bamscale-cov.cwl
.. _bamscale-scale.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/bamscale/bamscale-scale.cwl

.. _05 - MEME Motif: https://github.com/ncbi/pm4ngs-chipexo/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/notebooks/05%20-%20MEME%20Motif.ipynb
.. _meme-chip.cwl: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/meme/meme-chip.cwl
