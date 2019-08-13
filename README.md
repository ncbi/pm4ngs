Cookiecutter based Jupyter Notebook Templates for NGS data analysis
============================================================

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), 
[Jupyter Notebook](https://jupyter.org/), [CWL](https://www.commonwl.org/), [Docker](https://www.docker.com), 
[Conda]().

Reference
---------

Vera Alvarez R, Pongor LS, Mariño-Ramírez L and Landsman D. [Containerized open-source framework for NGS data analysis and management](https://f1000research.com/posters/8-1229) [version 1; not peer reviewed]. F1000Research 2019, 8(ISCB Comm J):1229 (poster) (doi: 10.7490/f1000research.1117155.1)

Features
---------
* NGS data integration, management and analysis based on Jupyter notebook, CWL workflows and cookiecutter project templates
* Easy installation and use with a minimum command line interaction.
* Data analysis CWL workflows executed from the Jupyter notebook with automatic failing detection and validated with published data
* CWL workflows and Jupyter Notebooks ready for cloud computing
* Project reports and dynamic content creation after data processing using CWL workflows
* Optional use of Docker/Biocontainers or Conda/Bioconda for Bioinformatics tool installation and management

Pipelines
---------

* Differential Gene expression from RNA-Seq data
* Differential Binding events from ChIP-Seq data
* Identification and annotation of binding motif from ChIP-exo data

Pipelines under development
---------------------------

* Chromatin state discovery with ChromHMM from ChIP-Seq data
* Differential Binding events from ATAC-Seq data
* Differential Gene expression from RNA-Seq data using as input NCBI SRA IDs

Constraints
-----------
* Designed for running  in a single server.

Installation
------------

### Conda and Bioconda

### Python virtual environment 

First, install Cookiecutter and other basic Python packages. 

    $ pip install -r https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/requirements.txt


Usage
-----
    
Go inside the project folders and activate virtual environment:

    source venv/bin/activate
    
Start the jupyter notebook server

    jupyter notebook
    
Start executing the Jupyter notebook from the number `01-` in a sequential way. Once everything is done run the
`00 - Project Report` for the creation of the final report page with tables and figures.
    
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
    
