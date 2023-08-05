import cv2
from matplotlib import pyplot as plt


def load_image():
    image = cv2.imread("images/COCO_train2014_000000581906.jpg")
    # image = cv2.imread("images/grid-original.jpg")
    rows, cols, ch = image.shape
    return image, rows, cols


def draw_points(image, points):
    radius = 5
    red = (0, 0, 255)
    thickness = -1

    image_with_points = image.copy()
    for point in points:
        cv2.circle(image_with_points, point, radius, red, thickness)


def define_points(cols, rows, transformation_type):
    percentage = 0.15
    point1 = (int(rows*percentage), int(cols*percentage))
    point2 = (int(rows*(1-percentage)), int(cols*percentage))
    point3 = (int(rows*percentage), int(cols*(1-percentage)))
    point4 = (int(rows*(1-percentage)), int(cols*(1-percentage)))

    if transformation_type == "affine":
        return point1, point2, point3
    elif transformation_type == "perspective":
        return point1, point2, point3, point4


def plot_two_images(title1, title2, image1, image2):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    show_subplot(image1, title1)

    plt.subplot(1, 2, 2)
    show_subplot(image2, title2)

    plt.show()


def show_subplot(image_original_with_feature, title):
    plt.imshow(cv2.cvtColor(image_original_with_feature, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.grid(visible=True)


def draw_feature_in_image(feature, image):
    radius = 5
    green = (0, 255, 0)
    thickness = -1
    image_with_feature = image.copy()
    cv2.circle(image_with_feature, feature[0:2], radius, green, thickness)
    return image_with_feature
