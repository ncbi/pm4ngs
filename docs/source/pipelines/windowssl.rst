.. _windowssl:

#####################################
PM4NGS on Windows Subsystem for Linux
#####################################

PM4NGS can be installed on Microsoft Windows 10 using the Windows Subsystem for Linux (WSL) and Docker.

Activating WSL
--------------

Follow the steps for activating WSL

1.	Open the Settings app
2.	Go to Apps -> Apps & Features
3.	Scroll down to the Programs and Feature link
4.	Click the link. The Programs and Features dialog will be opened.
5.	On the left, click the link Turn Windows Features on or off.
6.	The dialog Windows Features will appear on the screen. Scroll down to the option named Windows Subsystem for Linux and enable it
7.	Click OK to apply the changes you made. Windows will install WSL.

.. image:: /_images/win/wsl_activation.png
    :width: 800px
    :align: center
    :alt: Activating WSL on Windows 10

8.	Reboot the operating system when prompted.

Installing Docker
-----------------

Before you install the Docker Desktop WSL 2 backend, you must complete the following steps:

1. Install Windows 10, version 2004 or higher. The Docker Desktop Edge release also supports Windows 10, version 1903 or higher.
2. Enable WSL 2 feature on Windows. For detailed instructions, refer to the `Microsoft documentation`_.

Download and install the `Linux kernel update package`_.

Download `Docker Desktop Stable 2.3.0.2`_ or a later release. After installed, open the Docker Setting and activate the
WSL 2. Then, click on Apply and Restart.

.. image:: /_images/win/activatewsldocker.png
    :width: 800px
    :align: center
    :alt: Activating WSL 2 on Docker

Open a PowerShell as Administrator for activating WSL 2 as default option runnign the command

.. code-block:: bash

    wsl.exe --set-default-version 2

.. image:: /_images/win/powershell.png
    :width: 800px
    :align: center
    :alt: Activating WSL 2 as default version

.. image:: /_images/win/powershell1.png
    :width: 800px
    :align: center
    :alt: Activating WSL 2 as default version

Installing Ubuntu on WSL
------------------------

Open Microsoft Store and search for Linux, then install the Linux distribution that you like. We recommend Ubuntu 20.04 LTS.

.. image:: /_images/win/storelinux.png
    :width: 800px
    :align: center
    :alt: Search for Linux on the Microsoft Store

Lunch Ubuntu


Installing PM4NGS
-----------------

Runs these commands on the Ubuntu terminal to to prepare the instance to run PM4NGS

.. code-block:: bash

    veraalva@perseo:~$ sudo apt-get update
    veraalva@perseo:~$ sudo apt-get install python3 python3-pip python3-venv python3-dev poppler-utils gcc nodejs docker.io
    veraalva@perseo:~$ sudo usermod -aG docker $USER

Close and reopen the terminal to set the docker group in the user.

Creates a Python virtual environment named: **pm4ngs_venv** for installing PM4NGS

.. code-block:: bash

    veraalva@perseo:~$ python3 -m venv pm4ngs_venv
    veraalva@perseo:~$ source pm4ngs_venv/bin/activate
    (pm4ngs_venv) veraalva@perseo:~$ pip install wheel
    (pm4ngs_venv) veraalva@perseo:~$ pip install pm4ngs

Using PM4NGS on WSL
-------------------

Open the Ubuntu app in Windows and activate the **pm4ngs_venv** virtual environment

.. code-block:: bash

    veraalva@perseo:~$ source pm4ngs_venv/bin/activate
    (pm4ngs_venv) veraalva@perseo:~$ pm4ngs-chipexo --version
    PM4NGS version: 0.0.4
    (pm4ngs_venv) veraalva@perseo:~$

.. image:: /_images/win/pm4ngs1.png
    :width: 800px
    :align: center
    :alt: Running PM4NGS

Running the ChIP-exo demo
-------------------------

Open the Ubuntu app in Windows and activate the **pm4ngs_venv** virtual environment

.. code-block:: bash

    veraalva@perseo:~$ source pm4ngs_venv/bin/activate
    (pm4ngs_venv) veraalva@perseo:~$ pm4ngs-chipexo-demo
    Generating demo for ChIP-exo data analysis project
    Downloading file: pm4ngs_chipexo_demo_config.yaml
    Downloading file: pm4ngs_chipexo_demo_sample_data.csv
    Using config file: pm4ngs_chipexo_demo_config.yaml
    {
        "author_name": "Roberto Vera Alvarez",
        "user_email": "veraalva@ncbi.nlm.nih.gov",
        "project_name": "pm4ngs-chipexo",
        "dataset_name": "PRJNA338159",
        "is_data_in_SRA": "y",
        "sequencing_technology": "single-end",
        "create_demo": "n",
        "number_spots": "1000000",
        "organism": "Escherichia coli",
        "genome_name": "NC_000913.3",
        "genome_dir": "{{ cookiecutter.genome_name}}",
        "aligner_index_dir": "{{ cookiecutter.genome_dir}}/BWA/",
        "genome_fasta": "{{ cookiecutter.genome_dir}}/NC_000913.3.fa",
        "genome_gtf": "{{ cookiecutter.genome_dir}}/NC_000913.3.gtf",
        "genome_chromsizes": "{{ cookiecutter.genome_dir}}/NC_000913.3.sizes",
        "use_docker": "y",
        "max_number_threads": "32"
    }
    Cloning Git repo: https://github.com/ncbi/cwl-ngs-workflows-cbb to /home/veraalva/pm4ngs-chipexo/bin/cwl
    Updating CWLs dockerPull and SoftwareRequirement from: /home/veraalva/pm4ngs-chipexo/requirements/conda-env-dependencies.yaml
    bamscale with version 0.0.3 update image to: quay.io/biocontainers/bamscale:0.0.3--ha85820d_0
        /Users/veraalva/my_ngs_project/bin/cwl/tools/bamscale/bamscale-docker.yml with old image replaced: quay.io/biocontainers/bamscale:0.0.5--h18f8b1d_1
    bedtools with version 2.29.2 update image to: quay.io/biocontainers/bedtools:2.29.2--hc088bd4_0
        /Users/veraalva/my_ngs_project/bin/cwl/tools/bedtools/bedtools-docker.yml with old image replaced: quay.io/biocontainers/bedtools:2.28.0--hdf88d34_0
    bioconductor-diffbind with version 2.16.0 update image to: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_0
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/deseq2-pca.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/macs-cutoff.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/dga_heatmaps.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/diffbind.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/edgeR-2conditions.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/volcano_plot.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/readQC.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/R/deseq2-2conditions.cwl with old image replaced: quay.io/biocontainers/bioconductor-diffbind:2.16.0--r40h5f743cb_2
    bwa with version 0.7.17 update image to: quay.io/biocontainers/bwa:0.7.17--hed695b0_7
        /Users/veraalva/my_ngs_project/bin/cwl/tools/bwa/bwa-docker.yml with old image replaced: quay.io/biocontainers/bwa:0.7.17--h84994c4_5
    There is not biocontainer image for gffread version 0.12.1
    homer with version 4.11 update image to: quay.io/biocontainers/homer:4.11--pl526h9a982cc_2
        /Users/veraalva/my_ngs_project/bin/cwl/tools/homer/homer-docker.yml with old image replaced: quay.io/biocontainers/homer:4.11--pl526h2bce143_2
    mace with version 1.2 update image to: quay.io/biocontainers/mace:1.2--py27h99da42f_0
        /Users/veraalva/my_ngs_project/bin/cwl/tools/mace/mace-docker.yml with old image replaced: quay.io/biocontainers/mace:1.2--py27h99da42f_1
    meme with version 5.1.1 update image to: quay.io/biocontainers/meme:5.1.1--py37pl526h072abfd_3
        /Users/veraalva/my_ngs_project/bin/cwl/tools/meme/meme-docker.yml with old image replaced: quay.io/biocontainers/meme:5.1.1--py27pl526h53063a7_3
    Copying file /Users/veraalva/Work/Developer/Python/pm4ngs/pm4ngs-chipexo/example/pm4ngs_chipexo_demo_sample_data.csv  to /Users/veraalva/my_ngs_project/data/my_dataset_name/sample_table.csv
    6 files loaded
    Using table:
      sample_name file                     condition  replicate
    0  SRR4011416        Exp_O2_growth_no_rifampicin          1
    1  SRR4011417        Exp_O2_growth_no_rifampicin          2
    2  SRR4011421           Exp_O2_growth_rifampicin          1
    3  SRR4011425           Exp_O2_growth_rifampicin          2
    4  SRR4011418       Stat_02_growth_no_rifampicin          1
    5  SRR4011419       Stat_02_growth_no_rifampicin          2
     Done

Running the Jupyter Server
--------------------------

Open the Ubuntu app in Windows and activate the **pm4ngs_venv** virtual environment

.. code-block:: bash

    veraalva@perseo:~$ source pm4ngs_venv/bin/activate
    (pm4ngs_venv) veraalva@perseo:~$ jupyter notebook --no-browser
    [I 17:04:45.633 NotebookApp] Serving notebooks from local directory: /home/veraalva
    [I 17:04:45.633 NotebookApp] Jupyter Notebook 6.1.4 is running at:
    [I 17:04:45.634 NotebookApp] http://localhost:8888/?token=90bcbcda87e5421cf451e6a58d88bfa212355b36f0ed7f1a
    [I 17:04:45.634 NotebookApp]  or http://127.0.0.1:8888/?token=90bcbcda87e5421cf451e6a58d88bfa212355b36f0ed7f1a
    [I 17:04:45.634 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 17:04:45.637 NotebookApp]

        To access the notebook, open this file in a browser:
            file:///home/veraalva/.local/share/jupyter/runtime/nbserver-522-open.html
        Or copy and paste one of these URLs:
            http://localhost:8888/?token=90bcbcda87e5421cf451e6a58d88bfa212355b36f0ed7f1a
         or http://127.0.0.1:8888/?token=90bcbcda87e5421cf451e6a58d88bfa212355b36f0ed7f1a

Copy the URL with localhost in a browser:

.. image:: /_images/win/chipexo.png
    :width: 800px
    :align: center
    :alt: Running PM4NGS


.. _Microsoft documentation: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Linux kernel update package: https://docs.microsoft.com/windows/wsl/wsl2-kernel
.. _Docker Desktop Stable 2.3.0.2: https://hub.docker.com/editions/community/docker-ce-desktop-windows/