.. _starIndexes:

####################
STAR Genomic Indexes
####################

The **genome.fa** and **genes.gtf** files should be copied to the genome directory.

.. code-block:: bash

    localhost:~> mkdir genome
    localhost:~> cd genome
    localhost:~> mkdir STAR
    localhost:~> cd STAR
    localhost:~> cwl-runner https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/star/star-index.cwl --runThreadN 16 --genomeDir . --genomeFastaFiles ../genome.fa  --sjdbGTFfile ../genes.gtf
    localhost:~> cd ..
    localhost:~> tree
    .
    ├── genes.gtf
    ├── genome.fa
    └── STAR
        ├── chrLength.txt
        ├── chrNameLength.txt
        ├── chrName.txt
        ├── chrStart.txt
        ├── exonGeTrInfo.tab
        ├── exonInfo.tab
        ├── geneInfo.tab
        ├── Genome
        ├── genomeParameters.txt
        ├── Log.out
        ├── SA
        ├── SAindex
        ├── sjdbInfo.txt
        ├── sjdbList.fromGTF.out.tab
        ├── sjdbList.out.tab
        └── transcriptInfo.tab

    1 directory, 18 files

Here all files inside the directory **STAR** are created by the workflow.
