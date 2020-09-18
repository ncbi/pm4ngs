Peak caller workflow using MACS2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflow uses `MACS2`_ as peak caller tool. The annotation is created using `Homer`_ and TDF files are created
with `igvtools`_.

.. image:: /_images/peak-caller-macs2-workflow.png
    :width: 800px
    :align: center
    :alt: BWA based alignment and quality control workflow

`MACS2`_ is executed two times. First, the **cutoff-analysis** option is used to execute a cutoff value analysis which
is used to estimate a proper value for the p-value used by MACS2 (for more detailed explanation read this `thread`_).

.. image:: /_images/macs2-cutoff-analysis.png
    :width: 500px
    :align: center
    :alt: MACS2 cutoff analysis

`RSeQC`_ is also executed for quality control.

.. topic:: Inputs

    * **homer_genome**: Homer genome name.
      Type: string. Required.
    * **genome_fasta** Genome FASTA file.
      Type: File. Required. Variable GENOME_FASTA in the Jupyter Notebooks.
    * **genome_gtf**: Genome GTF file.
      Type: File. Required. Variable GENOME_GTF in the Jupyter Notebooks.
    * **tagAlign_gz**: Tag aligned file created with the BWA based alignment and quality control workflow.
      Type: File. Required.
    * **macs_callpeaks_g**: Genome mapeable size as defined in MACS2.
      Type: string. Required. Variable GENOME_MAPPABLE_SIZE in the Jupyter Notebooks.
    * **macs_callpeaks_q**: MACS2 **q** option. Starting qvalue (minimum FDR) cutoff to call significant regions.
      Type: float. Required. Variable fdr in the Jupyter Notebooks.
    * **nomodel**: MACS2 nomodel option. MACS will bypass building the shifting model.
      Type: boolean. Optional.
    * **extsize**: MACS2 extsize option. MACS uses this parameter to extend reads in 5'->3' direction to
      fix-sized fragments.
      Type: int. Optional.

.. topic:: Outputs

    * **readQC_plots**: RSeQC plots. Type: File[]
    * **macs_cutoff_pdf** MACS2 cutoff analysis plot in PDF format. Type: File
    * **macs_cutoff_inflection**: MACS2 inflection q value used for the second round. Type: File
    * **macs_callpeak_q_value_narrowPeak**: Final MACS2 narrowpeak file. Type: File
    * **macs_callpeak_q_value_xls**: Final MACS2 XLS file. Type: File
    * **macs_callpeak_q_value_bed**: Final MACS2 BED file. Type: File
    * **homer_annotate_peaks_output**: Homer annotated BED file. Type: File
    * **homer_annotate_peaks_annStats**: Homer annotation statistics. Type: File
    * **lambda_tdf_out**: MACS2 lambda file in TDF format. Type: File
    * **pileup_tdf_out**: MACS2 pileup file in TDF format. Type: File

.. _MACS2: https://github.com/taoliu/MACS
.. _Homer: http://homer.ucsd.edu/homer/
.. _igvtools: https://software.broadinstitute.org/software/igv/igvtools
.. _RSeQC: http://rseqc.sourceforge.net/
.. _thread: https://github.com/taoliu/MACS/issues/151#issuecomment-249908402

