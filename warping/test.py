import numpy as np
import torch
from PIL import Image
from torch.nn import functional as F

from fisheye import get_fisheye
from horizontal_wave import get_horizontal_wave
from utils import plot_two_images, draw_feature_in_image, get_image_batch, plot
import cv2


def affine_test(M, image_original, image_transformed, feature_image_original):
    feature_image_transformed = get_feature_coordinates_in_transformed_image(M, feature_image_original)

    image_original_with_feature = draw_feature_in_image(feature_image_original, image_original)
    image_transformed_with_feature = draw_feature_in_image(feature_image_transformed, image_transformed)

    plot_two_images(f'Original: {feature_image_original}', f'Transformed: {feature_image_transformed}',
                    image_original_with_feature, image_transformed_with_feature)


def get_feature_coordinates_in_transformed_image(M, feature_image_original):
    feature_image_transformed_list = np.dot(M, np.array([feature_image_original[0], feature_image_original[1], 1]))
    feature_image_transformed_tuple = tuple(int(value) for value in feature_image_transformed_list)
    return feature_image_transformed_tuple


def perspective_test(image_original, image_transformed, feature_image_original, homography_matrix):
    feature_image_original = np.array(feature_image_original, dtype=np.float32).reshape(-1, 1, 2)
    feature_image_transformed = cv2.perspectiveTransform(feature_image_original, homography_matrix)
    feature_image_transformed = (int(feature_image_transformed[0][0][0]), int(feature_image_transformed[0][0][1]))
    feature_image_original = (int(feature_image_original[0][0][0]), int(feature_image_original[0][0][1]))
    image_original_with_feature = draw_feature_in_image(feature_image_original, image_original)
    image_transformed_with_feature = draw_feature_in_image(feature_image_transformed, image_transformed)

    plot_two_images(f'Original: {feature_image_original}', f'Transformed: {feature_image_transformed}',
                    image_original_with_feature, image_transformed_with_feature)


def fisheye_and_horizontal_wave_test():
    # img = Image.open('checkerboard.png')
    # img = Image.open('images/grid-original.jpg')
    img = Image.open('../images/COCO_train2014_000000581906.jpg')
    imgs = get_image_batch(img)
    N, C, H, W = imgs.shape
    fisheye_grid = get_fisheye(H, W, torch.tensor([0, 0]), 0.4)
    hwave_grid = get_horizontal_wave(H, W, 10, 0.1)
    fisheye_output = F.grid_sample(imgs, fisheye_grid, align_corners=True)
    hwave_output = F.grid_sample(imgs, hwave_grid, align_corners=True)
    plot(img, fisheye_output, hwave_output)