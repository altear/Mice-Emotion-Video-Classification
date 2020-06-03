# Docker TF
This document is about setting up a dev server with GPU

## Installation
Assumes CUDA, cuDNN are already installed

1. Install Docker: https://docs.docker.com/engine/install/ubuntu/
2. Install nvidia-docker: https://github.com/NVIDIA/nvidia-docker   
   it may be useful to run the following commands separately    
   ```
    sudo apt-get update
    sudo apt-get install -y nvidia-container-toolkit
   ```    
   also restart docker `sudo systemctl restart docker`
3. Install tools: 
   - tmux: long-running multi sessions
   - ngrok: tunnel through VPN to expose notebook 
4. TF Docker Image: https://www.tensorflow.org/install/docker    
   Currently `docker pull tensorflow/tensorflow:latest-gpu-jupyter`

**Note**: At the time of writing this, there was an issue with h5py (showed as a cython error). This was fixed by downgrading h5py using `pip install h5py==2.9` 

## Build
```
sudo docker build -t mouse-emotion .
```

## Launching
Use the following command. Make modifications to volume, notebookdir, and token depending on system.

```
sudo docker run \
    -v /storage:/storage \
    -it --gpus all \
    -p 8888:8888 \
    mouse-emotion \
    jupyter lab \
        --ip 0.0.0.0 --port 8888 --no-browser --allow-root \
        --NotebookApp.token="yourtoken" \
        --NotebookApp.allow_origin=* \
        --NotebookApp.notebook_dir=/storage
```



