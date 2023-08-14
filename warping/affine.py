import cv2
import numpy as np
import utils
import test


def affine_transformation(img, rows, cols, points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    pts1 = np.float32(points)
    pts2 = np.float32([(x_coords[0] * 0.7, y_coords[0] * 0.6),
                       (x_coords[1] * 0.9, y_coords[1] * 1.1),
                       (x_coords[2] * 0.8, y_coords[2] * 0.9)])

    matrix = cv2.getAffineTransform(pts1, pts2)
    round_matrix = np.round(matrix, decimals=1)
    print(round_matrix)
    result = cv2.warpAffine(img, matrix, (int(cols), int(rows)))
    return matrix, result


def main():
    image_original, rows, cols = utils.load_image()
    points = utils.define_points(rows, cols, "affine")
    # utils.draw_points(image_original, points)
    matrix, image_transformed = affine_transformation(image_original, rows, cols, points)
    feature_image_original = (550, 277)
    test.affine_test(matrix, image_original, image_transformed, feature_image_original)
    cv2.imwrite("results/affine-result.png", image_transformed)
    np.savetxt("results/affine_matrix.csv", matrix, delimiter=",")


if __name__ == "__main__":
    main()
