# Environments
Here is a list of docker environments used in this project. More details can be found by navigating to their respective folders 

## docker-tf
This is the main environment 

It's a GPU environment with 
- jupyter 
- deeplabcut
- tensorflow 2.X

## ffmpeg-gpu
A ffmpeg environment that supports hardware acceleration

This is really just `willprice/nvidia-ffmpeg` with a bash entrypoint

## cvat
cvat is an annotator/labeler tool that is hosted on the web

Install instruction here: https://github.com/opencv/cvat/blob/develop/cvat/apps/documentation/installation.md


# General

## ngrok
Ngrok is a very useful tool for tunnelling out of local networks

If you have at least the lowest tier paid account, it can help you keep familiar domains on new webservers

There's an `ngrok-config.yml.template` file in this folder. To use it, rename to `ngrok-config.yml` and set the values for authtoken and subdomains (which can be found by logging into ngrok's website). Then run using 
Example: 
```
./ngrok start -config /path/to/ngrok-config.yml cvat jupyter
```

## Watching resources

### CPU
```
top
```

### GPU
```
watch -d -n 0.5 nvidia-smi
```
