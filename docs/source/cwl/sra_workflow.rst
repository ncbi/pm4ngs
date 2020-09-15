SRA download and QC workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This CWL workflow is designed to download FASTQ files from the NCBI SRA database using `fastq-dump`_ and then, execute
`fastqc`_ generating a quality control report of the sample.

.. image:: /_images/sra-workflow.png
    :width: 800px
    :align: center
    :alt: SRA workflow

.. topic:: Inputs

    * **accession**: SRA accession ID.
      Type: string. Required.
    * **aligned**: Used it to download only aligned reads.
      Type: boolean. Optional.
    * **split-files**: Dump each read into separate file.
      Files will receive suffix corresponding to read number.
      Type: boolean. Optional.
    * **threads**: Number of threads.
      Type: int. Default: 1. Optional.
    * **X**: Maximum spot id. Optional.

.. topic:: Outputs

    * **output**: Fastq files downloaded. Type: File[]
    * **out_zip**: FastQC report ZIP file. Type: File[]
    * **out_html**: FastQC report HTML. Type: File[]

.. _fastq-dump: https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc&f=fastq-dump
.. _fastqc: https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
