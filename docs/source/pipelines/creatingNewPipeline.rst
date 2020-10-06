.. _creatingNewPipeline:

############################
Create a new PM4NGS pipeline
############################

The recommended way to create a new pipeline is modifying one of the current available pipelines.
Before reading this instructions, the user should understand the basics concepts of the Cookiecutter_.

PM4NGS based pipeline folder structure
--------------------------------------

The PM4NGS based pipeline folder structure is:

.. code-block:: bash

    .
    |── LICENSE
    ├── README.md
    ├── cookiecutter.json
    ├── example
    │   ├── pm4ngs_chipseq_demo_config.yaml
    │   └── pm4ngs_chipseq_demo_sample_data.csv
    ├── hooks
    │   ├── post_gen_project.py
    │   └── pre_gen_project.py
    └── {{cookiecutter.project_name}}
        ├── LICENSE
        ├── README.md
        ├── bin
        ├── config
        │   └── init.py
        ├── data
        │   └── {{cookiecutter.dataset_name}}
        ├── doc
        ├── index.html
        ├── notebooks
        │   ├── 00 - Project Report.ipynb
        │   ├── 01 - Pre-processing QC.ipynb
        │   ├── 02 - Samples trimming.ipynb
        │   ├── 03 - Alignments.ipynb
        │   ├── 04 - Peak Calling and IDR.ipynb
        │   └── 05 - Differential binding Detection.ipynb
        ├── requirements
        │   └── conda-env-dependencies.yaml
        ├── results
        │   └── {{cookiecutter.dataset_name}}
        ├── src
        └── tmp

    14 directories, 18 files

Folders:

    * **cookiecutter.json**: the default cookiecutter JSON file where all input variables are defined
    * **example**: this folder should include the sample sheet and yaml config file for the pipeline demo
    * **hooks**: Cookiecutter pre and post execution scripts. PM4NGS uses these pre and post scripts to execute tasks
      required to configure the pipeline like cloning the CWL repo, copying the raw data and the sample sheet.

      In the **post_gen_project.py** is where the CWL repository is defined. Users should modify this variable with the
      localization of their own CWL workflows.

          CWL_WORKFLOW_REPO = 'https://github.com/ncbi/cwl-ngs-workflows-cbb'

      This repo will be clone to a folder named **cwl** in the project **bin** directory.
    * **{{cookiecutter.project_name}}**: this is a folder with the cookiecutter variable for project name.

      This folder store all pipeline's files.
    * **config/init.py**: This is the configuration file for the workflow that should be loaded at the beginning of
      all notebooks.
      Any function for creating tables, figures and plots not included in PM4NGS should be included in the **init.py** file.
      Users can also do PR on the PM4NGS repo to the package: pm4ngs.jupyterngsplugin to include their functions in
      the PM4NGS package but this is not required.


    * **notebooks**: In this folder all jupyter notebook are stored.

      The specific requirement for the notebooks are:

         1. Run the **init.py** at the first cell of the notebook

            .. code-block:: python

                %run ../config/init.py

         2. Use relative paths all the time.
         3. Global variables should be defined in the **init.py** file.
         4. HTML code can be used to display information on the notebook:

            To show a link to the sample sheet this can be used on the notebook cell:

            .. code-block:: python

                filename = os.path.relpath(os.path.join(DATA, DATASET, 'sample_sheet.tsv'))
                html_link = '<a href="{}" target="_blank">sample_sheet.tsv</a>'.format(filename.replace(' ', '%20'))
                display(Markdown(html))

         5. PM4NGS include functions to create links from an image or PDF file:
            Note that this functions require Poppler (https://poppler.freedesktop.org/) installed.

            .. code-block:: python

                from pm4ngs.jupyterngsplugin.markdown.utils import get_link_image

                width = 450
                height = 450
                filename = os.path.relpath(os.path.join(RESULTS, DATASET, 'dga', 'condition_POST_NACT_CRS2_vs_PRE_NACT_NORMAL_deseq2_pca.pdf'))
                html_link = get_link_image(filename, width, height, ' --- ')
                display(Markdown(html))

    * **requirements/conda-env-dependencies.yaml**: Define the conda packages and versions tu run the pipeline.

.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/latest/first_steps.html

CWL tools and workflows specifications
--------------------------------------

The workflow repository should include two main directories: **tools** and **workflows**.
The first directory, **tools**, includes all computational tools used by the workflows in CWL format.
The second folder, **workflows**, includes all workflows.

Each CWL tool should include two YAML files with suffixes **bioconda.yml**  and **docker.yml**  that are imported in the **hints**
block.

.. code-block:: bash

   hints:
      - $import: bwa-docker.yml
      - $import: bwa-bioconda.yml

See example `bwa-mem.cwl`_

As it is indicated by its names, the **bioconda.yml** files stores the software requirements for executing the
CWL tool using Conda. The files specify the package name and version. The CWL runner will create a Conda environment
and install the package, if it doesnt exists, at runtime.

.. code-block:: bash

   class: SoftwareRequirement
   packages:
      - package: 'bwa'
        version:
          - '0.7.17'
        specs:
          - https://anaconda.org/bioconda/bwa

See example `bwa-bioconda.yml`_

The docker.yml file defines the Biocontainers docker image to be used. This image will be pulled
by the CWL runner at runtime.

.. code-block:: bash

   class: DockerRequirement
   dockerPull: quay.io/biocontainers/bwa:0.7.17--h84994c4_5

See example `bwa-docker.yml`_

PM4NGS uses the `Biocontainers Registry`_ through its python interface named bioconda2biocontainer_  to keep
CWL docker images defined in the **docker.yml** file updated to its latest tag. The Bioconda package name and version
defined in the **bioconda.yml**  file is passed as an argument to the update_cwl_docker_from_tool_name_ method in
bioconda2biocontainer returning the latest docker image available for the tool. PM4NGS after cloning the CWL
repository, reads the Bioconda package names and version from the **bioconda.yml** files and updates all defined
docker images to its latest tags modifying all **docker.yml** files.

.. _`bwa-mem.cwl`: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/bwa/bwa-mem.cwl#L9
.. _`bwa-bioconda.yml`: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/bwa/bwa-bioconda.yml
.. _`bwa-docker.yml`: https://github.com/ncbi/cwl-ngs-workflows-cbb/blob/master/tools/bwa/bwa-docker.yml
.. _Biocontainers Registry: https://biocontainers.pro/
.. _bioconda2biocontainer: https://pypi.org/project/bioconda2biocontainer/
.. _update_cwl_docker_from_tool_name: https://github.com/BioContainers/bioconda2biocontainer/blob/master/src/bioconda2biocontainer/update_cwl_docker_image.py#L78
