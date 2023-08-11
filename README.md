# Affine, projective, fisheye and horizontal wave image Transformations using OpenCV

Please star ⭐ this repo if you found it useful!

| ![affine-example.png](readme%20files/affine-example.png) | 
|:--------------------------------------------------------:| 
|                          Affine transformation                           |

| ![perspective-example.png](readme%20files/perspective-example.png) | 
|:------------------------------------------------------------------:| 
|                     Perspective transformation                     |


| ![fisheye-and-horizontal-wave-example.png](readme%20files/fisheye-and-horizontal-wave-example.png) | 
|:--------------------------------------------------------------------------------------------------:| 
|                            Fisheye and Horizontal wave transformations                             |

This repository contains Python scripts that demonstrate how to perform multiple different image transformations using the OpenCV library. These image transformations are common techniques in computer vision and image processing for tasks like image registration, perspective correction, and more.

## Table of Contents

- [Introduction](#introduction)
- [Available image transformation types](#available-image-transformation-types)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Introduction

This script showcases the usage of OpenCV to apply multiple image transformations to images. Affine transformations preserve lines and parallelism, while projective transformations (also known as perspective transformations) can map any quadrilateral to any other quadrilateral.

Affine and projective transformations are defined using transformation matrices, and OpenCV provides convenient functions to apply these transformations to images.

The scripts include testing using the resulting transformation matrix and a coordinate of a feature to get the coordinate of the same feature in the transformed image.

## Available image transformation types
- Affine
- Perspective
- Fisheye
- Horizontal wave

## Prerequisites

Before using the script, make sure you have the following dependencies installed:

- Python (>=3.x). I personally used Python 3.10.12
- OpenCV (cv2) library. I personally used OpenCV 4.8.0
- PyTorch (v.1.13.1)

You can install the OpenCV library using pip:

```
pip install opencv-python
```

## Installation
Clone this repository to your local machine:

```
git clone https://github.com/dmartinvega/warping-images.git
```

Navigate to the repository's directory:

```
cd warping-images
```

## Usage

Modify and use the provided script to experiment with affine and projective transformations. The script takes an input image, applies specified transformation matrices, and shows the transformed images.

There is a default example image in `images/`. You can use any other image you desire. You just have to define the location and name of your file in `utils.load_image()`, `image` variable.

To run the script:

    python affine.py

or 

    python perspective.py

The resulting image and matrix will be saved into `results/` folder.

We defined parameters to make the warping. You can adjust those transformation values to suit your needs in the variable `pts2` in `affine.affine_transformation()` and `perspective.perspective_transformation()`.

To test fisheye and horizontal wave transformations, use `test.fisheye_and_horizontal_wave_test()` function.

## Use cases

Here are a few examples of how you can use these scripts:

- Applying an affine transformation to straighten a rotated image.
- Correcting the perspective of an image containing a skewed object.
- Creating a collage of images by applying projective transformations.

Feel free to explore and adapt the script for your specific use cases.

# Issues and requests

Questions and issues can be left as issues in the repository. If you make any improvements/changes, feel free to create pull requests and I will check and approve them as well.


## License

This project is licensed under the MIT License, which means you are free to use, modify, and distribute the code in your projects.

Happy transforming! If you have any questions or suggestions, feel free to contact dmartinvega@gmail.com.

## Acknowledgements
For fisheye and horizontal wave transformations I acknowledge the contributions of Nilesh Vijayrania in his Towards Data Science post: [Non-Linear Augmentations For Deep Learning](https://towardsdatascience.com/non-linear-augmentations-for-deep-leaning-4ba99baaaaca) (Accessed on August 11th, 2023)