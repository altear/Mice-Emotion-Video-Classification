# DLC-CPU Environment
For using DeepLabCut's UI tools

```
conda env create -f DLC-CPU.yaml
```

Once installed, you can add the kernel to access it from Jupyter

```
activate DLC-CPU
python -m ipykernel install --user --name DLC-CPU --display-name "DLC-CPU"
```
**Note**: At the time of writing this, there was an issue with h5py (showed as a cython error). This was fixed by downgrading h5py using `pip install h5py==2.9` 