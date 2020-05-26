FROM tensorflow/tensorflow:latest-gpu

# Install tools
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git wget

WORKDIR /temp

# Install Anaconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
RUN bash ~/miniconda.sh -b -p $HOME/miniconda
ENV PATH="${HOME}/miniconda/bin:${PATH}"

# Install Jupyter
RUN conda install -c conda-forge jupyterlab

# Install DLC
RUN git clone https://github.com/DeepLabCut/DeepLabCut.git
RUN conda env create -f ./DeepLabCut/conda-environments/DLC-GPU.yaml
RUN activate DLC-GPU
RUN python -m ipykernel install --user --name DLC-GPU --display-name "DLC-GPU"

