import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import LSTM
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from f1_score import *

traini = pd.read_csv('test_images.csv')
trainl = pd.read_csv('test_labels.csv')

traini = traini.values
trainl = trainl.values

#traini = traini.reshape(22796,18)

def convert_to_integer(data):
    rowNum=data.shape[0]
    featureNum=data.shape[1]
    newdata= np.arange(rowNum)
 
    for i in range(rowNum):    # 0,1,2,3,4...n-1
        result=0
        movingbit= 1<< (featureNum-1) 
        
        for j in range(featureNum):  
            if data[i][j] ==1: 
                result= result + movingbit
            movingbit= movingbit >> 1           
        newdata[i]=result 
        
    return newdata

#trainl = convert_to_integer(trainl)
#trainl= to_categorical(trainl)
#traini= to_categorical(traini)

data_gen = TimeseriesGenerator(traini,trainl,length = 1,batch_size=1)

model2 = Sequential()
model2.add(layers.SimpleRNN(512,
                            stateful= True,
                            batch_input_shape=(1,None,18)))
#model2.add(layers.SimpleRNN(512,
#                           input_shape=(18,65501)))
model2.add(layers.Dense(256, activation='sigmoid'))
model2.add(layers.Dense(128, activation='sigmoid'))
model2.add(layers.Dense(64, activation='sigmoid'))
model2.add(layers.Dense(11, activation='sigmoid'))
model2.summary()

model2.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['acc'])

#history = model2.fit(
#                    traini,
#                    trainl,
#                    epochs=50)

epochs = 50
for i in range(epochs):
    print('Epochs',i+1,'/',epochs)
    model2.fit_generator(data_gen,epochs = 1,shuffle=False)
    model2.reset_states()

cf1 = pd.read_csv('train_images-1.csv')
cf2 = pd.read_csv('train_labels-1.csv')
cf1=cf1.values
cf2=cf2.values
cf1 = cf1.reshape(5695,1,18)
test_loss,test_acc = model2.evaluate(cf1,cf2)
print(test_acc)

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