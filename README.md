PM4NGS: Program manager for NGS data analysis
=============================================

![Python package](https://github.com/ncbi/pm4ngs/workflows/Python%20package/badge.svg)
![Python application](https://github.com/ncbi/pm4ngs/workflows/Python%20application/badge.svg)
![Upload Python Package](https://github.com/ncbi/pm4ngs/workflows/Upload%20Python%20Package/badge.svg)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/pm4ngs/badges/version.svg)](https://anaconda.org/bioconda/pm4ngs)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/pm4ngs/badges/latest_release_date.svg)](https://anaconda.org/bioconda/pm4ngs)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/pm4ngs/badges/downloads.svg)](https://anaconda.org/bioconda/pm4ngs)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/pm4ngs/badges/installer/conda.svg)](https://conda.anaconda.org/bioconda)

PM4NGS is designed to generate a standard organizational structure for Next Generation Sequencing (NGS) data 
analysis including directory structures for the project, Jupyter notebooks for data management and CWL workflows 
for the pipeline execution.

Our work was inspired for a paper published by Prof. William Noble in 2009:
[A Quick Guide to Organizing Computational Biology Projects](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424). 
We recommend reading this manuscript for a better understanding of the guiding principles of the PM4NGS project.

The project is composed of three parts:

 * the project organizational structure which defines standard files and directories for the project
 * the Jupyter Notebook which is a user interface for the data management and the visualization of results
 * the CWL workflow that executes the data analysis

**PM4NGS** source code includes the templates used by **cookiecutter** to generate the project
organizational structure and the Jupyter notebooks. The CWL workflows are defined in a separate GitHub project named:
[cwl-ngs-workflows-cbb](https://github.com/ncbi/cwl-ngs-workflows-cbb).

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), 
[Jupyter Notebook](https://jupyter.org/), [CWL](https://www.commonwl.org/), [Docker](https://www.docker.com), 
[Conda](https://pm4ngs.readthedocs.io/) and [Bioconda](https://pm4ngs.readthedocs.io/).

Documentation
-------------

Go to https://pm4ngs.readthedocs.io for more detail information.

Reference
---------

 * Vera Alvarez R, Pongor LS, Mariño-Ramírez L and Landsman D. PM4NGS, a project management framework for next-generation sequencing data analysis, GigaScience, Volume 10, Issue 1, January 2021, giaa141, https://doi.org/10.1093/gigascience/giaa141 
 * Vera Alvarez R, Mariño-Ramírez L and Landsman D. Transcriptome annotation in the cloud: complexity, best practices, and cost, GigaScience, Volume 10, Issue 2, February 2021, giaa163, https://doi.org/10.1093/gigascience/giaa163
 * Vera Alvarez R, Pongor LS, Mariño-Ramírez L and Landsman D. [Containerized open-source framework for NGS data analysis and management](https://f1000research.com/posters/8-1229) [version 1; not peer reviewed]. F1000Research 2019, 8(ISCB Comm J):1229 (poster) (doi: 10.7490/f1000research.1117155.1)

Features
---------
* NGS data integration, management and analysis based on Jupyter notebook, CWL workflows and cookiecutter project templates
* Easy installation and use with a minimum command line interaction.
* Data analysis CWL workflows executed from the Jupyter notebook with automatic failing detection and validated with published data
* CWL workflows and Jupyter Notebooks ready for cloud computing
* Project reports and dynamic content creation after data processing using CWL workflows
* Optional use of Docker/Biocontainers or Conda/Bioconda for Bioinformatics tool installation and management

External dependencies
---------------------

 * poppler
    
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
    
