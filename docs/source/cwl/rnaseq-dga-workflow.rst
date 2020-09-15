Differential Gene Expression analysis from RNA-Seq data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Our notebooks are designed to execute a Differential Gene Expression analysis using two available tools: `DESeq2`_ and
`EdgeR`_. Also, the results for the interception of both tools output is reported with volcano plots, heatmaps and PCA
plots.

The workflow use the **sample_sheet.tsv** file to generate an array with all combinations of **conditions**. The code to
generate this array is very simple and can be found in the cell number 3 in the **05 - DGA.ipynb** notebook.

.. code-block:: python

    comparisons = []
    for s in itertools.combinations(factors['condition'].unique(), 2):
        comparisons.append(list(s))

Let's suppose we have a **factors.txt** file with three conditions: **cond1**, **cond2** and **cond3**. The
**comparisons** array will look like:

.. code-block:: python

    comparisons = [
        ['cond1', 'cond2'],
        ['cond1', 'cond3'],
        ['cond2', 'cond3']
    ]


To avoid this behavior and execute the comparison just in a set of conditions, you should remove the code
in the cell number 3 in the **05 - DGA.ipynb** notebook and manually create the array of combinations to be compared as:

.. code-block:: python

    comparisons = [
        ['cond1', 'cond3'],
    ]


The R code used for running DESeq2 is embedded in `deseq2-2conditions.cwl from line 25 to line 169`_.
The R code used for running EdgeR is embedded in `edgeR-2conditions.cwl from line 25 to line 159`_.

A table with DGA plots is generated for each condition in the **00 - Project Report.ipynb** as shown next.

.. image:: /_images/rnaseq-dga-plots.png
    :width: 800px
    :align: center
    :alt: DGA table for one condition.

.. _DESeq2: https://bioconductor.org/packages/release/bioc/html/DESeq2.html
.. _EdgeR: https://bioconductor.org/packages/release/bioc/html/edgeR.html
.. _deseq2-2conditions.cwl from line 25 to line 169: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/R/deseq2-2conditions.cwl#L14
.. _edgeR-2conditions.cwl from line 25 to line 159: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/R/edgeR-2conditions.cwl#L14
