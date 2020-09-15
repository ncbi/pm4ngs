Differential binding analysis with Diffbind
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Differential binding event is detected with `Diffbind`_. Thsi `tool`_ will be executed for all comparisons added to the
**comparisons** array. See cell number 3 in the notebook **05 - Differential binding analysis.ipynb**
(ChIP-Seq workflow).

.. topic:: Inputs

    * **bamDir**: Directory with the BAM files.
      Type: Directory. Required.
    * **bedDir**: Directory with BED files created from MACS2 peak calling workflow
      Type: Directory. Required.


.. topic:: Outputs

    * **outpng**: PNG files created from Diffbind. Type File[]
    * **outxls**: XLS files created from Diffbind. Type: File[]
    * **outbed** BED files created from Diffbind. Type: File[]

.. _Diffbind: https://bioconductor.org/packages/release/bioc/html/DiffBind.html
.. _tool: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/R/DiffBind.cwl
