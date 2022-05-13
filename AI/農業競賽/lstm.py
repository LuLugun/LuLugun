import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import LSTM


df1 = pd.read_csv('test_images.csv')
df2 = pd.read_csv('test_labels.csv')
data_images=df1.values
data_labels=df2.values
#print("data_images.shape:",data_images.shape)
#print("data_labels.shape:",data_labels.shape)

data_images = data_images.reshape(22796,1,18)



model = Sequential() 
model.add(LSTM(units = 256, input_shape=(1,18), activation='sigmoid',return_sequences=True))
model.add(layers.Dropout(0.2))
model.add(LSTM(units = 256, activation='sigmoid',return_sequences=True))
model.add(layers.Dropout(0.2))
model.add(LSTM(units = 256, activation='sigmoid',return_sequences=True))
model.add(layers.Dropout(0.2))
model.add(LSTM(units = 256, activation='sigmoid',return_sequences=True))
model.add(layers.Dropout(0.2))
model.add(LSTM(units = 256, activation='sigmoid'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(units = 11, activation='sigmoid'))

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
cf1 = cf1.reshape(5695,1,18)
test_loss,test_acc = model.evaluate(cf1,cf2)
print(test_acc)


p1 = pd.read_csv('submission.csv')
p1 = p1.values
p1 = p1.reshape(12457,1,18)
predict = model.predict(p1)
#print(predict)
pd.DataFrame(predict).to_csv("file.csv")




