# Jupyter {{ cookiecutter.ngs_data_type }} data analysis pipeline

## Basic requirements

1. Python 3.7.x
2. virtualenv 16.5.0
3. ImageMagick 7.0.x

Full list of requirements *requirements/python.txt*

## Installation

```bash
cd {{ cookiecutter.project_name }}
virtualenv -p `which python3` venv
source venv/bin/activate
pip install -r requirements/python.txt
```

## Starting Jupyter Notebook

```bash
jupyter notebook
```

{% if cookiecutter.is_data_in_SRA == 'y' %}
## Using data from SRA

{% else %}
## Using your own data

{% endif %}
### Start using the notebooks

Use notebook by number in the folder `notebooks`

# Public Domain notice

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
