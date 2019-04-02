from __future__ import print_function
import matplotlib, sys
from matplotlib import pyplot as plt
import numpy as np
import random

def plot(matrix, weights=None, title="Prediction Matrix"):
    if len(matrix[0]) == 4:
        fig, ax = plt.subplots()
        ax.set_title(title)
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        if weights != None:
            map_min = 0.0
            map_max = 1.1
            y_res = 0.001
            x_res = 0.001
            ys = np.arange(map_min, map_max, y_res)
            xs = np.arange(map_min, map_max, x_res)
            zs = []
            for cur_y in np.arange(map_min, map_max, y_res):
                for cur_x in np.arange(map_min, map_max, x_res):
                    zs.append(predict([1.0, cur_x, cur_y], weights))
            xs, ys = np.meshgrid(xs, ys)
            zs = np.array(zs)
            zs = zs.reshape(xs.shape)
            cp = plt.contourf(xs, ys, zs, levels=[-1, -0.0001, 0, 1], colors=('b', 'r'), alpha=0.1)

        c1_data = [[], []]
        c0_data = [[], []]
        for i in range(len(matrix)):
            cur_i1 = matrix[i][1] #x
            cur_i2 = matrix[i][2] #y
            cur_y = matrix[i][-1] #t
            if cur_y == 1:
                c1_data[0].append(cur_i1)
                c1_data[1].append(cur_i2)
            else:
                c0_data[0].append(cur_i1)
                c0_data[1].append(cur_i2)

        plt.xticks(np.arange(0.0, 1.1, 0.1))
        plt.yticks(np.arange(0.0, 1.1, 0.1))
        plt.xlim(0, 1.05)
        plt.ylim(0, 1.05)

        c0s = plt.scatter(c0_data[0], c0_data[1], s=40.0, c='r', label='0')
        c1s = plt.scatter(c1_data[0], c1_data[1], s=40.0, c='b', label='1')

        plt.legend(fontsize=10, loc=1)
        plt.show()
        return

    print("Matrix dimensions not covered.")


# each matrix row: up to last row = inputs, last row = y (classification)
def accuracy(matrix, weights):
    num_correct = 0.0
    preds = []
    for i in range(len(matrix)):
        pred = predict(matrix[i][:-1], weights)  # get predicted classification
        preds.append(pred)
        if pred == matrix[i][-1]: num_correct += 1.0
    print("Predictions:", preds)
    return num_correct / float(len(matrix))

#okreslanie outputu czyli Yi
def predict(inputs, weights):
    activation = 0.0
    for i, w in zip(inputs, weights): #x*w
        activation += i * w #x1 *w1, x2*w2, ...
    return 1.0 if activation > 0.0 else 0.0

# each matrix row: up to last row = inputs, last row = y (classification)
def train_weights(matrix, weights, nb_epoch=10, l_rate=1.00, do_plot=False, stop_early=True, verbose=True):
    for epoch in range(nb_epoch):
        cur_acc = accuracy(matrix, weights)
        print("\nEpoch %d \nWeights: " % epoch, weights)
        print("Accuracy: ", cur_acc)

        if cur_acc == 1.0 and stop_early: break

        for i in range(len(matrix)):
            prediction = predict(matrix[i][:-1], weights)
            error = matrix[i][-1] - prediction  # get error
            if verbose: sys.stdout.write("Training on data at index %d...\n" % (i))
            for j in range(len(weights)):  # calculate new weight for each node
                if verbose: sys.stdout.write("\tWeight[%d]: %0.5f --> " % (j, weights[j]))
                weights[j] = weights[j] + (l_rate * error * matrix[i][j])
                if verbose: sys.stdout.write("%0.5f\n" % (weights[j]))

    plot(matrix, weights, title="Final Epoch")
    return weights

def main():
    nb_epoch = 1000  # number of repetitions
    l_rate = 1.0  # learning rate
    plot_each_epoch = False
    stop_early = True

    b = random.random()
    print("b="+str(b))
    w1 = random.random()
    w2= random.random()
    w3 = random.random()

           #   B     x 	 y 	  t
    matrix = [[b, 0.08, 0.72, 1.0],
              [b, 0.10, 1.00, 1.0],
              [b, 0.26, 0.58, 1.0],
              [b, 0.35, 0.95, 1.0],
              [b, 0.45, 0.15, 0.0],
              [b, 0.60, 0.30, 0.0],
              [b, 0.70, 0.65, 0.0],
              [b, 0.92, 0.45, 0.0]]
    weights = [w1, w2, w3]  # initial weights specified in problem

    train_weights(matrix, weights=weights, nb_epoch=nb_epoch, l_rate=l_rate, do_plot=plot_each_epoch,
                  stop_early=stop_early)


if __name__ == '__main__':
    main()

# https://www.youtube.com/watch?v=OVHc-7GYRo4&feature=youtu.be&fbclid=IwAR2AMccOpjErDMtRf1JPgOZLXjzaokxj2VrbHKImmFANPr9O6wwbciOre_A
