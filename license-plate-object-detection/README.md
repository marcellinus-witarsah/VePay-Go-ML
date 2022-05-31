## Installation for Using NVIDIA GPU Device
License Plate Object Detection is the part of our Deep Learning Pipeline where we need to identify Region of Interest of the license plate that we want to recognize. Our Object Detection model will be using a ***YOLOv5*** method which has been created by ***ultralytics***. All Credits goes to every people who are involve in bringing YOLOv5 Method to live. The code can be accessed using this link https://github.com/ultralytics/yolov5.

The training of the data will be using NVIDIA GeForce GTX 1660 Ti device. But there are some things that we need to prepare for this project such as:
1. Installing CUDA Toolkit version 10.2 (use this [link](https://developer.nvidia.com/cuda-10.2-download-archive) for downloading it)
2. Installing CuDNN version 8.3.0 (or pick other version that is compatible with CUDA Toolkit version, check this [link](https://developer.nvidia.com/rdp/cudnn-archive) for further information)
3. Installing NVIDIA driver from this [link](https://www.nvidia.com/download/index.aspx) and choose the driver based on your GPU device name and type.
4. Installing Visual Studio 2019 using this [link](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=community&rel=16&utm_medium=microsoft&utm_source=docs.microsoft.com&utm_campaign=download+from+relnotes&utm_content=vs2019ga+button) 
