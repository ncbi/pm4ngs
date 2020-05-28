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
    apt-get install -y wget locales-all && \
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
COPY conda-trans-annot.yaml /tmp/conda-trans-annot.yaml
RUN conda env create -f /tmp/conda-trans-annot.yaml
RUN conda clean --all
RUN rm /tmp/conda-trans-annot.yaml /tmp/Miniconda3-latest-Linux-x86_64.sh

# Add user ubuntu with no password, add to sudo group
RUN locale -a
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV PATH="/usr/envs/transannot/bin:${PATH}"
COPY aws-pipeline.sh /usr/envs/transannot/bin/
RUN chmod a+x /usr/envs/transannot/bin/aws-pipeline.sh
RUN vdb-config --report-cloud-identity yes --accept-gcp-charges no

WORKDIR /data/

CMD ["/bin/bash", "-c"]
