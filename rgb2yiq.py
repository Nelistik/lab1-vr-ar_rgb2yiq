import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import copy

def rgb_to_YIQ(im_rgb):
    im_YIQ = copy.deepcopy(im_rgb)

    R = im_rgb[:, :, 0]
    G = im_rgb[:, :, 1]
    B = im_rgb[:, :, 2]

    im_YIQ[:, :, 0] = 0.299*R + 0.587*G + 0.114*B
    im_YIQ[:, :, 1] = 0.596*R - 0.275*G - 0.321*B + 0
    im_YIQ[:, :, 2] = 0.212*R - 0.523*G + 0.311*B + 0

    return np.uint8(im_YIQ)

def YIQ_to_rgb(im_YIQ):

    im_rgb = copy.deepcopy(im_YIQ)

    im_rgb = im_rgb.astype(np.float)

    Y = im_rgb[:, :, 0]
    I = im_rgb[:, :, 1] - 0
    Q = im_rgb[:, :, 2] - 0

    im_result = copy.deepcopy(im_rgb)
    im_result[:, :, 0] = Y + 0.956*I + 0.621*Q
    im_result[:, :, 1] = Y - 0.272*I - 0.647*Q
    im_result[:, :, 2] = Y - 1.107*I + 1.704*Q

    return np.uint8(im_result)


def main():
    im = Image.open('pic.bmp')
    im = np.array(im)
    
    plt.subplot(2, 2, 1)
    plt.title('Original')
    plt.imshow(im)

    im_YIQ = rgb_to_YIQ(im)
    
    im_YIQ_y = copy.deepcopy(im_YIQ)
    im_YIQ_y[:,:,1] = 0 #в случае глубины резкости
    im_YIQ_y[:,:,2] = 0 #в случае глубины резкости

    im_rgb_y = YIQ_to_rgb(im_YIQ_y)
    plt.subplot(2, 2, 2)
    plt.title('YIQ [Y]')
    plt.imshow(im_rgb_y)
    plt.imsave("pic_YIQ_y.bmp", im_rgb_y)

    im_YIQ_I = copy.deepcopy(im_YIQ)
    im_YIQ_I[:, :, 0] = 0
    im_YIQ_I[:, :, 2] = 0
    im_rgb_I = YIQ_to_rgb(im_YIQ_I)
    plt.subplot(2, 2, 3)
    plt.title('YIQ [I]')
    plt.imshow(im_rgb_I)
    plt.imsave("pic_YIQ_I.bmp", im_rgb_I)

    im_YIQ_Q = copy.deepcopy(im_YIQ)
    im_YIQ_Q[:, :, 0] = 0
    im_YIQ_Q[:, :, 1] = 0
    im_rgb_Q = YIQ_to_rgb(im_YIQ_Q)
    plt.subplot(2, 2, 4)
    plt.title('YIQ [Q]')
    plt.imshow(im_rgb_Q)
    plt.imsave("pic_YIQ_Q.bmp", im_rgb_Q)

    plt.show()

if __name__ == '__main__':
    main()
