## Installation for Using NVIDIA GPU Device
License Plate Object Detection is the part of our Deep Learning Pipeline where we need to identify Region of Interest of the license plate that we want to recognize. Our Object Detection model will be using a ***YOLOv5*** method which has been created by ***ultralytics***. All Credits goes to every people who are involve in bringing YOLOv5 Method to live. The code can be accessed using this link https://github.com/ultralytics/yolov5.

The training of the data will be using NVIDIA GeForce GTX 1660 Ti device. But there are some things that we need to prepare for this project such as:
1. Installing CUDA Toolkit version 10.2 (use this [link](https://developer.nvidia.com/cuda-10.2-download-archive) for downloading it)
2. Installing CuDNN version 8.3.0 (or pick other version that is compatible with CUDA Toolkit version, check this [link](https://developer.nvidia.com/rdp/cudnn-archive) for further information)
3. Installing NVIDIA driver from this [link](https://www.nvidia.com/download/index.aspx) and choose the driver based on your GPU device name and type.
4. Installing Visual Studio 2019 using this [link](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=community&rel=16&utm_medium=microsoft&utm_source=docs.microsoft.com&utm_campaign=download+from+relnotes&utm_content=vs2019ga+button) 

## Setting Up Environment
Python environment can be created using [anaconda](https://www.anaconda.com/) or [pipenv](https://pipenv.pypa.io/en/latest/) package by Python. In this project, pipenv is a tool that has been chosen for setting up environment. For starting things off, download the any Python version from this [link](https://www.python.org/downloads/). After that, go to command line and run command this command for installing pipenv package: 

```pip install pipenv``` 

Copy this folder into your local data or clone the GitHub repo by running command:

```git clone https://github.com/marcellinus-witarsah/VePay-Go-ML.git```

Then setting up the environment at your project directory folder (/license-plate-object-detection) by running this command for automatically create an environment and install all dependencies from Pipfile: 

```python -m pipenv install```

Then you want to access or activate the environment using this command: 

```python -m pipenv shell```

Next, we need to install libaries to enable pytorch to access GPU by installing python packages by using this command
***pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html***

This command can be run in the jupyter notebook or in the command line (***make sure to run the command in the python environment we just created***)
