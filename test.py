import numpy as np
from utils import plot_two_images, draw_feature_in_image
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
