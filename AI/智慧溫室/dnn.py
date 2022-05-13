import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from keras.layers.core import Dense, Activation ,Dropout
pd.set_option('display.float_format', lambda x: '%.0f' % x)
traini_sensor = pd.read_csv('train_sensor.csv')
trainl_action = pd.read_csv('train_action.csv')

traini = traini_sensor.values
trainl = trainl_action.values

model = Sequential()
model.add(Dense(2048, input_dim=8))
model.add(Activation('sigmoid'))
model.add(Dropout(0.3))
model.add(Dense(1024))
model.add(Activation('sigmoid'))
model.add(Dropout(0.3))
model.add(Dense(512))
model.add(Activation('sigmoid'))
model.add(Dropout(0.3))
model.add(Dense(4))
model.add(Activation('sigmoid'))

model.compile(loss='MSE', optimizer='adam', metrics=['accuracy'])

train_history = model.fit(traini,  
                          trainl,validation_split = 0.1,
                          epochs=30, batch_size=144)

cf1 = pd.read_csv('test_sensor.csv')
cf2 = pd.read_csv('test_action.csv')
cf1=cf1.values
cf2=cf2.values

test_loss,test_acc = model.evaluate(cf1,cf2)
print(test_acc)

result_batch = model.predict(cf1)

print(result_batch)

result_batch = pd.DataFrame(result_batch)
result_batch = result_batch.round(0).astype(int)
result_batch.to_csv("file_dnn.csv")


