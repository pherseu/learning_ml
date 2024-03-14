import csv
import numpy as np

data_list = list(csv.reader(open("./01/challenges/I/sonar_data/sonar.all-data")))
data_array = np.array(data_list)
data = np.insert(data_array, 0, 1, axis=1)

np.random.seed(1234)
np.random.shuffle(data)

X = data[:, 0:-1].astype(np.float32)

labels = data[:, -1].reshape(-1,1)
Y_unencoded = (labels == 'M').astype(int)

SIZE_OF_TRAINING_SET = 160

X_train, X_test = np.vsplit(X, [SIZE_OF_TRAINING_SET])
Y_train_unencoded, Y_test = np.vsplit(Y_unencoded, [SIZE_OF_TRAINING_SET])

def one_hot_encode(Y):
    n_labels = Y.shape[0]
    n_classes = 2
    encoded_Y = np.zeros((n_labels, n_classes))
    for i in range(n_labels):
        label = Y[i]
        encoded_Y[i][label] = 1
    return encoded_Y

Y_train = one_hot_encode(Y_train_unencoded)