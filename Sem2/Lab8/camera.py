import cv2
import numpy as np
import os


prev_center = None
fly_icon = None


def overlay_icon(frame, icon, center):
    if icon is None:
        return

    icon_h, icon_w = icon.shape[:2]
    x, y = center
    top = max(0, y - icon_h // 2)
    left = max(0, x - icon_w // 2)
    bottom = min(frame.shape[0], top + icon_h)
    right = min(frame.shape[1], left + icon_w)

    top = y - icon_h // 2
    left = x - icon_w // 2
    bottom = top + icon_h
    right = left + icon_w

    if top < 0 or left < 0 or bottom > frame.shape[0] or right > frame.shape[1]:
        return

    roi = frame[top:bottom, left:right]
    icon_roi = icon

    if icon_roi.shape[2] == 4:
        alpha = icon_roi[:, :, 3] / 255.0
        for c in range(3):
            roi[:, :, c] = (alpha * icon_roi[:, :, c] + (1 - alpha) *
                            roi[:, :, c]).astype(np.uint8)
    else:
        roi[:, :] = icon_roi


def find_mark(frame):
    global prev_center

    blurred = cv2.GaussianBlur(frame, (7, 7), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    lower_blue1 = np.array([80, 30, 30])
    upper_blue1 = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue1, upper_blue1)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    best_quad = None
    best_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 100:
            continue

        epsilon = 0.03 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h if h > 0 else 0

            if 0.6 < aspect_ratio < 1.5:
                if area > best_area:
                    best_area = area
                    best_quad = approx

    if best_quad is not None:
        x, y, w, h = cv2.boundingRect(best_quad)
        current_center = (x + w // 2, y + h // 2)

        prev_center = current_center

        cv2.drawContours(frame, [best_quad], -1, (255, 0, 0), 2)
        overlay_icon(frame, fly_icon, prev_center)
        cv2.line(frame, (prev_center[0], 0), (prev_center[0], frame.shape[0]),
                 (0, 255, 0), 2)
        cv2.line(frame, (0, prev_center[1]), (frame.shape[1], prev_center[1]),
                 (0, 255, 0), 2)
    else:
        prev_center = None


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    fly_icon = cv2.imread(r'C:\Users\korol\Labs\fly64.png',
                          cv2.IMREAD_UNCHANGED)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        find_mark(frame)

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
