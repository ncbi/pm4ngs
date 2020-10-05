.. _sampleSheet:

############
Sample sheet
############

A CSV file describing samples, conditions and replicate number is required during the PM4NGS project creation.

PM4NGS will copy the sample sheet file to the folder **data/{{dataset_name}}** with the standard name
**sample_table.csv**.

******************
Single-end example
******************

This is an sample sheet example for **single-end** sequencing technology data:

.. csv-table::
    :file: ../_static/examples/sample_sheet_single_end.csv
    :widths: 10, 50, 30, 10
    :header-rows: 1

Table source: sample_sheet_single_end.csv_

.. _sample_sheet_single_end.csv: ../_static/examples/sample_sheet_single_end.csv

******************
Paired-end example
******************

For **paired-end** sequencing technology data, the **|** should be used to separate forward and reverse fastq files:

.. csv-table::
    :file: ../_static/examples/sample_sheet_paired_end.csv
    :widths: 10, 70, 12, 8
    :header-rows: 1

Source: sample_sheet_paired_end.csv_

.. _sample_sheet_paired_end.csv: ../_static/examples/sample_sheet_paired_end.csv

PM4NGS will copy or download the raw fastq files to the **data/{{dataset_name}}/** directory during the project creation
if the [--copy-rawdata] is used.

*********************************
Processing data from the NCBI SRA
*********************************

For data in the NCBI SRA database, the *file* column should be empty. PM4NGS will download the files during the
pre-processing quality control step.

.. csv-table::
    :file: ../_static/examples/sample_sheet_sra.csv
    :header-rows: 1

Source: sample_sheet_sra.csv_

.. _sample_sheet_sra.csv: ../_static/examples/sample_sheet_sra.csv

*****************************************
Sample sheet column names and description
*****************************************

.. note::  Columns names are required and are case sensitive.

.. topic:: Columns

    * **sample_name**: Sample names. It can be different of sample file name.
    * **file**: This is the absolute path or URL to the raw fastq file.

      For paired-end data the files should be separated using the unix pipe **|** as
      **SRR4053795_1.fastq.gz|SRR4053795_2.fastq.gz** must exist.

      The data files will be copied to the folder **data/{{dataset_name}}/**.
    * **condition**: Conditions to group the samples. Use only alphanumeric characters.

      For RNASeq projects the differential gene expression will be generated comparing these conditions. If there are
      multiple conditions all comparisons will be generated. It must be at least two conditions.

      For ChIPSeq projects differential binding events will be detected comparing these conditions. If there are
      multiple conditions all comparisons will be generated. It must be at least two conditions.

      For ChIPexo projects the samples of the same condition will be grouped for the peak calling with MACE.
    * **replicate**: Replicate number for samples.
