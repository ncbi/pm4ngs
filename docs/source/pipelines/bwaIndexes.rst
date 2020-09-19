.. _bwaIndexes:

###################
BWA Genomic Indexes
###################

The **genome.fa** file should be copied to the genome directory.

.. code-block:: bash

    localhost:~> mkdir genome
    localhost:~> cd genome
    localhost:~> mkdir BWA
    localhost:~> cd BWA
    localhost:~> cwl-runner --no-container https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/tools/BWA/bwa-index.cwl --sequences ../genome.fa
    localhost:~> cd ..
    localhost:~> tree
    .
    ├── BWA
    │   ├── genome.fa
    │   ├── genome.fa.amb
    │   ├── genome.fa.ann
    │   ├── genome.fa.bwt
    │   ├── genome.fa.pac
    │   └── genome.fa.sa
    └── genome.fa

    1 directory, 7 files
