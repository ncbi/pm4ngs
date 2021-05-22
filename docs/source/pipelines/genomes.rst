.. _genomes:

########################
PM4NGS available genomes
########################

A set of genomes are available for download with the required files already configured. If the genome name is used, PM4NGS
will include in the alignment notebook a cell to download, uncompress the genome file and create the aligner indexes.

.. note::

    We recommend to move our of the first project the generated genome folder **data/{{genome_name}}/**
    to a different folder so it can be reutilized for other projects. This will avoid the extra time for the index
    creation and will save space.

.. table:: Available genomes
    :widths: 15 15 15 13 10 12 20

    +----------------+-------------------------------------+--------+
    | Name           | Organism                            | Source |
    +================+=====================================+========+
    | `hg38`_        | Homo sapiens                        | UCSC   |
    +----------------+-------------------------------------+--------+
    | `hg19`_        | Homo sapiens                        | UCSC   |
    +----------------+-------------------------------------+--------+
    | `mm10`_        | Mus musculus (Mouse)                | UCSC   |
    +----------------+-------------------------------------+--------+
    | `mm9`_         | Mus musculus (Mouse)                | UCSC   |
    +----------------+-------------------------------------+--------+
    | `NC_000913.3`_ | Escherichia coli strain K12, MG1655 | NCBI   |
    +----------------+-------------------------------------+--------+
    | `canFam3`_     | Canis familiaris (Dog)              | UCSC   |
    +----------------+-------------------------------------+--------+
    | `dm6`_         | Drosophila melanogaster             | UCSC   |
    +----------------+-------------------------------------+--------+
    | `TAIR10`_      | Arabidopsis thaliana                | NCBI   |
    +----------------+-------------------------------------+--------+


.. _hg38: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/resources/hg38.tar.gz
.. _hg19: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/resources/hg19.tar.gz
.. _mm10: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/resources/mm10.tar.gz
.. _mm9: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/resources/mm9.tar.gz
.. _NC_000913.3: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/resources/NC_000913.3.tar.gz
.. _canFam3: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/resources/canFam3.tar.gz
.. _dm6: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/resources/dm6.tar.gz
.. _TAIR10: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/resources/TAIR10.tar.gz
