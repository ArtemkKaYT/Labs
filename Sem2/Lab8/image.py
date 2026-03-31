import cv2


IMAGE = 'variant-8.jpg'
SIZE = 400


def crop_image():
    image = cv2.imread(IMAGE)
    height, width = image.shape[:2]

    center_x = width // 2
    center_y = height // 2
    half_size = SIZE // 2

    x1 = center_x - half_size
    x2 = center_x + half_size
    y1 = center_y - half_size
    y2 = center_y + half_size

    cropped_image = image[y1:y2, x1:x2]

    return cropped_image


if __name__ == '__main__':
    cropped_image = crop_image()
    cv2.imwrite('variant-8_cropped.jpg', cropped_image)
    cv2.imshow('Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
