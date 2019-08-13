Cookiecutter based Jupyter Notebook Templates for NGS data analysis
===================================================================

Powered by Cookiecutter_, `Jupyter Notebook`_, CWL_, Docker_, Conda_.

Reference
---------

Vera Alvarez R, Pongor LS, Mariño-Ramírez L and Landsman D. `Containerized open-source framework for NGS data analysis
and management`_ [version 1; not peer reviewed]. F1000Research 2019, 8(ISCB Comm J):1229 (poster) (doi: 10.7490/f1000research.1117155.1)

Features
---------
* NGS data integration, management and analysis based on Jupyter notebook, CWL workflows and cookiecutter project templates
* Easy installation and use with a minimum command line interaction.
* Data analysis CWL workflows executed from the Jupyter notebook with automatic failing detection and validated with published data
* CWL workflows and Jupyter Notebooks ready for cloud computing
* Project reports and dynamic content creation after data processing using CWL workflows
* Optional use of Docker/Biocontainers or Conda/Bioconda for Bioinformatics tool installation and management


Available data analysis workflows
---------------------------------

* `Differential Gene expression from RNA-Seq data`_

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   configuration


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Jupyter Notebook: https://jupyter.org/
.. _CWL: https://www.commonwl.org/
.. _Docker: https://www.docker.com
.. _Conda: https://github.com/conda/conda
.. _Containerized open-source framework for NGS data analysis and management: https://f1000research.com/posters/8-1229
.. _Differential Gene expression from RNA-Seq data: diff_gene_exp_rnaseq
