import numpy as np
import cv2

def k_means():

    mean_list = [[0, 0, 0], [63, 63, 63], [127, 127, 127], [255, 255, 255]]

    width, length, height = img.shape

    img_lin = np.reshape(img, (width*length, height))

    seg_img = np.zeros((np.shape(img_lin)))

    iter = 0

    while (iter < 40):
        class1 = []
        class2 = []
        class3 = []
        class4 = []

        for i in range(np.shape(img_lin)[0]):

            new_means = mean_list.copy()

            dist = np.sum((np.square(np.subtract(new_means, img_lin[i]))), axis=1)

            index = np.argmin(dist)

            if index == 0:
                class1.append(img_lin[i])
            elif index == 1:
                class2.append(img_lin[i])
            elif index == 2:
                class3.append(img_lin[i])
            elif index == 3:
                class4.append(img_lin[i])

            seg_img[i] = new_means[index]

        class1 = np.asarray(class1)
        class2 = np.asarray(class2)
        class3 = np.asarray(class3)
        class4 = np.asarray(class4)

        centroid1 = [(np.mean(class1[:, 0])), (np.mean(class1[:, 1])), (np.mean(class1[:, 2]))]
        centroid2 = [(np.mean(class2[:, 0])), (np.mean(class2[:, 1])), (np.mean(class2[:, 2]))]
        centroid3 = [(np.mean(class3[:, 0])), (np.mean(class3[:, 1])), (np.mean(class3[:, 2]))]
        centroid4 = [(np.mean(class4[:, 0])), (np.mean(class4[:, 1])), (np.mean(class4[:, 2]))]

        mean_list = [centroid1, centroid2, centroid3, centroid4]
    
        iter += 1
        print('Iteration: ', iter)


    seg_img = np.uint8(np.reshape(seg_img, (width, length, height)))

    cv2.imshow('test', seg_img)
    cv2.waitKey(0)


if __name__ == "__main__":

    img = cv2.imread('../data/traffic_img.png')

    k_means(img)
