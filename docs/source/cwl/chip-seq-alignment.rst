BWA based alignment and quality control workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflow use `BWA`_ as base aligner. It also use `SAMtools`_ and `bedtools`_ for file conversion and statistics
report. Finally, `Phantompeakqualtools`_ is used to generate quality control report for the processed samples.

.. image:: /_images/chip-seq-alignment-workflow.png
    :width: 800px
    :align: center
    :alt: BWA based alignment and quality control workflow

.. topic:: Inputs

    * **genome_index**: Aligner indexes directory.
      Type: Directory. Required. Variable ALIGNER_INDEX in the Jupyter Notebooks.
    * **genome_prefix**: Prefix of the aligner indexes. Generally, it is the name of the genome FASTA file.
      It can be used as os.path.basename(GENOME_FASTA) in the Jupyter Notebooks.
      Type: string. Required.
    * **readsquality**:
      Minimum MAPQ value to use reads. We recommend for ChIP_exo dataa value of: 30.
      Type: int. Required.
    * **threads**: Number of threads.
      Type: int. Default: 1. Optional.
    * **subsample_nreads**: Number of reads to be used for the subsample.
      We recomend for ChIP_exo dataa value of: 500000.
      Type: int. Required.
    * **reads**: FastQ file to be processed.
      Type: File. Required.

.. topic:: Outputs

    * **bam_flagstat_out**: SAMtools flagstats for unfiltered BAM file. Type: File.
    * **bam_stats_out**: SAMtools stats for unfiltered BAM file. Type: File.
    * **final_bam_flagstat_out**: SAMtools flagstats for filtered BAM file. Type: File.
    * **bed_file_out**:: Aligned reads in BED format. Type: File.
    * **final_bam_out**: Final BAM file filtered and sorted. Type: File.
    * **bam_index_out**: BAM index file. Type: File.
    * **pbc_out**: Library complexity report. Type: File.
    * **phantompeakqualtools_output_out**: Phantompeakqualtools main output. Type: File.
    * **phantompeakqualtools_output_savp**: Phantompeakqualtools SAVP output. Type: File.
    * **subsample_pseudoreplicate_gzip_out**: Subsample pseudoreplicates tagAlign gzipped. Type: File[].
    * **subsample_tagalign_out**: Subsample tagAlign gzipped. Type: File[].
    * **subsample_subsample_out**: Subsample shuffled tagAlign gzipped. Type: File[].

.. _BWA: http://bio-bwa.sourceforge.net/
.. _SAMtools: http://www.htslib.org/
.. _bedtools: https://bedtools.readthedocs.io/en/latest/
.. _Phantompeakqualtools: https://github.com/kundajelab/phantompeakqualtools
