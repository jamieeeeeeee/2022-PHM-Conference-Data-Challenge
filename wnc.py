# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:52:18 2023

@author: USER
"""
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.layers import Input, Dense, GlobalAveragePooling2D, LSTM, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam, RMSprop
from keras.models import Model, Sequential
from keras.applications import DenseNet201
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import to_categorical


### 資料預處理
data_files = {
    'data_pdmp1': 'Data/data_pdmp1.csv',
    'data_pdmp2': 'Data/data_pdmp2.csv',
    'data_pdmp4': 'Data/data_pdmp4.csv',
    'data_pdmp5': 'Data/data_pdmp5.csv',
    'data_pdmp6': 'Data/data_pdmp6.csv',
    'data_pin1': 'Data/data_pin1.csv',
    'data_pin2': 'Data/data_pin2.csv',
    'data_pin4': 'Data/data_pin4.csv',
    'data_pin5': 'Data/data_pin5.csv',
    'data_pin6': 'Data/data_pin6.csv',
    'data_po1': 'Data/data_po1.csv',
    'data_po2': 'Data/data_po2.csv',
    'data_po4': 'Data/data_po4.csv',
    'data_po5': 'Data/data_po5.csv',
    'data_po6': 'Data/data_po6.csv'
}

datasets = {}
for key, file_path in data_files.items():
    dataset = pd.read_csv(file_path, header=None, usecols=range(571)).to_numpy()
    datasets[key] = dataset
    
    
    
combined_data = []
for key in ['data_pdmp1', 'data_pdmp2', 'data_pdmp4', 'data_pdmp5', 'data_pdmp6']:
    combined_data.append(datasets[key])

data_pdmp = np.concatenate(combined_data, axis=0)[:, 1:]

combined_data = []
for key in ['data_pin1', 'data_pin2', 'data_pin4', 'data_pin5', 'data_pin6']:
    combined_data.append(datasets[key])

data_pin = np.concatenate(combined_data, axis=0)[:, 1:]

combined_data = []
for key in ['data_po1', 'data_po2', 'data_po4', 'data_po5', 'data_po6']:
    combined_data.append(datasets[key])

data_po = np.concatenate(combined_data, axis=0)[:, 1:]    
    
    
### 標準化
mean = np.mean(data_pdmp, axis=1, keepdims=True)
std = np.std(data_pdmp, axis=1, keepdims=True)
data_pdmp = (data_pdmp - mean) / std


mean = np.mean(data_pin, axis=1, keepdims=True)
std = np.std(data_pin, axis=1, keepdims=True)
data_pin = (data_pin - mean) / std

mean = np.mean(data_po, axis=1, keepdims=True)
std = np.std(data_po, axis=1, keepdims=True)
data_po = (data_po - mean) / std
   
    

### X = features, Y = labels
features = np.stack([data_pdmp, data_pin, data_po])
labels = np.concatenate((combined_data[0][:,0],
                        combined_data[1][:,0],
                        combined_data[2][:,0],
                        combined_data[3][:,0],
                        combined_data[4][:,0]))


### 將資料轉換為符合 RNN 模型輸入格式的形狀
data_rnn = np.transpose(features, (1, 2, 0))  # 將維度 (3, 7311, 500) 轉換為 (7311, 3, 500)


### 進行資料分割成訓練集和測試集
train_data, test_data, train_labels, test_labels = train_test_split(data_rnn, 
                                                                    labels, 
                                                                    test_size=0.2, 
                                                                    random_state=42)
    
    
    
### one-HOT
labels_int  = train_labels.astype(int)
train_labels = np.zeros((len(train_labels), 11))
train_labels[np.arange(len(train_labels)), labels_int -1] = 1

labels_int  = test_labels.astype(int)
test_labels = np.zeros((len(test_labels), 11))
test_labels[np.arange(len(test_labels)), labels_int -1] = 1


# 建立 LSTM 模型
model = Sequential()
model.add(LSTM(64, input_shape=(570, 3),return_sequences=False)) 
model.add(Dropout(0.2))
model.add(Dense(units=11, activation='softmax'))  

# 編譯模型
model.compile(optimizer='RMSprop', loss='categorical_crossentropy', metrics=['accuracy'])

# 輸出模型摘要
model.summary()

# 進行模型訓練
model.fit(train_data, train_labels, validation_data=(test_data, test_labels), epochs=10, batch_size=32)
