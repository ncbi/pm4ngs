MEME Motif detection workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Motif detection is executed using the `MEME`_ suite.

.. image:: /_images/MEME-motif-workflow.png
    :width: 800px
    :align: center
    :alt: MEME Motif detection workflow

.. topic:: Inputs

    * **bed**: BED file with detected peaks.
      Type: File. Required.
    * **memedb**: MEME database for use by Tomtom and CentriMo.
      Type: File. Required.
    * **genome**:
      Genome FASTA file. Variable GENOME_FASTA in the Jupyter Notebooks.
      Type: File. Required.
    * **nmotifs**: Maximum number of motifs to find. We recommend use 10.
      Type: int. Required.

.. topic:: Outputs

    * **meme_out**: MEME output directory. Type: Directory

.. _MEME: http://meme-suite.org/

MEME databases
^^^^^^^^^^^^^^

MEME workflow depends on the MEME databases. Go to the MEME Suite Download page: http://meme-suite.org/doc/download.html

Download the latest version for the Motif Databases and GOMo Databases.

The downloaded files should be uncompressed in a directory **data/meme**. The final directory should be:

.. code-block:: bash

    localhost:~> cd data
    localhost:~> mkdir meme
    localhost:~> cd meme
    localhost:~> wget http://meme-suite.org/meme-software/Databases/motifs/motif_databases.12.18.tgz
    localhost:~> wget http://meme-suite.org/meme-software/Databases/gomo/gomo_databases.3.2.tgz
    localhost:~> tar xzf motif_databases.12.18.tgz
    localhost:~> tar xzf gomo_databases.3.2.tgz
    localhost:~> rm gomo_databases.3.2.tgz motif_databases.12.18.tgz
    localhost:~> tree -d
    .
    ├── gomo_databases
    └── motif_databases
        ├── ARABD
        ├── CIS-BP
        ├── CISBP-RNA
        ├── ECOLI
        ├── EUKARYOTE
        ├── FLY
        ├── HUMAN
        ├── JASPAR
        ├── MALARIA
        ├── MIRBASE
        ├── MOUSE
        ├── PROKARYOTE
        ├── PROTEIN
        ├── RNA
        ├── TFBSshape
        ├── WORM
        └── YEAST

    19 directories

See also an example in our test project: https://ftp.ncbi.nlm.nih.gov/pub/pm4ngs/examples/chipexo-single/data/

