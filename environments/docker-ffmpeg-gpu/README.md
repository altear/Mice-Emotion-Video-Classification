This is for gpu accelerated ffmpeg use

# Docker Image
```
 docker build -t ffmpeg-gpu .

```

# Usage example

```
sudo docker run --rm -it --gpus all \
    --volume /storage:/workspace \
    ffmpeg-gpu
```

