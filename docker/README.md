Docker deployment
=================

This folder include Dockerfiles for the creation of Docker images and the deployment of the Jupyter Notebook 
inside a Docker container.

Image build
-----------

Download from this folder the Dockerfile for the pipeline you're going to use. The examples are for the 
Dockerfile-RNASeq-DGA pipeline.

    docker build -t jupyter-rnaseq-pipeline https://raw.githubusercontent.com/ncbi/cookiecutter-jupyter-ngs/master/docker/Dockerfile-RNASeq-DGA
    
Initialization of the data structure
------------------------------------

The container working directory is **/data**. Therefore, you should mount the host directory with your data as a volume
pointing to the **/data** directory.

For initializing the project structure, the container expect to find a file named **config.yaml** in that folder
with all information about the project that will be created. This file is like the examples included in the **example** 
folder.

    docker run -t -i -u 1000:1000 -v /home/myuser/data:/data jupyter-rnaseq-pipeline:latest init.sh
    
In this command the **-u** option uses the user UID and GID to map the data volume. 

Starting the Jupyter server
---------------------------

    docker run -t -i -u 1000:1000 -p 8888:8888 -v /home/myuser/data:/data jupyter-rnaseq-pipeline:latest
    
In this command the **-p** option will map the port used by the container jupyter server to the host port.
 
You should get an output like this:

    perseo:docker> docker run -t -i -u 1000:1000 -p 8888:8888 -v /home/myuser/data:/data jupyter-rnaseq-pipeline:latest
    [I 18:36:07.480 NotebookApp] Writing notebook server cookie secret to /home/ubuntu/.local/share/jupyter/runtime/notebook_cookie_secret
    [I 18:36:07.776 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.6/site-packages/jupyterlab
    [I 18:36:07.776 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
    [I 18:36:07.779 NotebookApp] Serving notebooks from local directory: /data
    [I 18:36:07.779 NotebookApp] The Jupyter Notebook is running at:
    [I 18:36:07.779 NotebookApp] http://(b1e4e47b1ad8 or 127.0.0.1):8888/?token=3f9281a106780f6c260743d8068048d4953ee1165f26d5b6
    [I 18:36:07.779 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 18:36:07.784 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/ubuntu/.local/share/jupyter/runtime/nbserver-7-open.html
    Or copy and paste one of these URLs:
        http://(b1e4e47b1ad8 or 127.0.0.1):8888/?token=3f9281a106780f6c260743d8068048d4953ee1165f26d5b6
        
The last line will give you the URL to be used in your host.

If the browser is used locally:
    
     http://127.0.0.1:8888/?token=3f9281a106780f6c260743d8068048d4953ee1165f26d5b6
     
If the browser is used remotely:

    http://(USE HOST IP or NAME here):8888/?token=3f9281a106780f6c260743d8068048d4953ee1165f26d5b6