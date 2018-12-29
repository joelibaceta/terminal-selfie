import os

import cv2
import image_processor


def capture_selfie():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    print_selfie(frame)
    cam.release()

def print_selfie(frame):
    rows, cols = os.popen('stty size', 'r').read().split()
    print(rows, cols)
    resized_frame = resize_frame(frame, (cols, rows))
    h, w, _ = resized_frame.shape
    printing_width = int(min(int(cols), (w * 2)) / 2)
    string = ""
    for j in range(h):
        for i in range(printing_width):
            pixel = resized_frame[j][i]
            char = image_processor.pixel_to_ascii(pixel)
            string += char
        string += "\n"
    print(string)

def resize_frame(frame, dimensions):
    """
    Resize a frame to meet the terminal dimensions

    Calculating the output terminal dimensions (cols, rows),
    we can to get a reduction factor to resize the frame
    according to the height of the terminal mainly
    to print each frame at a time, using all the available rows

    Args:
        frame: Frame to resize
        dimensions: If you want to set a printer area size (cols, rows)
    Returns:
        A resized frame
    """
    height, width, _ = frame.shape
    _, rows = dimensions
    reduction_factor = (float(rows)) / height * 100
    reduced_width = int(width * reduction_factor / 100)
    reduced_height = int(height * reduction_factor / 100)
    dimension = (reduced_width, reduced_height)
    resized_frame = cv2.resize(frame, dimension, interpolation=cv2.INTER_LINEAR)
    return resized_frame


if __name__ == '__main__':
    capture_selfie()