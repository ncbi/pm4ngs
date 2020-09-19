.. _createBEDFromGTF:

###################
Create BED from GTF
###################

For generating a BED file from a GTF.

The **genes.gtf** file should be copied to the genome directory.

.. code-block:: bash

    localhost:~> mkdir genome
    localhost:~> cd genome
    localhost:~> cwl-runner --no-container https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/workflows/UCSC/gtftobed.cwl --gtf genes.gtf
    localhost:~> tree
    .
    ├── genes.bed
    ├── genes.genePred
    └── genome.gtf

    0 directory, 3 files

Here the files **genes.bed** and **genes.genePred** are created from the workflow.