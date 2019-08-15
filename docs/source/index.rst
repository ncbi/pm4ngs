cookiecutter-jupyter-ngs
===================================================================

Cookiecutter based Jupyter Notebook Templates for NGS data analysis.

Powered by Cookiecutter_, `Jupyter Notebook`_, CWL_, Docker_, Conda_ and BioConda_.

Reference
---------

Vera Alvarez R, Pongor LS, Mariño-Ramírez L and Landsman D. `Containerized open-source framework for NGS data analysis
and management`_ [version 1; not peer reviewed]. F1000Research 2019, 8(ISCB Comm J):1229 (poster) (doi: 10.7490/f1000research.1117155.1)

Features
--------

* NGS data integration, management and analysis based on Jupyter notebook, CWL workflows and cookiecutter project templates
* Easy installation and use with a minimum command line interaction.
* Data analysis CWL workflows executed from the Jupyter notebook with automatic failing detection and validated with published data
* CWL workflows and Jupyter Notebooks ready for cloud computing
* Project reports and dynamic content creation after data processing using CWL workflows
* Optional use of Docker/Biocontainers or Conda/Bioconda for Bioinformatics tool installation and management

Extra
-----
.. toctree::
   :maxdepth: 2

   installation
   cookiecutter_json


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Jupyter Notebook: https://jupyter.org/
.. _CWL: https://www.commonwl.org/
.. _Docker: https://www.docker.com
.. _Conda: https://github.com/conda/conda
.. _BioConda: https://bioconda.github.io/
.. _Containerized open-source framework for NGS data analysis and management: https://f1000research.com/posters/8-1229

Available data analysis workflow
--------------------------------

.. toctree::
   :maxdepth: 1

   diff_gene_exp_rnaseq
   det_bind_chipexo

Public Domain notice
====================

National Center for Biotechnology Information.

This software is a "United States Government Work" under the terms of the United States
Copyright Act. It was written as part of the authors' official duties as United States
Government employees and thus cannot be copyrighted. This software is freely available
to the public for use. The National Library of Medicine and the U.S. Government have not
placed any restriction on its use or reproduction.

Although all reasonable efforts have been taken to ensure the accuracy and reliability
of the software and data, the NLM and the U.S. Government do not and cannot warrant the
performance or results that may be obtained by using this software or data. The NLM and
the U.S. Government disclaim all warranties, express or implied, including warranties
of performance, merchantability or fitness for any particular purpose.

Please cite NCBI in any work or product based on this material.
