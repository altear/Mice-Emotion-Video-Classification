# Author: Andre Telfer
# Contact: andretelfer@cmail.carleton.ca

ARG CUDA_VERSION=10.2
FROM nvidia/cuda:${CUDA_VERSION}-cudnn7-devel-ubuntu18.04

# Note: you must find the arch for your gpu from https://developer.nvidia.com/cuda-gpus#compute
ARG CUDA_ARCH_BIN=7.5
ARG OPENCV_VERSION=3.4.10 
ARG INSTALL_PATH=/opencv_install
ARG CUDA_VERSION

ENTRYPOINT /bin/bash

# Install dependencies
RUN apt-get update 
RUN apt-get install -y build-essential cmake unzip pkg-config wget \
    libjpeg-dev libpng-dev libtiff-dev \
    libavcodec-dev libavformat-dev libswscale-dev \
    libv4l-dev libxvidcore-dev libx264-dev \
    libgtk-3-dev libatlas-base-dev gfortran \
    python3-dev python3-numpy

# Download sources
RUN cd /
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip
RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip
RUN unzip opencv.zip && unzip opencv_contrib.zip
RUN mv opencv-${OPENCV_VERSION} opencv && mv opencv_contrib-${OPENCV_VERSION} opencv_contrib

# Build
RUN mkdir ${INSTALL_PATH}
RUN mkdir /opencv/build 
WORKDIR /opencv/build

# Options aren't well documented, so looking at the CMakeLists.txt is the best method
# OpenCV 3.4 => https://github.com/opencv/opencv/blob/3.4/CMakeLists.txt
RUN echo 'test'
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=${INSTALL_PATH} \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D WITH_CUDA=ON \
	-D WITH_CUDNN=ON \
	-D OPENCV_DNN_CUDA=ON \
	-D ENABLE_FAST_MATH=1 \
    -D CUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-10.2 \
	-D CUDA_FAST_MATH=1 \
	-D CUDA_ARCH_BIN=$CUDA_ARCH_BIN \
	-D WITH_CUBLAS=1 \
	-D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules \
	-D HAVE_opencv_python3=ON \
	-D BUILD_EXAMPLES=ON ..

RUN make -j8
RUN make install
ENV PKG_CONFIG_PATH "${INSTALL_PATH}/lib/pkgconfig:${PKG_CONFIG_PATH}"
RUN ldconfig

# Darknet begins here
WORKDIR /
RUN apt-get install -y git
RUN git clone https://github.com/AlexeyAB/darknet.git
RUN sed -i 's/GPU=0/GPU=1/g' /darknet/Makefile
RUN sed -i 's/CUDNN=0/CUDNN=1/g' /darknet/Makefile
RUN sed -i 's/OPENCV=0/OPENCV=1/g' /darknet/Makefile
RUN sed -i 's/LIBSO=0/LIBSO=1/g' /darknet/Makefile

WORKDIR /darknet
RUN make -j8

ENV LD_LIBRARY_PATH "${INSTALL_PATH}/lib:/usr/local/cuda-${CUDA_VERSION}/lib64/stubs:${PATH}"
RUN ldconfig
COPY yolo-obj.cfg .
COPY clean-data.py .
