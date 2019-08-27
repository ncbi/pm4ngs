MEME Motif detection workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Motif detection is executed using the `MEME`_ suite.

.. image:: /img/MEME-motif-workflow.png
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
