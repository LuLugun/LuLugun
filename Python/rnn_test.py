import numpy as np
import pandas as pd
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import LSTM


df1 = pd.read_csv('test_images-1.csv')
df2 = pd.read_csv('test_labels.csv')

traini = pd.read_csv('train_images-1.csv')
trainl = pd.read_csv('train_labels-1.csv')

p1 = pd.read_csv('submission.csv')

df1=df1.values
df2=df2.values
traini = traini.values
trainl = trainl.values
p1 = p1.values

traini=traini.reshape(5695,18)

#dfi = df1.reshape(4,7123,18)
#dfl = df2.reshape(4,7123,11)


#dfi = df1.reshape(28492,18)
#dfl = df2.reshape(28492,11)
#print("trainl.shape:",trainl.shape)
#print("traini.shape:",traini.shape)
#print("df1.shape:",df1.shape)



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

# 將數字資料轉成 one-hot 編碼
trainl = convert_to_integer(trainl)
#print("trainl:",trainl)
trainl= to_categorical(trainl)
#print("trainl.shape:",trainl.shape)
#print("trainl:",trainl)

traini= to_categorical(traini)
print("traini.shape:",traini.shape)
#print("traini:",traini)

#dfi = to_categorical(dfi[0])
#print("dfi.shape:",dfi.shape)
#df2 = convert_to_integer(df2)
#df2= to_categorical(dfl[0])



model = Sequential()
model.add(layers.SimpleRNN(512,
                           input_shape=(18,65501)))


model.add(layers.Dense(256, activation='sigmoid'))
model.add(layers.Dense(128, activation='sigmoid'))
model.add(layers.Dense(64, activation='sigmoid'))
model.add(layers.Dense(11, activation='sigmoid'))
model.summary()

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['acc'])

history = model.fit(
                    traini,
                    trainl,
                    epochs=100)

predict = model.predict(p1)
#print(predict)
pd.DataFrame(predict).to_csv("file.csv")