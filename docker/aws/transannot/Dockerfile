# Base Image
FROM amazonlinux:latest

# Metadata
LABEL base.image="amazonlinux:latest"
LABEL version="1"
LABEL software="transcriptome-annotation"
LABEL software.version="0.0.1"
LABEL description=""
LABEL tags="transcriptome"
LABEL website="https://github.com/ncbi/pm4ngs"

# Maintainer
MAINTAINER Roberto Vera Alvarez <veraalva@ncbi.nlm.nih.gov>

RUN yum update -y && \
    yum install -y wget unzip git && \
    yum clean all && \
    rm -rf /var/cache/yum /tmp/* /var/tmp/*

# Updating Anaconda packages
RUN wget -O /tmp/Miniconda3-latest-Linux-x86_64.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN sh /tmp/Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr
RUN conda update conda
RUN conda update --all
RUN conda config --add channels defaults && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge
RUN rm -v /tmp/Miniconda3-latest-Linux-x86_64.sh

# Adding Bioconda packages
RUN wget -O /tmp/conda-jupyter.yaml https://raw.githubusercontent.com/ncbi/cwl-ngs-workflows-cbb/master/requirements/conda-jupyter.yaml
RUN conda env update -n base -f /tmp/conda-jupyter.yaml
RUN conda install -c bioconda galaxy-lib
RUN wget -O /tmp/conda-trans-annot.yaml https://raw.githubusercontent.com/ncbi/cwl-ngs-workflows-cbb/master/requirements/conda-trans-annot.yaml
RUN conda env create -f /tmp/conda-trans-annot.yaml
RUN rm -v /tmp/conda-jupyter.yaml /tmp/conda-trans-annot.yaml
RUN conda install -n transannot parallel
RUN wget -O /usr/envs/transannot/bin/update_blastdb.pl ftp://ftp.ncbi.nlm.nih.gov/blast/temp/camacho/update_blastdb.pl
RUN wget -O /tmp/awscliv2.zip https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip
RUN cd /tmp && unzip awscliv2.zip && ./aws/install && rm -rf aws awscliv2.zip
ADD pipeline.sh /usr/bin/pipeline.sh
RUN chmod a+x /usr/bin/pipeline.sh

RUN mkdir /home/nobody
RUN chmod a+rwx /home/nobody
RUN chown -R nobody /home/nobody
# Add user nobody with no password, add to sudo group
USER nobody
RUN locale -a
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV PATH="/usr/envs/transannot/bin:${PATH}"

RUN cd /home/nobody && \
    git clone https://github.com/ncbi/cwl-ngs-workflows-cbb

WORKDIR /data/
