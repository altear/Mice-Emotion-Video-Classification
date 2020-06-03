sudo docker run \
    -v /storage:/workspace \
    -it --gpus all \
    -p 8888:8888 \
    mouse-emotion \
    jupyter lab \
        --ip 0.0.0.0 --port 8888 --no-browser --allow-root \
        --NotebookApp.token="yourtoken" \
        --NotebookApp.allow_origin=* \
        --NotebookApp.notebook_dir=/workspace