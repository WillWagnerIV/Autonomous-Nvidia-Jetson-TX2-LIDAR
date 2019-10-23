<img src="https://github.com/dusty-nv/jetson-inference/raw/master/docs/images/deep-vision-header.jpg">

# Deploying Deep Learning
Welcome to our instructional guide for inference and realtime [DNN vision](#api-reference) library for NVIDIA **[Jetson Nano/TX1/TX2/Xavier](http://www.nvidia.com/object/embedded-systems.html)**.

This repo uses NVIDIA **[TensorRT](https://developer.nvidia.com/tensorrt)** for efficiently deploying neural networks onto the embedded Jetson platform, improving performance and power efficiency using graph optimizations, kernel fusion, and FP16/INT8 precision.

Vision primitives, such as [`imageNet`](c/imageNet.h) for image recognition, [`detectNet`](c/detectNet.h) for object localization, and [`segNet`](c/segNet.h) for semantic segmentation, inherit from the shared [`tensorNet`](c/tensorNet.h) object.  Examples are provided for streaming from live camera feed and processing images.  See the **[API Reference](#api-reference)** section for detailed reference documentation of the C++ and Python libraries. 

<img src="https://github.com/dusty-nv/jetson-inference/raw/master/docs/images/deep-vision-primitives.png" width="800">

There are multiple tracks of the tutorial that you can choose to follow, including [Hello AI World](#hello-ai-world) for running inference and transfer learning onboard your Jetson, or the full [Two Days to a Demo](#two-days-to-a-demo-digits) tutorial for training on a PC or server with DIGITS.  

It's recommended to walk through the Hello AI World module first to familiarize yourself with machine learning and inference with TensorRT, before proceeding to training in the cloud with DIGITS.

### Table of Contents

* [Hello AI World](#hello-ai-world)
* [Two Days to a Demo](#two-days-to-a-demo-digits)
* [API Reference](#api-reference)
* [Code Examples](#code-examples)
* [Pre-Trained Models](#pre-trained-models)
* [System Requirements](#recommended-system-requirements)
* [Extra Resources](#extra-resources)

> &gt; &nbsp; Jetson Nano Developer Kit and JetPack 4.2.2 is now supported in the repo. <br/>
> &gt; &nbsp; See our latest technical blog including benchmarks, [`Jetson Nano Brings AI Computing to Everyone`](https://devblogs.nvidia.com/jetson-nano-ai-computing/). <br/>
> &gt; &nbsp; Hello AI World now supports Python and onboard training with PyTorch!

## Hello AI World

Hello AI World can be run completely onboard your Jetson, including inferencing with TensorRT and transfer learning with PyTorch.  The inference portion of Hello AI World - which includes coding your own image classification application for C++ or Python, object detection, and live camera demos - can be run on your Jetson in roughly two hours or less, while transfer learning is best left to leave running overnight.

* [Setting up Jetson with JetPack](docs/jetpack-setup-2.md)
* [Building the Project from Source](docs/building-repo-2.md)
* [Classifying Images with ImageNet](docs/imagenet-console-2.md)
	* [Using the Console Program on Jetson](docs/imagenet-console-2.md#using-the-console-program-on-jetson)
	* [Coding Your Own Image Recognition Program (Python)](docs/imagenet-example-python-2.md)
	* [Coding Your Own Image Recognition Program (C++)](docs/imagenet-example-2.md)
	* [Running the Live Camera Recognition Demo](docs/imagenet-camera-2.md)
* [Locating Objects with DetectNet](docs/detectnet-console-2.md)
	* [Detecting Objects from the Command Line](docs/detectnet-console-2.md#detecting-objects-from-the-command-line)
	* [Running the Live Camera Detection Demo](docs/detectnet-camera-2.md)
	* [Coding Your Own Object Detection Program](docs/detectnet-example-2.md)
* [Semantic Segmentation with SegNet](docs/segnet-console-2.md)
	* [Segmenting Images from the Command Line](docs/segnet-console-2.md#segmenting-images-from-the-command-line)
	* [Running the Live Camera Segmentation Demo](docs/segnet-camera-2.md)
* [Transfer Learning with PyTorch](docs/pytorch-transfer-learning.md)
	* [Re-training on the Cat/Dog Dataset](docs/pytorch-cat-dog.md)
	* [Re-training on the PlantCLEF Dataset](docs/pytorch-plants.md)
	* [Collecting your own Datasets](docs/pytorch-collect.md)

## Two Days to a Demo (DIGITS)

The full tutorial includes training in the cloud or PC, and inference on the Jetson with TensorRT, and can take roughly two days or more depending on system setup, downloading the datasets, and the training speed of your GPU.

* [DIGITS Workflow](docs/digits-workflow.md) 
* [DIGITS System Setup](docs/digits-setup.md)
* [Setting up Jetson with JetPack](docs/jetpack-setup.md)
* [Building the Project from Source](docs/building-repo.md)
* [Classifying Images with ImageNet](docs/imagenet-console.md)
	* [Using the Console Program on Jetson](docs/imagenet-console.md#using-the-console-program-on-jetson)
	* [Coding Your Own Image Recognition Program](docs/imagenet-example.md)
	* [Running the Live Camera Recognition Demo](docs/imagenet-camera.md)
	* [Re-Training the Network with DIGITS](docs/imagenet-training.md)
	* [Downloading Image Recognition Dataset](docs/imagenet-training.md#downloading-image-recognition-dataset)
	* [Customizing the Object Classes](docs/imagenet-training.md#customizing-the-object-classes)
	* [Importing Classification Dataset into DIGITS](docs/imagenet-training.md#importing-classification-dataset-into-digits)
	* [Creating Image Classification Model with DIGITS](docs/imagenet-training.md#creating-image-classification-model-with-digits)
	* [Testing Classification Model in DIGITS](docs/imagenet-training.md#testing-classification-model-in-digits)
	* [Downloading Model Snapshot to Jetson](docs/imagenet-snapshot.md)
	* [Loading Custom Models on Jetson](docs/imagenet-custom.md)
* [Locating Objects with DetectNet](docs/detectnet-training.md)
	* [Detection Data Formatting in DIGITS](docs/detectnet-training.md#detection-data-formatting-in-digits)
	* [Downloading the Detection Dataset](docs/detectnet-training.md#downloading-the-detection-dataset)
	* [Importing the Detection Dataset into DIGITS](docs/detectnet-training.md#importing-the-detection-dataset-into-digits)
	* [Creating DetectNet Model with DIGITS](docs/detectnet-training.md#creating-detectnet-model-with-digits)
	* [Testing DetectNet Model Inference in DIGITS](docs/detectnet-training.md#testing-detectnet-model-inference-in-digits)
	* [Downloading the Detection Model to Jetson](docs/detectnet-snapshot.md)
	* [DetectNet Patches for TensorRT](docs/detectnet-snapshot.md#detectnet-patches-for-tensorrt)
	* [Detecting Objects from the Command Line](docs/detectnet-console.md)
	* [Multi-class Object Detection Models](docs/detectnet-console.md#multi-class-object-detection-models)
	* [Running the Live Camera Detection Demo on Jetson](docs/detectnet-camera.md)
* [Semantic Segmentation with SegNet](docs/segnet-dataset.md)
	* [Downloading Aerial Drone Dataset](docs/segnet-dataset.md#downloading-aerial-drone-dataset)
	* [Importing the Aerial Dataset into DIGITS](docs/segnet-dataset.md#importing-the-aerial-dataset-into-digits)
	* [Generating Pretrained FCN-Alexnet](docs/segnet-pretrained.md)
	* [Training FCN-Alexnet with DIGITS](docs/segnet-training.md)
	* [Testing Inference Model in DIGITS](docs/segnet-training.md#testing-inference-model-in-digits)
	* [FCN-Alexnet Patches for TensorRT](docs/segnet-patches.md)
	* [Running Segmentation Models on Jetson](docs/segnet-console.md)

## API Reference

Below are links to reference documentation for the [C++](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/index.html) and [Python](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/python/jetson.html) libraries from the repo:

#### jetson-inference

|                   | [C++](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/group__deepVision.html) | [Python](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/python/jetson.inference.html) |
|-------------------|--------------|--------------|
| Image Recognition | [`imageNet`](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/classimageNet.html) | [`imageNet`](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/python/jetson.inference.html#imageNet) |
| Object Detection  | [`detectNet`](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/classdetectNet.html) | [`detectNet`](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/python/jetson.inference.html#detectNet)
| Segmentation      | [`segNet`](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/classsegNet.html) | [`segNet`](https://rawgit.com/dusty-nv/jetson-inference/pytorch/docs/html/python/jetson.inference.html#segNet) |

#### jetson-utils

* [C++](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/group__util.html)
* [Python](https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/python/jetson.utils.html)

These libraries are able to be used in external projects by linking to `libjetson-inference` and `libjetson-utils`.

## Code Examples

Introductory code walkthroughs of using the library are covered during these steps of the Hello AI World tutorial:

* [Coding Your Own Image Recognition Program (Python)](docs/imagenet-example-python-2.md)
* [Coding Your Own Image Recognition Program (C++)](docs/imagenet-example-2.md)

Additional C++ and Python samples for running the networks on static images and live camera streams can be found here:

|                   | Images              | Camera              |
|-------------------|---------------------|---------------------|
| **C++ ([`examples`](examples/))** | |
| &nbsp;&nbsp;&nbsp;Image Recognition | [`imagenet-console`](examples/imagenet-console/imagenet-console.cpp) | [`imagenet-camera`](examples/imagenet-camera/imagenet-camera.cpp) |
| &nbsp;&nbsp;&nbsp;Object Detection  | [`detectnet-console`](examples/detectnet-console/detectnet-console.cpp) | [`detectnet-camera`](examples/detectnet-camera/detectnet-camera.cpp)
| &nbsp;&nbsp;&nbsp;Segmentation      | [`segnet-console`](examples/segnet-console/segnet-console.cpp) | [`segnet-camera`](examples/segnet-camera/segnet-camera.cpp) |
| **Python ([`python/examples`](python/examples/))** | | |
| &nbsp;&nbsp;&nbsp;Image Recognition | [`imagenet-console.py`](python/examples/imagenet-console.py) | [`imagenet-camera.py`](python/examples/imagenet-camera.py) |
| &nbsp;&nbsp;&nbsp;Object Detection  | [`detectnet-console.py`](python/examples/detectnet-console.py) | [`detectnet-camera.py`](python/examples/detectnet-camera.py) |
| &nbsp;&nbsp;&nbsp;Segmentation      | [`segnet-console.py`](python/examples/segnet-console.py) | [`segnet-camera.py`](python/examples/segnet-camera.py) |

> **note**:  for working with numpy arrays, see [`cuda-from-numpy.py`](https://github.com/dusty-nv/jetson-utils/blob/master/python/examples/cuda-from-numpy.py) and [`cuda-to-numpy.py`](https://github.com/dusty-nv/jetson-utils/blob/master/python/examples/cuda-to-numpy.py)

These examples will automatically be compiled while [Building the Project from Source](docs/building-repo-2.md), and are able to run the pre-trained models listed below in addition to custom models provided by the user.  Launch each example with `--help` for usage info.

## Pre-Trained Models

The project comes with a number of pre-trained models that are available through the [**Model Downloader**](docs/building-repo-2.md#downloading-models) tool:

#### Image Recognition

| Network       | CLI argument   | NetworkType enum |
| --------------|----------------|------------------|
| AlexNet       | `alexnet`      | `ALEXNET`        |
| GoogleNet     | `googlenet`    | `GOOGLENET`      |
| GoogleNet-12  | `googlenet-12` | `GOOGLENET_12`   |
| ResNet-18     | `resnet-18`    | `RESNET_18`      |
| ResNet-50     | `resnet-50`    | `RESNET_50`      |
| ResNet-101    | `resnet-101`   | `RESNET_101`     |
| ResNet-152    | `resnet-152`   | `RESNET_152`     |
| VGG-16        | `vgg-16`       | `VGG-16`         |
| VGG-19        | `vgg-19`       | `VGG-19`         |
| Inception-v4  | `inception-v4` | `INCEPTION_V4`   |

#### Object Detection

| Network                 | CLI argument       | NetworkType enum   | Object classes       |
| ------------------------|--------------------|--------------------|----------------------|
| SSD-Mobilenet-v1        | `ssd-mobilenet-v1` | `SSD_MOBILENET_V1` | 91 ([COCO classes](data/networks/ssd_coco_labels.txt)) |
| SSD-Mobilenet-v2        | `ssd-mobilenet-v2` | `SSD_MOBILENET_V2` | 91 ([COCO classes](data/networks/ssd_coco_labels.txt)) |
| SSD-Inception-v2        | `ssd-inception-v2` | `SSD_INCEPTION_V2` | 91 ([COCO classes](data/networks/ssd_coco_labels.txt)) |
| DetectNet-COCO-Dog      | `coco-dog`         | `COCO_DOG`         | dogs                 |
| DetectNet-COCO-Bottle   | `coco-bottle`      | `COCO_BOTTLE`      | bottles              |
| DetectNet-COCO-Chair    | `coco-chair`       | `COCO_CHAIR`       | chairs               |
| DetectNet-COCO-Airplane | `coco-airplane`    | `COCO_AIRPLANE`    | airplanes            |
| ped-100                 | `pednet`           | `PEDNET`           | pedestrians          |
| multiped-500            | `multiped`         | `PEDNET_MULTI`     | pedestrians, luggage |
| facenet-120             | `facenet`          | `FACENET`          | faces                |

#### Semantic Segmentation

| Dataset      | Resolution | CLI Argument | Accuracy | Jetson Nano | Jetson Xavier |
|:------------:|:----------:|--------------|:--------:|:-----------:|:-------------:|
| [Cityscapes](https://www.cityscapes-dataset.com/) | 512x256 | `fcn-resnet18-cityscapes-512x256` | 83.3% | 48 FPS | 480 FPS |
| [Cityscapes](https://www.cityscapes-dataset.com/) | 1024x512 | `fcn-resnet18-cityscapes-1024x512` | 87.3% | 12 FPS | 175 FPS |
| [Cityscapes](https://www.cityscapes-dataset.com/) | 2048x1024 | `fcn-resnet18-cityscapes-2048x1024` | 89.6% | 3 FPS | 47 FPS |
| [DeepScene](http://deepscene.cs.uni-freiburg.de/) | 576x320 | `fcn-resnet18-deepscene-576x320` | 96.4% | 26 FPS | 360 FPS |
| [DeepScene](http://deepscene.cs.uni-freiburg.de/) | 864x480 | `fcn-resnet18-deepscene-864x480` | 96.9% | 14 FPS | 190 FPS |
| [Multi-Human](https://lv-mhp.github.io/) | 512x320 | `fcn-resnet18-mhp-512x320` | 86.5% | 34 FPS | 370 FPS |
| [Multi-Human](https://lv-mhp.github.io/) | 640x360 | `fcn-resnet18-mhp-512x320` | 87.1% | 23 FPS | 325 FPS |
| [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/) | 320x320 | `fcn-resnet18-voc-320x320` | 85.9% | 45 FPS | 508 FPS |
| [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/) | 512x320 | `fcn-resnet18-voc-512x320` | 88.5% | 34 FPS | 375 FPS |
| [SUN RGB-D](http://rgbd.cs.princeton.edu/) | 512x400 | `fcn-resnet18-sun-512x400` | 64.3% | 28 FPS | 340 FPS |
| [SUN RGB-D](http://rgbd.cs.princeton.edu/) | 640x512 | `fcn-resnet18-sun-640x512` | 65.1% | 17 FPS | 224 FPS |

* If the resolution is omitted from the CLI argument, the lowest resolution model is loaded
* Accuracy indicates the pixel classification accuracy across the model's validation dataset
* Performance is measured for GPU FP16 mode with JetPack 4.2.1, `nvpmodel 0` (MAX-N)

<details>
<summary>Legacy Segmentation Models</summary>

| Network                 | CLI Argument                    | NetworkType enum                | Classes |
| ------------------------|---------------------------------|---------------------------------|---------|
| Cityscapes (2048x2048)  | `fcn-alexnet-cityscapes-hd`     | `FCN_ALEXNET_CITYSCAPES_HD`     |    21   |
| Cityscapes (1024x1024)  | `fcn-alexnet-cityscapes-sd`     | `FCN_ALEXNET_CITYSCAPES_SD`     |    21   |
| Pascal VOC (500x356)    | `fcn-alexnet-pascal-voc`        | `FCN_ALEXNET_PASCAL_VOC`        |    21   |
| Synthia (CVPR16)        | `fcn-alexnet-synthia-cvpr`      | `FCN_ALEXNET_SYNTHIA_CVPR`      |    14   |
| Synthia (Summer-HD)     | `fcn-alexnet-synthia-summer-hd` | `FCN_ALEXNET_SYNTHIA_SUMMER_HD` |    14   |
| Synthia (Summer-SD)     | `fcn-alexnet-synthia-summer-sd` | `FCN_ALEXNET_SYNTHIA_SUMMER_SD` |    14   |
| Aerial-FPV (1280x720)   | `fcn-alexnet-aerial-fpv-720p`   | `FCN_ALEXNET_AERIAL_FPV_720p`   |     2   |

</details>

## Recommended System Requirements

**Training GPU:**  Maxwell, Pascal, Volta, or Turing-based GPU (ideally with at least 6GB video memory)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;optionally, AWS P2/P3 instance or Microsoft Azure N-series  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ubuntu 16.04/18.04 x86_64

**Deployment:**    &nbsp;&nbsp;Jetson Nano Developer Kit with JetPack 4.2 or newer (Ubuntu 18.04 aarch64).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jetson Xavier Developer Kit with JetPack 4.0 or newer (Ubuntu 18.04 aarch64)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jetson TX2 Developer Kit with JetPack 3.0 or newer (Ubuntu 16.04 aarch64).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jetson TX1 Developer Kit with JetPack 2.3 or newer (Ubuntu 16.04 aarch64).

Note that TensorRT samples from the repo are intended for deployment onboard Jetson, however when cuDNN and TensorRT have been installed on the host side, the TensorRT samples in the repo can be compiled for PC.


## Extra Resources

In this area, links and resources for deep learning are listed:

* [ros_deep_learning](http://www.github.com/dusty-nv/ros_deep_learning) - TensorRT inference ROS nodes
* [NVIDIA AI IoT](https://github.com/NVIDIA-AI-IOT) - NVIDIA Jetson GitHub repositories
* [Jetson eLinux Wiki](https://www.eLinux.org/Jetson) - Jetson eLinux Wiki

## Legacy Links

<details open>
<summary>Since the documentation has been re-organized, below are links mapping the previous content to the new locations.</summary>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(click on the arrow above to hide this section)

### DIGITS Workflow

See [DIGITS Workflow](docs/digits-workflow.md)

### System Setup

See [DIGITS Setup](docs/digits-setup.md)

#### Running JetPack on the Host

See [JetPack Setup](docs/jetpack-setup.md)

#### Installing Ubuntu on the Host

See [DIGITS Setup](docs/digits-setup.md#installing-ubuntu-on-the-host)

#### Setting up host training PC with NGC container	

See [DIGITS Setup](docs/digits-setup.md#setting-up-host-training-pc-with-ngc-container)

#### Installing the NVIDIA driver

See [DIGITS Setup](docs/digits-setup.md#installing-the-nvidia-driver)

#### Installing Docker

See [DIGITS Setup](docs/digits-setup.md#installing-docker)

#### NGC Sign-up 

See [DIGITS Setup](docs/digits-setup.md#ngc-sign-up)

#### Setting up data and job directories

See [DIGITS Setup](docs/digits-setup.md#setting-up-data-and-job-directories)

#### Starting DIGITS container

See [DIGITS Setup](docs/digits-setup.md#starting-digits-container)

#### Natively setting up DIGITS on the Host 

See [DIGITS Native Setup](docs/digits-native.md)

#### Installing NVIDIA Driver on the Host

See [DIGITS Native Setup](docs/digits-native.md#installing-nvidia-driver-on-the-host)

#### Installing cuDNN on the Host

See [DIGITS Native Setup](docs/digits-native.md#installing-cudnn-on-the-host)

#### Installing NVcaffe on the Host

See [DIGITS Native Setup](docs/digits-native.md#installing-nvcaffe-on-the-host)

#### Installing DIGITS on the Host

See [DIGITS Native Setup](docs/digits-native.md#installing-digits-on-the-host)

#### Starting the DIGITS Server

See [DIGITS Native Setup](docs/digits-native.md#starting-the-digits-server)

### Building from Source on Jetson

See [Building the Repo from Source](docs/building-repo.md)
      
#### Cloning the Repo

See [Building the Repo from Source](docs/building-repo.md#cloning-the-repo)

#### Configuring with CMake

See [Building the Repo from Source](docs/building-repo.md#configuring-with-cmake)

#### Compiling the Project

See [Building the Repo from Source](docs/building-repo.md#compiling-the-project)

#### Digging Into the Code

See [Building the Repo from Source](docs/building-repo.md#digging-into-the-code)

### Classifying Images with ImageNet

See [Classifying Images with ImageNet](docs/imagenet-console.md)

#### Using the Console Program on Jetson

See [Classifying Images with ImageNet](docs/imagenet-console.md#using-the-console-program-on-jetson)

### Running the Live Camera Recognition Demo

See [Running the Live Camera Recognition Demo](docs/imagenet-camera.md)

### Re-training the Network with DIGITS

See [Re-Training the Recognition Network](docs/imagenet-training.md)

#### Downloading Image Recognition Dataset

See [Re-Training the Recognition Network](docs/imagenet-training.md#downloading-image-recognition-dataset)

#### Customizing the Object Classes

See [Re-Training the Recognition Network](docs/imagenet-training.md#customizing-the-object-classes)

#### Importing Classification Dataset into DIGITS

See [Re-Training the Recognition Network](docs/imagenet-training.md#importing-classification-dataset-into-digits)

#### Creating Image Classification Model with DIGITS

See [Re-Training the Recognition Network](docs/imagenet-training.md#creating-image-classification-model-with-digits)

#### Testing Classification Model in DIGITS

See [Re-Training the Recognition Network](docs/imagenet-training.md#testing-classification-model-in-digits)

#### Downloading Model Snapshot to Jetson

See [Downloading Model Snapshots to Jetson](docs/imagenet-snapshot.md)

### Loading Custom Models on Jetson

See [Loading Custom Models on Jetson](docs/imagenet-custom.md)

### Locating Object Coordinates using DetectNet

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md)

#### Detection Data Formatting in DIGITS

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md#detection-data-formatting-in-digits)

#### Downloading the Detection Dataset

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md#downloading-the-detection-dataset)

#### Importing the Detection Dataset into DIGITS

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md#importing-the-detection-dataset-into-digits)

#### Creating DetectNet Model with DIGITS

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md#creating-detectnet-model-with-digits)

#### Selecting DetectNet Batch Size

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md#selecting-detectnet-batch-size)

#### Specifying the DetectNet Prototxt 

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md#specifying-the-detectnet-prototxt)

#### Training the Model with Pretrained Googlenet

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md#training-the-model-with-pretrained-googlenet)

#### Testing DetectNet Model Inference in DIGITS

See [Locating Object Coordinates using DetectNet](docs/detectnet-training.md#testing-detectnet-model-inference-in-digits)

#### Downloading the Model Snapshot to Jetson

See [Downloading the Detection Model to Jetson](docs/detectnet-snapshot.md)

#### DetectNet Patches for TensorRT

See [Downloading the Detection Model to Jetson](docs/detectnet-snapshot.md#detectnet-patches-for-tensorrt)

### Processing Images from the Command Line on Jetson

See [Detecting Objects from the Command Line](docs/detectnet-console.md)

#### Launching With a Pretrained Model

See [Detecting Objects from the Command Line](docs/detectnet-console.md#launching-with-a-pretrained-model)

#### Pretrained DetectNet Models Available

See [Detecting Objects from the Command Line](docs/detectnet-console.md#pretrained-detectnet-models-available)

#### Running Other MS-COCO Models on Jetson

See [Detecting Objects from the Command Line](docs/detectnet-console.md#running-other-ms-coco-models-on-jetson)

#### Running Pedestrian Models on Jetson

See [Detecting Objects from the Command Line](docs/detectnet-console.md#running-pedestrian-models-on-jetson)

#### Multi-class Object Detection Models

See [Detecting Objects from the Command Line](docs/detectnet-console.md#multi-class-object-detection-models)

### Running the Live Camera Detection Demo on Jetson

See [Running the Live Camera Detection Demo](docs/detectnet-camera.md)

### Image Segmentation with SegNet

See [Semantic Segmentation with SegNet](docs/segnet-dataset.md)

#### Downloading Aerial Drone Dataset

See [Semantic Segmentation with SegNet](docs/segnet-dataset.md#downloading-aerial-drone-dataset)

#### Importing the Aerial Dataset into DIGITS

See [Semantic Segmentation with SegNet](docs/segnet-dataset.md#importing-the-aerial-dataset-into-digits)

#### Generating Pretrained FCN-Alexnet

See [Generating Pretrained FCN-Alexnet](docs/segnet-pretrained.md)

### Training FCN-Alexnet with DIGITS

See [Training FCN-Alexnet with DIGITS](docs/segnet-training.md)

#### Testing Inference Model in DIGITS

See [Training FCN-Alexnet with DIGITS](docs/segnet-training.md#testing-inference-model-in-digits)

#### FCN-Alexnet Patches for TensorRT

See [FCN-Alexnet Patches for TensorRT](docs/segnet-patches.md)

### Running Segmentation Models on Jetson

See [Running Segmentation Models on Jetson](docs/segnet-console.md)

</details>

##
<p align="center"><sup>© 2016-2019 NVIDIA | </sup><a href="#deploying-deep-learning"><sup>Table of Contents</sup></a></p>

