Peak caller workflow using MACE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflow uses `MACE`_ as peak caller tool. The annotation is created from the GTF file using a *in-house* python
script available `here`_. `BAMscale`_ is used for the quantification of the resulting peaks.

.. image:: /_images/peak-caller-mace-workflow.png
    :width: 800px
    :align: center
    :alt: BWA based alignment and quality control workflow

.. topic:: Inputs

    * **chrom_size**: Chromosome size file. Tab or space separated text file with 2 columns: first column is
      chromosome name, second column is size of the chromosome.
      Type: File. Required. Variable GENOME_CHROMSIZES in the Jupyter Notebooks.
    * **output_basename**: Prefix for the output file.
      Type: string. Required.
    * **genome_gtf**:
      Genome GTF file. Variable GENOME_GTF in the Jupyter Notebooks.
      Type: File. Required.
    * **tss_size**: Number of bp to use for TSS definition. We recommend use 1000.
      Type: int. Required.

.. topic:: Outputs

    * **annotated_bed**: Annotated detected peaks in BED format. Type: File

.. _MACE: http://chipexo.sourceforge.net/
.. _here: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/python/annotate_bed_gtf.cwl
.. _BAMscale: https://github.com/ncbi/BAMscale
