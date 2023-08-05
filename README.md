# Affine and Projective Transformations using OpenCV

| ![affine-example.png](readme%20files/affine-example.png) | 
|:--------------------------------------------------------:| 
|                          Affine transformation                           |

| ![perspective-example.png](readme%20files/perspective-example.png) | 
|:------------------------------------------------------------------:| 
|                     Perspective transformation                     |


This repository contains a Python script that demonstrates how to perform affine and projective transformations using the OpenCV library. Affine and projective transformations are common techniques in computer vision and image processing for tasks like image registration, perspective correction, and more.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Introduction

This script showcases the usage of OpenCV to apply affine and projective transformations to images. Affine transformations preserve lines and parallelism, while projective transformations (also known as perspective transformations) can map any quadrilateral to any other quadrilateral.

The transformations are defined using transformation matrices, and OpenCV provides convenient functions to apply these transformations to images.

The script includes testing using the resulting transformation matrix and a coordinate of a feature to get the coordinate of the same feature in the transformed image.

## Prerequisites

Before using the script, make sure you have the following dependencies installed:

- Python (>=3.x)
- OpenCV (cv2) library

You can install the OpenCV library using pip:

```
pip install opencv-python
```

## Installation
Clone this repository to your local machine:

```
git clone https://github.com/dmartinvega/affine-projective-transformations.git
```

Navigate to the repository's directory:

```
cd affine-projective-transformations
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

## Use cases

Here are a few examples of how you can use this script:

- Applying an affine transformation to straighten a rotated image.
- Correcting the perspective of an image containing a skewed object.
- Creating a collage of images by applying projective transformations.

Feel free to explore and adapt the script for your specific use cases.

## License

This project is licensed under the MIT License, which means you are free to use, modify, and distribute the code in your projects.

Happy transforming! If you have any questions or suggestions, feel free to contact dmartinvega@gmail.com.
