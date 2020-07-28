This is for gpu accelerated ffmpeg use

# Docker Image
```
 docker build -t ffmpeg-gpu .

```

# Usage example

```
sudo docker run --rm -it --gpus all \
    --volume /storage:/storage \
    ffmpeg-gpu
```

## Downsample Frames

```
ffmpeg -vsync 0 –hwaccel cuvid -c:v h264_cuvid –resize 1280x720 -i input.mp4 -c:a copy -c:v h264_nvenc -b:v 5M output.mp4
```