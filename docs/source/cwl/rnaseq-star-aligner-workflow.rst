STAR based alignment and sorting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflows use `STAR`_ for alignning RNA-Seq reads to a genome. The obtained BAM file is sorted using `SAMtools`_.
Statistics outputs from STAR and SAMtools are returned as well.

.. image:: /_images/rnaseq-star-aligner-workflow.png
    :width: 800px
    :align: center
    :alt: STAR based alignment and sorting

.. topic:: Inputs

    * **genomeDir**: Aligner indexes directory.
      Type: Directory. Required. Variable ALIGNER_INDEX in the Jupyter Notebooks.
    * **threads**: Number of threads.
      Type: int. Default: 1. Optional.
    * **reads_1**: FastQ file to be processed for paired-end reads _1.
      Type: File. Required.
    * **reads_2**: FastQ file to be processed for paired-end reads _2.
      Type: File. Required.

.. topic:: Outputs

    * **sorted_bam**: Final BAM file filtered and sorted. Type: File.
    * **indexed_bam**: BAM index file. Type: File.
    * **star_stats**: STAR alignment statistics. Type: File.
    * **readspergene**: STAR reads per gene output. Type: File.
    * **stats_bam**: SAMtools stats output: Type: File.

.. _STAR: https://github.com/alexdobin/STAR
.. _SAMtools: http://www.htslib.org/
