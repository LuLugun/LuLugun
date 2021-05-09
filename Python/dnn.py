import pandas as pd 
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.utils import to_categorical

df1 = pd.read_csv('test_images-1.csv')
df2 = pd.read_csv('test_labels.csv')

#cf1 = pd.read_csv('train_images.csv')
#cf2 = pd.read_csv('train_labels.csv')

p1 = pd.read_csv('submission.csv')

df1=df1.values
df2=df2.values
#cf1 = cf1.values
#cf2 = cf2.values
p1 = p1.values

model = Sequential()
model.add(Dense(1024, activation='relu', input_dim=18))
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(11, activation='softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['acc'])


test = model.fit(df1,df2,epochs = 50,batch_size = 288)
#test_loss,test_acc = model.evaluate(cf1,cf2)
#print(test_acc)

predict = model.predict(p1)
#print(predict)
pd.DataFrame(predict).to_csv("file.csv")