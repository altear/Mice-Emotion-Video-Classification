# Darknet-OpenCV-GPU
Builds OpenCV (3.4 by default) with CUDA 
Builds Darknet with OpenCV/CUDA

## Setup
1. Find your GPU arch type on https://developer.nvidia.com/cuda-gpus#compute (aka `Compute Capability`) and set it in the docker file args.
2. Configure other args according to your needs (opencv, cuda, etc)
3. Run `bash.sh`, which will create an image with tag `darknet-opencv-gpu`

## Run Example
```
sudo docker run \
    -it --gpus=all \
    -v /storage:/storage \
    darknet-opencv-gpu
```

Note that if you don't run `--gpus=all` with darknet it wont work

### Training
1. Label data locally with yolo_mark (or setup [cvat](https://github.com/opencv/cvat))
2. Move data folder to the training server
3. Modify the yolo-obj.cfg according to darknet's guide (can be found in their github readme)
4. Run this dockerfile, make sure to mount the volume that contains the training data
5. Download the training weights. For v4 this is `https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137`
6. Link your data to the data in the darknet repo, ie `ln -s /storage/gs/rat-emotion/2020-05-30/data/ data`
7. Train. Modify paths according to your setup, more info is found on darknet's github readme
   ```
    ./darknet detector train data/obj.data yolo-obj.cfg yolov4.conv.137 -dont_show -mjpeg_port 8090
   ```


## Resources
Many of the steps for the OpenCV installation are described in greater detail in this article

https://www.pyimagesearch.com/2020/02/03/how-to-use-opencvs-dnn-module-with-nvidia-gpus-cuda-and-cudnn/

## Contact
Author: Andre Telfer
Email: andretelfer@cmail.carleton.ca