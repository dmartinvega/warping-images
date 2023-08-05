import cv2
import numpy as np
import utils
import test


def perspective_transformation(img, rows, cols, points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    pts1 = np.float32(points)
    pts2 = np.float32([(x_coords[0]*0.9, y_coords[0]),
                       (x_coords[1]*0.8, y_coords[1]*0.75),
                       (x_coords[2]*0.8, y_coords[2]*0.9),
                       (x_coords[3], y_coords[3])])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    round_matrix = np.round(matrix, decimals=1)
    print(round_matrix)
    image_transformed = cv2.warpPerspective(img, matrix, (int(cols), int(rows)))
    return matrix, image_transformed


def main():
    image_original, rows, cols = utils.load_image()
    points = utils.define_points(rows, cols, "perspective")
    # utils.draw_points(image_original, points)
    homography_matrix, image_transformed = perspective_transformation(image_original, rows, cols, points)
    feature_image_original = (550, 277)
    test.perspective_test(image_original, image_transformed, feature_image_original, homography_matrix)
    cv2.imwrite("results/perspective-result.png", image_transformed)
    np.savetxt("results/homography_matrix.csv", homography_matrix, delimiter=",")


if __name__ == "__main__":
    main()
