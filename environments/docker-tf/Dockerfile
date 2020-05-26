FROM tensorflow/tensorflow:latest-gpu

# Install tools
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git wget libgtk2.0-dev libxxf86vm1 ffmpeg

WORKDIR /temp

# Install Anaconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
RUN bash ~/miniconda.sh -b -p $HOME/miniconda
RUN sed -e 's|PATH="\(.*\)"|PATH="/root/miniconda/bin:\1"|g' -i /etc/environment
ENV PATH="/root/miniconda/bin:${PATH}"

# Install Jupyter
RUN conda install -c conda-forge jupyterlab

# Install DLC
RUN git clone https://github.com/DeepLabCut/DeepLabCut.git
RUN conda env create -f ./DeepLabCut/conda-environments/DLC-GPU.yaml
RUN /bin/bash -c "source activate DLC-GPU"
RUN python -m ipykernel install --user --name DLC-GPU --display-name "DLC-GPU"
ENV DLClight=True 

WORKDIR /storage
ENTRYPOINT ["/bin/bash"]