import numpy as np

def ImageHistogram(img_in):
    img_out = np.ones((600, 600), np.uint8) * 255
    grey_color = 125
    # x-axis draw
    img_out[560, 35:555] = grey_color
    # y-axis draw
    img_out[15:565, 40] = grey_color
    # 255 tap
    img_out[560:565, 552] = grey_color
    # draw values
    cv2.putText(img_out, '0', (35, 585), cv2.FONT_HERSHEY_SIMPLEX, 0.5, grey_color, 2)
    cv2.putText(img_out, '255', (530, 585), cv2.FONT_HERSHEY_SIMPLEX, 0.5, grey_color, 2)

    hist = cv2.calcHist([img_in], [0], None, [256], [0, 256])
    hist = hist / np.amax(hist) * 550
    hist = hist.astype(int)
    i = 0
    for val in hist:
        img_out[(565 - val[0]):560, i + 41:i + 43] = grey_color
        i += 2
    return img_out