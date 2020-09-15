RNA-Seq quantification and QC workflow using TPMCalculator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflow uses `TPMCalculator`_  to quantify the abundance of genes and transcripts from the sorted BAM file.
Additionally, `RSeQC`_ is executed to generate multiple quality control outputs from the sorted BAM file. At the end,
a TDF file is generated using `igvtools`_ from the BAM file for a quick visualization.

.. image:: /_images/rnaseq-quantification-tpmcalculator-qc-workflow.png
    :width: 800px
    :align: center
    :alt: RNA-Seq quantification and QC workflow using TPMCalculator

.. topic:: Inputs

    * **gtf**:
      Genome GTF file. Variable GENOME_GTF in the Jupyter Notebooks.
      Type: File. Required.
    * **genome_name**: Genome name as defined in IGV for TDF conversion.
      Type: string. Required.
    * **q**: Minimum MAPQ value to use reads. We recommend 255.
      Type: int. Required.
    * **r**: Reference Genome in BED format used by RSeQC.
      Variable GENOME_BED in the Jupyter Notebooks.
      Type: File. Required.
    * **sorted_bam**: Sorted BAM file to quantify.
      Type: File. Required.

.. topic:: Outputs

    * **bam_to_tdf_out**: TDF file created with igvtools from the BAM file for quick visualization. Type: File.
    * **gzip_gene_ent_out**: TPMCalculator gene ENT output gzipped. Type: File.
    * **gzip_gene_out_out**: TPMCalculator gene OUT output gzipped. Type: File.
    * **gzip_gene_uni_out**: TPMCalculator gene UNI output gzipped. Type: File.
    * **gzip_transcripts_ent_out**: TPMCalculator transcript ENT output gzipped. Type: File.
    * **gzip_transcripts_out_out**: TPMCalculator transcript OUT output gzipped. Type: File.
    * **bam_stat_out**: RSeQC BAM stats output. Type: File.
    * **experiment_out**: RSeQC experiment output. Type: File.
    * **gzip_junction_annotation_bed_out**: RSeQC junction annotation bed. Type: File.
    * **gzip_junction_annotation_xls_out**: RSeQC junction annotation xls. Type: File.
    * **junction_annotation_pdf_out**: RSeQC junction annotation PDF figure. Type: File.
    * **junction_saturation_out**: RSeQC junction saturation output. Type: File.
    * **read_distribution_out**: RSeQC read distribution output. Type: File.
    * **read_quality_out**: RSeQC read quality output. Type: File.

.. _TPMCalculator: https://github.com/ncbi/TPMCalculator
.. _RSeQC: http://rseqc.sourceforge.net/
.. _igvtools: https://software.broadinstitute.org/software/igv/igvtools
