import pandas as pd 
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.utils import to_categorical
import tensorflow as tf
df1 = pd.read_csv('train_sensor.csv')
df2 = pd.read_csv('train_action.csv')

cf1 = pd.read_csv('test_sensor.csv')
cf2 = pd.read_csv('test_action.csv')

#p1 = pd.read_csv('submission.csv')

df1=df1.values
df2=df2.values
cf1 = cf1.values
cf2 = cf2.values
#p1 = p1.values

model = Sequential()
model.add(Dense(1024, activation='relu', input_dim=7))
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(4, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['acc'])


test = model.fit(df1,df2,epochs = 10,batch_size = 288)
test_loss,test_acc = model.evaluate(cf1,cf2)
print('model:',test_acc)

#result_batch = model.predict(p1)
model.save('keras_model.h5')
reload_model = tf.keras.models.load_model('keras_model.h5')
reload_model.summary()
#reload_result_batch = reload_model.predict(p1)
test_loss,test_acc = reload_model.evaluate(cf1,cf2)
print('reload_model:',test_acc)
#print((abs(result_batch - reload_result_batch)).max())  

#print(predict)
#pd.DataFrame(result_batch).to_csv("file.csv")