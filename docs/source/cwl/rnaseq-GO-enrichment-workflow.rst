GO enrichment from RNA-Seq data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The GO enrichment analysis is executed with an *in-house* developed python package named `goenrichment`_. This tools
uses the `hypergeometric distribution`_ test to estimate the probability of successes in selecting GO terms from a
list of differentially expressed genes. The GO terms are represented as a network using the python library `NetworkX`_.

The tool uses a pre-computed database, currently available for `human`_ and `mouse`_, at
https://ftp.ncbi.nlm.nih.gov/pub/goenrichment/. However, the project web page describe how to create your own database
from a set of reference databases.

The workflow uses the **factors.txt** file to generate an array with all combinations of **conditions**. The code to
generate this array is very simple and can be found in the cell number 3 in the **06 - GO enrichment.ipynb** notebook.

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
in the cell number 3 in the **06 - GO enrichment.ipynb** notebook and manually create the array of combinations to be compared as:

.. code-block:: python

    comparisons = [
        ['cond1', 'cond3'],
    ]


Additionally, the workflow requires three cutoff that are defined in the cell number 5 of the same notebook.

.. code-block:: python

    min_category_depth=4
    min_category_size=3
    max_category_size=500

.. topic:: Cutoffs definition

    * min_category_depth: Min GO term graph depth to include in the report. Default: 4
    * min_category_size: Min number of gene in a GO term to include in the report. Default: 3
    * max_category_size: Max number of gene in a GO term to include in the report. Default: 500

A table with GO terms plots is generated for each condition in the **00 - Project Report.ipynb** as shown next. In
these plots the red bars are for GO terms selected from the over expressed genes and the blue bars are for
GO terms selected from the under expressed genes. It is important to clarify that the two sets of GO terms don't
overlap each other.

.. image:: /_images/rnaseq-go-plots.png
    :width: 800px
    :align: center
    :alt: GO enrichment table for one condition.

.. _goenrichment: https://pypi.org/project/goenrichment/
.. _NetworkX: https://networkx.github.io/
.. _hypergeometric distribution: https://en.wikipedia.org/wiki/Hypergeometric_distribution
.. _human: https://ftp.ncbi.nlm.nih.gov/pub/goenrichment/goenrichDB_human.pickle
.. _mouse: https://ftp.ncbi.nlm.nih.gov/pub/goenrichment/goenrichDB_mouse.pickle