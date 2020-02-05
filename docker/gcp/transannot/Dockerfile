# Base Image
FROM gcr.io/cloud-marketplace-containers/google/ubuntu1804

# Metadata
LABEL base.image="gcr.io/cloud-marketplace-containers/google/ubuntu1804"
LABEL version="1"
LABEL software="transcriptome-annotation"
LABEL software.version="0.0.1"
LABEL description=""
LABEL tags="transcriptome"
LABEL website="https://github.com/ncbi/pm4ngs"

# Maintainer
MAINTAINER Roberto Vera Alvarez <veraalva@ncbi.nlm.nih.gov>

RUN apt-get update && \
    apt-get install -y wget parallel locales-all && \
    apt-get clean && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Updating Anaconda packages
RUN wget -O /tmp/Miniconda3-latest-Linux-x86_64.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN sh /tmp/Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr
RUN conda update conda
RUN conda update --all
RUN conda config --add channels defaults && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge

# Adding Bioconda packages
RUN wget -O /tmp/conda-jupyter.yaml https://raw.githubusercontent.com/ncbi/cwl-ngs-workflows-cbb/master/requirements/conda-jupyter.yaml
RUN conda env update -n base -f /tmp/conda-jupyter.yaml
RUN conda install -c bioconda galaxy-lib
RUN wget -O /tmp/conda-trans-annot.yaml https://raw.githubusercontent.com/ncbi/cwl-ngs-workflows-cbb/master/requirements/conda-trans-annot.yaml
RUN conda env create -f /tmp/conda-trans-annot.yaml
RUN rm -v /tmp/conda-jupyter.yaml /tmp/conda-trans-annot.yaml

# Add user ubuntu with no password, add to sudo group
RUN locale -a
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV PATH="/usr/envs/transannot/bin:${PATH}"

WORKDIR /data/

CMD ["/bin/bash", "-c"]
