class ClfMetrics:
    """
    This class calculates some of the metrics of classifier including accuracy, precision, recall, f1 according to confusion matrix.
    Args:
        y_true (ndarray): 1d-array for true target vector.
        y_pred (ndarray): 1d-array for predicted target vector.
    """
    def __init__(self, y_true, y_pred):
        self._y_true = y_true
        self._y_pred = y_pred
    def confusion_matrix(self):
        """
        This function returns the confusion matrix given true/predicted target vectors.
        """
        n_unique = np.unique(self._y_true).size
        cm = np.zeros((n_unique, n_unique), dtype=int)
        for i in range(n_unique):
            for j in range(n_unique):
                n_obs = np.sum(np.logical_and(self._y_true == i, self._y_pred == j))
                cm[i, j] = n_obs
        self._tn = cm[0, 0]
        self._tp = cm[1, 1]
        self._fn = cm[1, 0]
        self._fp = cm[0, 1]
        return cm
    def accuracy_score(self):
        """
        This function returns the accuracy score given true/predicted target vectors.
        """
        cm = self.confusion_matrix()
        accuracy = (self._tn + self._tp) / np.sum(cm)
        return accuracy
    def precision_score(self):
        """
        This function returns the precision score given true/predicted target vectors.
        """
        precision = self._tp / (self._tp + self._fp)
        return precision
    def recall_score(self):
        """
        This function returns the recall score given true/predicted target vectors.
        """
        recall = self._tp / (self._tp + self._fn)
        return recall
    def f1_score(self, beta=1):
        """
        This function returns the f1 score given true/predicted target vectors.
        Args:
            beta (int, float): Can be used to generalize from f1 score to f score.
        """
        precision = self.precision_score()
        recall = self.recall_score()
        f1 = (1 + beta**2)*precision*recall / ((beta**2 * precision) + recall)
        return f1


import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import LSTM
#from sklearn.metrics import f1_score
df1 = pd.read_csv('test_images.csv')
df2 = pd.read_csv('test_labels.csv')

data_images=df1.values
data_labels=df2.values
#print("data_images.shape:",data_images.shape)
#print("data_labels.shape:",data_labels.shape)

data_images = data_images.reshape(22796,18)

model = Sequential()
model.add(layers.Dense(512, activation='relu', input_dim=18))
model.add(layers.Dense(11, activation='sigmoid'))
model.summary()

model.compile(optimizer='adam',
              loss='mean_absolute_error',
              metrics=['acc'])

history = model.fit(
                    data_images,
                    data_labels,
                    epochs=100)

cf1 = pd.read_csv('train_images-1.csv')
cf2 = pd.read_csv('train_labels-1.csv')
cf1=cf1.values
cf2=cf2.values
cf1 = cf1.reshape(5695,18)
predict_score = model.predict(cf1)
#test_loss,test_acc = model.evaluate(cf1,cf2)
clf_metrics = ClfMetrics(cf2, predict_score)
clf_metrics.confusion_matrix()
print(clf_metrics.f1_score())
#print(test_acc)

p1 = pd.read_csv('submission.csv')
p1 = p1.values
p1 = p1.reshape(12457,18)
predict = model.predict(p1)
#print(predict)
pd.DataFrame(predict).to_csv("file.csv")
