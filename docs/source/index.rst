PM4NGS
===================================================================

`PM4NGS`_ was designed to generate a standard organizational structure for Next Generation Sequencing
(ngs) data analysis. It includes a directory structure for the project, several Jupyter notebooks for data management
and  CWL workflows for pipeline execution.

Our work was inspired by a manuscript by Prof. William Noble in 2009:
`A Quick Guide to Organizing Computational Biology Projects`_. We recommend reading this paper for a better
understanding of the guiding principles of our project.

The project is composed of three main parts.

#. a project organizational structure which define a standard files and directories for the project
#. Jupyter Notebooks as user interfaces for data management and visualization
#. CWL workflows that execute the data analysis

**PM4NGS** source code includes the templates used by **cookiecutter** to generate the project
organizational structure and the Jupyter notebooks. The CWL workflows are defined in a separate GitHub project named:
`cwl-ngs-workflows-cbb`_.

All projects generated from these templates follow the same design principles explained in the
:doc:`Background Information </background_information>`.

.. _PM4NGS: https://github.com/ncbi/pm4ngs
.. _A Quick Guide to Organizing Computational Biology Projects: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424
.. _GNU Parallel: https://www.gnu.org/software/parallel/
.. _cwl-ngs-workflows-cbb: https://github.com/ncbi/cwl-ngs-workflows-cbb

Features
--------

* NGS data integration, management and analysis uses Jupyter notebooks, CWL workflows and cookiecutter project templates
* Easy installation and use with a minimum command line interaction
* Data analysis CWL workflows executed from the Jupyter notebook with automatic failing detection and can be validated with published data
* CWL workflows and Jupyter Notebooks are ready for cloud computing
* Project reports and dynamic content creation after data processing using CWL workflows are included
* Optional use of Docker/Biocontainers or Conda/Bioconda for Bioinformatics tool installations and managements are also included

Links to available data analysis workflows
------------------------------------------

.. toctree::
   :maxdepth: 2

   /workflows/diff_gene_exp_rnaseq
   /workflows/diff_bind_event_chipseq
   /workflows/det_bind_chipexo

Extra links
-----------

.. toctree::
   :maxdepth: 1

   /envs/installation
   /extra/cookiecutter_json

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Jupyter Notebook: https://jupyter.org/
.. _CWL: https://www.commonwl.org/
.. _Docker: https://www.docker.com
.. _Conda: https://github.com/conda/conda
.. _BioConda: https://bioconda.github.io/
.. _Containerized open-source framework for NGS data analysis and management: https://f1000research.com/posters/8-1229

Reference
---------

#. Vera Alvarez R, Pongor LS, Mariño-Ramírez L and Landsman D. `Containerized open-source framework for NGS data analysis and management`_ [version 1; not peer reviewed]. F1000Research 2019, 8(ISCB Comm J):1229 (poster) (doi: 10.7490/f1000research.1117155.1)

Public Domain Notice
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
